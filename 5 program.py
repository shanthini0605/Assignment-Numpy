# Create a 10x10 array with random values and find the minimum and maximum values.

import numpy as np
# Create a 10x10 array with random values between 0 and 1
array = np.random.rand(10, 10)
# Find the minimum and maximum values
min_value = np.min(array)
max_value = np.max(array)
print("Array:")
print(array)
print("\nMinimum Value:", min_value)
print("Maximum Value:", max_value)
