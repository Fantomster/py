from keras.datasets import mnist
import matplotlib.pyplot as plt

(train_images, train_labels), (test_images, test_labels) = mnist.load_data()

print(train_images.shape)
print(len(train_images[0][0]))
print(len(train_labels))
print(train_labels)

print(test_images.shape)
print(len(test_labels))
print(test_labels)

digit = train_images[4]
plt.imshow(digit, cmap=plt.cm.binary)
plt.show()

# my_slice = train_images[10:100]
# print(my_slice.shape)
