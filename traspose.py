import numpy as np

a = np.array([2, 3, 4])

# Transpose using numpy.transpose()
transposed_a = np.transpose(a)

# Or you can use the T attribute
transposed_a = a.T

print("Original array:")
print(a.shape)
print("Transposed array:")
print(transposed_a.shape)