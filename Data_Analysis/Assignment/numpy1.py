
#Module: NumPy Assignments\n

# Create a NumPy array of shape (5, 5) filled with random integers between 1 and 20.
# Replace all the elements in the third column with 1.\n"

import numpy as np
import random as rand
arr = np.random.randint(1, 21, size=(5, 5))
print("Original array:\n", arr)

arr[:,2]=1
print("Filtered array:\n", arr)

arr[:,1]=0
print("Filtered array:\n", arr)


#Create a NumPy array of shape (4, 4) with values from 1 to 16. Replace the diagonal elements with 0.\n",
arr2= np.arange(1,17).reshape(4,4)
np.fill_diagonal(arr2, 0)
print("Filtered array:\n", arr2)


# "### Assignment 2: Array Indexing and Slicing\n",

#Create a NumPy array of shape (6, 6) with values from 1 to 36.
# Extract the sub-array consisting of the 3rd to 5th rows and 2nd to 4th columns.\n",

arr3= np.random.randint(1, 37, size=(6,6))
print(" array:\n", arr3)

#Rows: index 2 to 4 → 3rd to 5th row

#Columns: index 1 to 3 → 2nd to 4th column

print("Extract the sub-array consisting of the 3rd to 5th rows" , arr3[2:5, 1:4])


#Rows: index 1 to 2 → 2nd to 3rd row 1:3

#Columns: index 2 to 4 → 3rd to 5th column 2:5

print("2 Extract the sub-array consisting of the 3rd to 5th rows" , arr3[1:3, 2:5])

#Create a NumPy array of shape (5, 5) with random integers. Extract the elements on the border.\n"
arr3= np.random.randint(1, 10, size=(5,5))
print("first row:\n", arr3)
print("first row/column:\n", arr3[:,0])

'''🔍 Now, the slicing: arr[1:-1, 0]
1. 1:-1 for the row index:
This means: start from row index 1 (the second row), up to but not including the last row (-1).

So you're selecting rows: 1, 2, 3, 4.

2. 0 for the column index:
This picks only the first column (index 0).'''




# Assignment 3: Array Operations\n"

#Create two NumPy arrays of shape (3, 4) filled with random integers.
# Perform element-wise addition, subtraction, multiplication, and division.\n",
#"2. Create a NumPy array of shape (4, 4) with values from 1 to 16.
# Compute the row-wise and column-wise sum.\n",


arr= np.random.randint(2, 20, size=(3,4))
arr2= np.random.randint(3, 30, size=(3,4))

print("Addition:\n", arr+ arr2)
print("Substraction:\n", arr - arr2)
print("Multiplication:\n", arr * arr2)
print("Division:\n", arr / arr2)

arr_data = np.random.randint(1, 16, size=(2,2))
print("Array data:\n", arr_data)
print("Compute row-wise axis always on 0:\n" , np.sum(arr_data, axis=0))
print("Compute column-wise axis always on 1:\n" , np.sum(arr_data, axis=1))





