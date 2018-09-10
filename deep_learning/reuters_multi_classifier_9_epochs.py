import matplotlib.pyplot as plt
from keras.datasets import reuters
import numpy as np
from deep_learning.common_functions.common import vectorize_sequences
from keras.utils.np_utils import to_categorical
from keras import models, layers
import copy

(train_data, train_labels), (test_data, test_labels) = reuters.load_data(num_words=10000)

print(max(train_labels))
print(max(test_labels))

# Decoding newswires back to text
word_index = reuters.get_word_index()
reverse_word_index = dict([(value, key) for (key, value) in word_index.items()])
decoded_newswire = ' ' . join([reverse_word_index.get(i - 3, '?') for i in train_data[0]])
print(decoded_newswire)

x_train = vectorize_sequences(train_data)
x_test = vectorize_sequences(test_data)

def to_one_hot(labels, dimension=46):
    results = np.zeros((len(labels), dimension))
    for i, label in enumerate(labels):
        results[i, label] = 1.
    return results

one_hot_train_labels = to_one_hot(train_labels)
one_hot_test_labels = to_one_hot(test_labels)

one_hot_train_labels = to_categorical(train_labels)
one_hot_test_labels = to_categorical(test_labels)

model = models.Sequential()
model.add(layers.Dense(64, activation='relu', input_shape=(10000, )))
model.add(layers.Dense(64, activation='relu'))
# model.add(layers.Dense(4, activation='relu'))
model.add(layers.Dense(46, activation='softmax'))

model.compile(optimizer='rmsprop',
              loss='categorical_crossentropy',
              metrics=['accuracy'])

x_val = x_train[:1000]
partial_x_train = x_train[1000:]

y_val = one_hot_train_labels[:1000]
partial_y_train = one_hot_train_labels[1000:]

history = model.fit(partial_x_train,
                    partial_y_train,
                    epochs=21,
                    batch_size=128,
                    validation_data=(x_val, y_val))

results = model.evaluate(x_test, one_hot_test_labels)
print(results)

test_labels_copy = copy.copy(test_labels)
np.random.shuffle(test_labels_copy)
hits_array = np.array(test_labels) == np.array(test_labels_copy)
print(len(test_labels))
print(np.sum(hits_array))
# loss in %
print(float(np.sum(hits_array)) / len(test_labels))

predictions = model.predict(x_test)
print(predictions[0].shape)
print(np.sum(predictions[0]))
print(np.argmax(predictions[0]))
# print(predictions)
for x in predictions[0]: print('%f' % x)

# Different way to handle the labels and the loss
y_train = np.array(train_labels)
y_test = np.array(test_labels)

print(y_train)
print(y_test)

# model.compile(optimizer='rmsprop',
#               loss='sparse_categorical_crossentropy',
#               metrics=['acc'])
