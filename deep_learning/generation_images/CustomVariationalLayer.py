import keras
from keras import backend as K

class CustomVariationalLayer(keras.layers.Layer):

    def vae_loss(self, x, z_decoded, z_mean, z_log_var):
        x = K.flatten(x)
        z_decoded = K.flatten(z_decoded)
        xent_loss = keras.metrics.binary_crossentropy(x, z_decoded)
        kl_loss = -5e-4 * K.mean(
            1 + z_log_var - K.square(z_mean) - K.exp(z_log_var), axis=-1)
        return K.mean(xent_loss + kl_loss)

    # You implement custom layers by writing a call method
    def call(self, inputs):
        x = inputs[0]
        z_decoded = inputs[1]
        z_mean = inputs[2]
        z_log_var = inputs[3]
        loss = self.vae_loss(x, z_decoded, z_mean, z_log_var)
        self.add_loss(loss, inputs=inputs)
        # You dont use this output, but the layer must return something
        return x
