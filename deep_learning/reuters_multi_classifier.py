from keras.datasets import reuters
import numpy as np
from deep_learning.common_functions.common import vectorize_sequences
from keras.utils.np_utils import to_categorical
from keras import models, layers

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
model.add(layers.Dense(46, activation='softmax'))

