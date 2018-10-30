import keras
from keras import layers
from keras.datasets import imdb
from keras.preprocessing import sequence

# Number of words to consider as features
max_features = 2000
# Cuts off texts after this number of words (among max_features most common words)
max_len = 500

(x_train, y_train), (x_test, y_test) = imdb.load_data(num_words=max_features)
x_train = sequence.pad_sequences(x_train, maxlen=max_len)
x_test = sequence.pad_sequences(x_test, maxlen=max_len)

model = keras.models.Sequential()
model.add(layers.Embedding(max_features, 128,
                           input_length=max_len,
                           name='embed'))
model.add(layers.Conv1D(32, 7, activation='relu'))
model.add(layers.MaxPooling1D(5))
model.add(layers.Conv1D(32, 7, activation='relu'))
model.add(layers.GlobalMaxPool1D())
model.add(layers.Dense(1))
model.summary()
model.compile(optimizer='rmsprop',
              loss='binary_crossentropy',
              metrics=['acc'])

# tensorboard --logdir=my_log_dir
callbacks = [
    keras.callbacks.TensorBoard(
        # Log files will be written at this location
        log_dir='my_log_dir',
        # Records activation histograms every 1 epochs
        histogram_freq=1,
        # Records embedding data every 1 epoch
        embeddings_freq=1,
    )
]
history = model.fit(x_train, y_train,
                    epochs=20,
                    batch_size=128,
                    validation_split=0.2,
                    callbacks=callbacks)

from keras.utils import plot_model

plot_model(model, to_file='model.png')
plot_model(model, show_shapes=True, to_file='model.png')

