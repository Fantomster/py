from keras import layers, applications, Input

# The base image-processing model is the Xception network(convolution base only)
xception_base = applications.Xception(weights=None, include_top=False)

# The inputs are 250 x 250 RGB images
left_input = Input(shape=(250, 250, 3))
right_input = Input(shape=(250, 250, 3))

# Calls the same vision model twice
left_features = xception_base(left_input)
right_input = xception_base(right_input)

# The merged features contain information from the right visual feed and the left visual feed
merged_features = layers.concatenate([left_features, right_input], axis=-1)