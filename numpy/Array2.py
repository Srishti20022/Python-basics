import numpy as np
x = np.array([5, 3, 9, -5])
print(x[0])
print(x[::2])
print(np.random.randint(5))
print(np.max(x))
print(np.min(x))
# arg in front of every function gives index for every function
print(np.argmin(x))
# np.sort() doesnot sort the actual array but returns the value of sorted array
np.sort(x)
print(x)
print(np.argsort(x))
y = np.array([[1, 2, 3, 4, 5, -4], [6, 7, 8, 9, 10, -3], [11, 12, 13, 14, 15, -2], [16, 17, 18, 19, 20, -1]])
# to get the total number of elements
print(y.shape)
# returns dimension whether 1 dimension or 2 dimension
print(y.ndim)
# flatten function does not change the value of y but just return an array which is not stored anywhere
y.flatten()
print(y)
print(y.flatten())
print(y.reshape(2, 12))
z = np.array([[1, 2, 3, 4, 5, -4], [6, 7, 8, 9, 10, -3], [11, 12, 13, 14, 15, -2], [16, 17, 18, 19, 20, -1]])
print(np.hstack((y, z)))