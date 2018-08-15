import numpy as np
x = np.array(12)
print(x)
print(x.ndim)

x = np.array([12, 3, 6, 14])
print(x)
print(x.ndim)
#2D tensor
x = np.array([
    [5, 62, 2, 43, 0],
    [5, 62, 2, 43, 0],
    [5, 62, 2, 43, 0],
              ])
print(x)
print(x.ndim)

#3D tensor
x = np.array([[
    [5, 62, 2, 43, 0],
    [5, 62, 2, 43, 0],
    [5, 62, 2, 43, 0]],
    [[5, 62, 2, 43, 0],
    [5, 62, 2, 43, 0],
    [5, 62, 2, 43, 0]],
    [[5, 62, 2, 43, 0],
    [5, 62, 2, 43, 0],
    [5, 62, 2, 43, 0]],
])
print(x)
print(x.ndim)