#"### Assignment 6: Linear Algebra\n",
#"1. Create a NumPy array of shape (3, 3) representing a matrix.
# Compute its determinant, inverse, and eigenvalues.\n",
# Create two NumPy arrays of shape (2, 3) and (3, 2).
# Perform matrix multiplication on these arrays.\n",


import random as rand
from email.message import Message

import numpy as np
import tkinter as tk
from tkinter import filedialog, messagebox, scrolledtext
#Create a NumPy array of shape (3, 3) representing a matrix
arr_np= np.random.randint(1,20 , size=(3,3))
print(arr_np)

# Create two NumPy arrays of shape (2, 3) and (3, 2).
arr_m1= np.random.randint(1,20 , size=(2,3))
arr_m2= np.random.randint(1,20 , size=(3,2))
print(arr_m1)
print(arr_m2)

#np.dot is using for multiplication
print("Perform matrix multiplication on these arrays.", np.dot(arr_m2, arr_m1))

# "### Assignment 7: Advanced Array Manipulation\n",

"1. Create a NumPy array of shape (3, 3) with values from 1 to 9.Reshape the array to shape (1, 9) and then to shape (9, 1).\n"
"2. Create a NumPy array of shape (5, 5) filled with random integers.Flatten the array and then reshape it back to (5, 5).\n"

arr_man= np.random.randint(1,10 , size=(3,3))
# Reshape to (1, 9)
A_1x9 = arr_man.reshape(1,9)
A_9x1 = arr_man.reshape(9,1)
print(A_1x9)
print(A_9x1)


arr_manshape= np.random.randint(1,10 , size=(5,5))
# Flatten the array to a 1D array
flattened = arr_manshape.flatten()

ravel = arr_manshape.ravel()

#print(messagebox.showinfo("Message", "The array is equal to the flattened array."))

print(".ravel()" , ravel)
print("\nFlattened array:\n", flattened)
A_flattern= arr_manshape.reshape(5,5)
print(A_flattern)
print("\nReshaped back to (5x5):\n", A_flattern)