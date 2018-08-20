import numpy as np


# z = np.dot(x, y)

# is

def naive_vector_dot(x, y):
    assert len(x.shape) == 1
    assert len(y.shape) == 1
    assert x.shape[0] == y.shape[0]

    z = 0
    for i in range(x.shape[0]):
        z += x[i] * y[i]

    return z


print(naive_vector_dot(np.array([1, 2, 3]), np.array([1, 2, 3])))


def naive_matrix_vector_dot(x, y):
    assert len(x.shape) == 2
    assert len(y.shape) == 1
    assert x.shape[1] == y.shape[0]

    z = np.zeros(x.shape[0])
    for i in range(x.shape[0]):
        for j in range(x.shape[1]):
            z[i] += x[i, j] * y[j]

    return z


x = np.array([[1, 2, 3, 4],
              [1, 2, 3, 4],
              [1, 2, 3, 4],
              [1, 2, 3, 4],
              [1, 2, 3, 4],
              [1, 2, 3, 4],
              [1, 2, 3, 4],])
print(x.shape)
y = np.array([1, 2, 3, 4])
print(naive_matrix_vector_dot(x, y))

# refactoring realization
def naive_matrix_vector_dot1(x, y):
    z = np.zeros(x.shape[0])
    for i in range(x.shape[0]):
        z[i] = naive_vector_dot(x[i, :], y)

    return z

def naive_matrix_dot(x, y):
    assert len(x.shape) == 2
    assert len(y.shape) == 2
    assert x.shape[1] == y.shape[0]

    z = np.zeros((x.shape[0], y.shape[1]))
    for i in range(x.shape[0]):
        for j in range(y.shape[1]):
            row_x = x[i, :]
            column_y = y[:, j]
            z[i, j] = naive_vector_dot(row_x, column_y)

    return z

y = np.array([[1, 2, 3],
              [1, 2, 3],
              [1, 2, 3],
              [1, 2, 3],])
print(x.shape)
print(y.shape)
print(naive_matrix_dot(x, y))

# Reshaping

x = np.array([[0., 1.],
              [2., 3.],
              [4., 5.]])
print(x.shape)

x = x.reshape((6,1))

print(x)

x = x.reshape((2, 3))
print(x)

x = np.zeros((300, 20))
# x = np.transpose(x)
print(x)