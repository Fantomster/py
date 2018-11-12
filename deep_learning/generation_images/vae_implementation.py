# Encodes the input into a mean and variance parameter
z_mean, z_log_variance = encoder(input_img)

# Draws a latent point using a small random epsilon
z = z_mean + exp(z_log_variance) * epsilon

# Instantiates the autoencoder model, which maps an input image to its reconstruction
reconstructed_img = decoder(z)

model = Model(input_img, reconstructed_img)

