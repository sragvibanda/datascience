"""
4)Create a 4x4 NumPy array filled with random integers between 1 and 100. Then, reshape this 
array into two separate 2D arrays, where one represents the rows and the other represents 
the columns. Write a function, preferably using a lambda function, to calculate the 
sum of each row and each column separately, and return the results as two separate NumPy arrays

"""

import numpy as np

random_array = np.random.randint(1, 101, size=(4, 4))
sum_axis = lambda arr, axis: np.sum(arr, axis=axis)
sums_rows = sum_axis(random_array, axis=1)
sums_columns = sum_axis(random_array, axis=0)

print("Sum of each row:", sums_rows)
print("Sum of each column:", sums_columns)

