import numpy as np
from keras import layers

normalized_data = (data - np.mean(data, axis=...)) / np.std(data, axis=...)

conv_model.add(layers.Conv2D(32, 3, activation='relu'))
conv_model.add(layers.BatchNormalization())

dense_model.add(layers.Dense(32, activation='relu'))
dense_model.add(layers.BatchNormalization())

