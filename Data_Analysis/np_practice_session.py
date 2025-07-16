

import numpy as np
import random
arr_data = np.array([x for x in range(1,5)])
print("arr_data: ", arr_data)

#"1. Create a NumPy array of shape (5, 5) filled with random integers between 1 and 20.
# Replace all the elements in the third column with 1.\n",
#"2. Create a NumPy array of shape (4, 4) with values from 1 to 16.
# Replace the diagonal elements with 0.\n",

arr_2 = np.random.randint(1,21, (5,5))
arr_2[:,2] = 1  # array[row, col]
print(arr_2)

arr_2[2,:] = 0
print(arr_2)

nm_array = np.random.randint(1 , 17 , (4,4))
np.fill_diagonal(nm_array, 0)
print("Filtered array:\n", nm_array)
#"1. Create a NumPy array of shape (6, 6) with values from 1 to 36.
# Extract the sub-array consisting of the 3rd to 5th rows and 2nd to 4th columns.\n",
   # "2. Create a NumPy array of shape (5, 5) with random integers.
# Extract the elements on the border.\n",

numarray = np.random.randint(1, 37, (6,6))
numarray[2:5, 1:4] # [row_start , row_end , row_step , col_start , col_end , col_step]
print(numarray)

#  "1. Create two NumPy arrays of shape (3, 4) filled with random integers.
#  Perform element-wise addition, subtraction, multiplication, and division.\n",
#   "2. Create a NumPy array of shape (4, 4) with values from 1 to 16.
#  Compute the row-wise and column-wise sum.\n",

num_1 = np.random.randint(1, 5, (3,4))
num_2 = np.random.randint(1, 5, (3,4))
arr= num_1 * num_2
print(arr)
print("first row/column:\n", arr[:,0])

#Create a NumPy array of shape (4, 4) with values from 1 to 16.
# Compute the row-wise and column-wise sum.

num = np.arange(1,17).reshape(4,4)
print(np.sum(num, axis=0))
print(np.sum(num, axis=1))


