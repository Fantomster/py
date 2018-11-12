"""
Vector data - densely connected network ( Dense layers ).
Image data - 2D convnets
Sound data (for example, waveform)—Either 1D convnets (preferred) or RNNs.
Text data—Either 1D convnets (preferred) or RNNs.
Timeseries data—Either RNNs (preferred) or 1D convnets.
Other types of sequence data — Either RNNs or 1D convnets. Prefer RNNs if data
ordering is strongly meaningful (for example, for timeseries, but not for text).
Video data—Either 3D convnets (if you need to capture motion effects) or a combination of a frame-level 2D convnet for feature extraction followed by
either an RNN or a 1D convnet to process the resulting sequences.
Volumetric data—3D convnets.
"""

# Densely connected networks
# for binary classification

from keras import models, layers

model = models.Sequential()
model.add(layers.Dense(32, activation='relu', input_shape=(num_input_features,)))
model.add(layers.Dense(32, activation='relu'))
model.add(layers.Dense(1, activation='sigmoid'))

model.compile(optimizer='rmsprop', loss='binary_crossentropy')

# Single-label categorical classification
# if targets integers, use sparse_categorical_crossentropy

model = models.Sequential()
model.add(layers.Dense(32, activation='relu', input_shape=(num_input_features,)))
model.add(layers.Dense(32, activation='relu'))
model.add(layers.Dense(num_classes, activation='softmax'))

# one-hot encoded targets
model.compile(optimizer='rmsprop', loss='categorical_crossentropy')

# Multilabel categorical classification
# use K-hot encoded

model = models.Sequential()
model.add(layers.Dense(32, activation='relu', input_shape=(num_input_features,)))
model.add(layers.Dense(32, activation='relu'))
model.add(layers.Dense(num_classes, activation='sigmoid'))

model.compile(optimizer='rmsprop', loss='binary_crossentropy')


# regression
# use mean_squared_error and mean_absolute_error for loss function
model = models.Sequential()
model.add(layers.Dense(32, activation='relu', input_shape=(num_input_features,)))
model.add(layers.Dense(32, activation='relu'))
model.add(layers.Dense(num_values))

model.compile(optimizer='rmsprop', loss='mse')

# Convnets
# Typical image-classification network

model = models.Sequential()
model.add(layers.SeparableConv2D(32, 3, activation='relu', input_shape=(height, width, channels)))
model.add(layers.SeparableConv2D(64, 3, activation='relu'))
model.add(layers.MaxPooling2D(2))
model.add(layers.SeparableConv2D(64, 3, activation='relu'))
model.add(layers.SeparableConv2D(128, 3, activation='relu'))
model.add(layers.MaxPooling2D(2))
model.add(layers.SeparableConv2D(64, 3, activation='relu'))
model.add(layers.SeparableConv2D(128,3, activation='relu'))
model.add(layers.GlobalAveragePooling2D())
model.add(layers.Dense(32, activation='relu'))
model.add(layers.Dense(num_classes, activation='softmax'))

model.compile(optimizer='rmsprop', loss='categorical_crossentropy')

# RNN
# binary classification of vector sequences
model = models.Sequential()
model.add(layers.LSTM(32, input_shape=(num_timesteps, num_features)))
model.add(layers.Dense(num_classes, activation='sigmoid'))
model.compile(optimizer='rmsprop', loss='binary_crossentropy')

# Stacked binary classification of vector sequences
model = models.Sequential()
model.add(layers.LSTM(32, return_sequences=True, input_shape=(num_timesteps, num_features)))
model.add(layers.LSTM(32, return_sequences=True))
model.add(layers.LSTM(32))
model.add(layers.Dense(num_classes, activation='sigmoid'))

model.compile(optimizer='rmsprop', loss='binary_crossentropy')