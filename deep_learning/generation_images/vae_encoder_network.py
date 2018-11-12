import keras
from keras import layers
from keras import backend as K
from keras.models import Model
import numpy as np
from deep_learning.generation_images import CustomVariationalLayer
from keras.datasets import mnist
import matplotlib.pyplot as plt
from scipy.stats import norm

img_shape = (28, 28, 1)
batch_size = 16
latent_dim = 2

input_img = keras.Input(shape=img_shape)
x = layers.Conv2D(32, 3, padding='same', activation='relu')(input_img)
x = layers.Conv2D(64, 3, padding='same', activation='relu', strides=(2, 2))(x)
x = layers.Conv2D(64, 3, padding='same', activation='relu')(x)
x = layers.Conv2D(64, 3, padding='same', activation='relu')(x)
shape_before_flattening = K.int_shape(x)

x = layers.Flatten()(x)
x = layers.Dense(32, activation='relu')(x)

# The input image ends up being encoded into these two parameters
z_mean = layers.Dense(latent_dim)(x)
z_log_var = layers.Dense(latent_dim)(x)

def sampling(args):
    z_mean, z_log_var = args
    epsilon = K.random_normal(shape=(K.shape(z_mean)[0], latent_dim),
                              mean=0., stddev=1.)
    return z_mean + K.exp(z_log_var) * epsilon

z = layers.Lambda(sampling)([z_mean, z_log_var])

# Input where you'll feed z
decoder_input = layers.Input(K.int_shape(z)[1:])
# Upsamples the input
x = layers.Dense(np.prod(shape_before_flattening[1:]), activation='relu')(decoder_input)
"""
 Reshapes z into a feature map of the same shape as the feature
 map just before the last Flatten layer in the encoder model
"""
x = layers.Reshape(shape_before_flattening[1:])(x)
"""
 Uses a Conv2DTranspose layer and Conv2D layer to decode z into a feature map
 the same size as the original image input
"""
x = layers.Conv2DTranspose(32, 3, padding='same', activation='relu', strides=(2, 2))(x)
x = layers.Conv2D(1, 3, padding='same', activation='sigmoid')(x)

# Instantiates the decoder model which turns "decoder_input" into the decoded image
decoder = Model(decoder_input, x)
# Applies it to z to recover the decoded z
z_decoded = decoder(z)

"""
Calls the custom layer on the input and the 
decoded output to obtain the final model output
"""
y = CustomVariationalLayer()([input_img, z_decoded, z_mean, z_log_var])

vae = Model(input_img, y)
vae.compile(optimizer='rmsprop', loss=None)
vae.summary()

(x_train, _), (x_test, y_test) = mnist.load_data()

x_train = x_train.astype('float32') / 255.
x_train = x_train.reshape(x_train.shape + (1,))
x_test = x_test.astype('float32') / 255.
x_test = x_test.reshape(x_test.shape + (1,))

vae.fit(x=x_train, y=None,
        shuffle=True,
        epochs=10,
        batch_size=batch_size,
        validation_data=(x_test, None))

# You'll display a grid of 15 x 15 digits (255 digits total)
n = 15
"""
Transforms linearly spaces coordinates using the SciPy ppf function to produce
values of the latent variable z (because the prior of the latent spave is Gaussian)
"""
digit_size = 28
figure = np.zeros((digit_size * n, digit_size * n))
grid_x = norm.ppf(np.linspace(0.05, 0.95, n))
grid_y = norm.ppf(np.linspace(0.05, 0.95, n))

for i, yi in enumerate(grid_x):
    for j, xi in enumerate(grid_y):
        z_sample = np.array([[xi, yi]])
        # Repeats z multiple times to form a complete batch
        z_sample = np.tile(z_sample, batch_size).reshape(batch_size, 2)
        # Decodes the batch into digit images
        x_decoded = decoder.predict(z_sample, batch_size=batch_size)
        # Reshapes the first digit in the batch from 28 x 28 x 1 to 28 x 28
        digit = x_decoded[0].reshape(digit_size, digit_size)
        figure[i * digit_size: (i + 1) * digit_size,
               j * digit_size: (j + 1) * digit_size] = digit

plt.figure(figsize=(10, 10))
plt.imshow(figure, cmap='Greys_r')
plt.show()


