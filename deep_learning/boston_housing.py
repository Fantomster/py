from keras.datasets import boston_housing

(train_data, train_targets), (test_data, test_targets) = boston_housing.load_data()

mean = train_data.mean(axis=0)
train_data -= mean
std = train_data.std(axis=0)
train_data /= std

test_data -= mean
test_data /= std

print(test_data)
print()
print(train_data)
print()
print(mean)
for x in mean: print('%f' % x)
print(std)
for x in std: print('%f' % x)
