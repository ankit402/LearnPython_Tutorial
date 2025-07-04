#Assignment 4: Statistical Operations\n",

#Create a NumPy array of shape (5, 5) filled with random integers.
# Compute the mean, median, standard deviation, and variance of the array.\n",
#"2. Create a NumPy array of shape (3, 3) with values from 1 to 9.
# Normalize the array (i.e., scale the values to have a mean of 0 and a standard deviation of 1).\n"
import numpy as np
import random as rand
arr_np= np.random.randint(1, 10 , size=(5,5))
print("Mean of the array", np.mean(arr_np))
print("Median of the array", np.median(arr_np))
print("Standard deviation of the array", np.std(arr_np))

arr_np2= np.random.randint(1, 9 , size=(3,3))
print(np.mean(arr_np2))
print(np.median(arr_np2))
print(np.std(arr_np2))

#formula normalized_arr = (arr - mean) / std

normalization =(arr_np2 - np.mean(arr_np))/ np.std(arr_np2)
print("Normalization :\n" ,normalization)

# Assignment 5: Broadcasting\n

#Create a NumPy array of shape (3, 3) filled with random integers.
# Add a 1D array of shape (3,) to each row of the 2D array using broadcasting.\n",


arr_bd= np.random.randint(1, 10 , size=(3,3))
b= 6
broadcast = arr_bd + b
print(broadcast)

arr_2d= np.array([[2,3,4],
                  [3,4,6]
                  ])

arr_broad= np.array([1,2,4])

result = arr_2d + arr_broad
print(result)

# #"2. Create a NumPy array of shape (4, 4) filled with random integers.
# Subtract a 1D array of shape (4,) from each column of the 2D array using broadcasting.\n",

arr_bd= np.random.randint(1, 10 , size=(4,4))
# Reshape to (4, 1) so it broadcasts across columns
arr_d= np.array([1,2,3,4]) # size=(4,))
# Reshape to (4, 1) so it broadcasts across columns
result = arr_bd - arr_d[:, np.newaxis]
print(result)

''''
✅ What does "broadcast" mean in NumPy?
    Broadcasting is a powerful NumPy feature that allows you to perform operations on arrays of different shapes 
    without explicitly reshaping or replicating them.

It automatically expands the smaller array across the larger one so that element-wise
 operations can be performed as if the shapes matched.
 '''

arr_1 = np.random.randint(1, 10 , size=(5,5))

arr_2 = np.array([5,10,15,20,25])

result = arr_1+ arr_2[:, np.newaxis]
print("Broadcasting 2D array 1D array", result)

result = arr_1 - arr_2[:, np.newaxis]
print("Broadcasting 2D array 1D array", result)

result = arr_1 * arr_2[:, np.newaxis]
print("Broadcasting 2D array 1D array", result)


arr_a= np.array([2,3,4,5])
arr_b= np.array([1,2,3,4])

result = arr_a + arr_b[:, np.newaxis]
print("Broadcasting 1D array 1D array\n", result)


arr_1 = np.random.randint(1, 10 , size=(5,5))

arr_2 = np.random.randint(1, 10 , size=(5,5))

result = arr_1 + arr_2[:, np.newaxis]
print("Broadcasting 2D" , result)
