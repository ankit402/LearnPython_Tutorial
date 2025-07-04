#array slicing

#Syntax for 1-D Array --> arr[start_index: end_index : step]

#Syntax for 2-D Array --> arr[row_start:row_stop: row_step, col_start:col_stop: col_step]
import numpy as np
import random as rand

#[expression for item in iterable if condition]
#[expression : iteration : condition]
#[x*2 : for x in range(10) : if (x>2)]
arr = np.array([x for x in range(22)])
print(arr[0:22:2])

arr2 = np.array([x for x in range(22) if x>0])
print(arr2[1:22:2])

#NumPy Array Slicing

#Array slicing is the process of extracting the portion of the array.

#Syntax of NumPy Array Slicing

#arr[start_index:end_index:step]

'''
start - index of the first element to be included in the slice
stop - index of the last element (exclusive)
step - step size between each element in the slice
'''

'''
Note: When we slice arrays, the start index is inclusive but the stop index is exclusive.
If we omit start, slicing starts from the first element
If we omit stop, slicing continues up to the last element
If we omit step, default step size is 1
'''

#1-D Numpy Array Slicing

#create a 1D array
arr= np.arange(10)
print(arr)

# slicing operator :

arr= np.array([1,2,3,4,5])
print("Slicing 1-D array", arr[0:3:1])

# slice array1 from index 2 to index 6 (exclusive)

arr= np.array([1, 3, 5, 7, 8, 9, 2, 4, 6])
print("slice array1 from index 2 to index 6 (exclusive)", arr[2:5]) #arr[start_index-2:end_index-5:step-0]

## slice array1 from index 0 to index 8 (exclusive) with a step size of 2
print("slice array1 from index 0 to index 8 (exclusive) with a step size of 2" , arr[0:8:2])   #arr[start_index-2:end_index-5:step-2]

# slice array1 from index 3 up to the last element
print("slice array1 from index 3 up to the last element" , arr[3:])

# items from start to end
print("items from start to end", arr[:])

'''Then, we used the slicing operator : to slice array elements.

array1[2:6] - slices array1 from index 2 to index 6, not including index 6
array1[0:8:2] - slices array1 from index 0 to index 8, not including index 8
array1[3:] - slices array1 from index 3 up to the last element
array1[:] - returns all items from beginning to end'''

#Modify Array Elements Using Slicing

'''With slicing, we can also modify array elements using:

start parameter
stop parameter
start and stop parameter
start, stop, and step parameter'''

#1 Using start Parameter
arr= np.array([1, 3, 5, 7, 8, 9, 2, 4, 6])
arr[3:]= 33 ## modify elements from index 3 onwards
print("Using start Parameter" , arr)

#Here, numbers[3:] = 20 replaces all the elements from index 3 onwards with new value 33.

#2 Using stop Parameter
arr= np.array([1, 3, 5, 7, 8, 9, 2, 4, 6])
arr[:3:] = 33  #modify the first 3 elements
print("Using stop Parameter" , arr)


#Here, numbers[:3] = 20 replaces the first 3 elements with the new value 33.

#3 Using start and stop parameter

arr= np.array([1, 3, 5, 7, 8, 9, 2, 4, 6])
arr[3:5]=33 # modify elements from indices 3 to 5
print("Using Start/Stop Parameter" , arr)

#Using start, stop, and step parameter
arr= np.array([1, 3, 5, 7, 8, 9, 2, 4, 6])
arr[2:5:2]=33 # modify elements from indices 3 to 5
print("Using Start/Stop Parameter" , arr)

'''NumPy Array Negative Slicing'''

#slice the last 3 elements of the array
arr= np.array([1, 3, 5, 7, 8, 9, 2, 4, 6])
# During negative slicing, elements are accessed from the end of the array.
print("slice the last 3 elements of the array" , arr[-3])

#slice elements from 2nd-to-last to 4th-to-last element
arr= np.array([1, 3, 5, 7, 8, 9, 2, 4, 6])
print("slice elements from 2nd-to-last to 4th-to-last element" , arr[-5:-4])

'''How slicing with negative indices works:
Negative indices count from the end of the array:


#[1, 2, 3, 4, 6, 8, 10] [-7,-6,-5,-4,-3,-2,-1]
-1 → last element (10)
-2 → second last (8)
-3 → third last (6)
-4 → fourth last (4)
-5 → fifth last (3)
So, numbers[-5:-2] means:
Start at index -5 (which is 3, the 5th from last element)'''

#slice every other element of the array from the end

arr= np.array([1, 3, 5, 7, 8, 9, 2, 4, 6])
print('1st last element', arr[-1::-2])
print('2nd last element', arr[-2:])
print('3rd last element', arr[-3])
print('4th last element', arr[-4])
print('5th last element', arr[-5])
print('6th last element', arr[-6])

# if last we dont know keep blank

#Reverse NumPy Array Using Negative Slicing

#start to 3 and end at last
arr= np.array([1, 3, 5, 7, 8, 9, 2, 4, 6])
#enumerator is use for showing the indexing from the collection of data
for i,x in enumerate(arr):
    print("indexing :" ,i , arr[x:])


#get the middle value from the array


#Reverse NumPy Array Using Negative Slicing

'''Syntax of 2D NumPy Array Slicing
array[row_start:row_stop:row_step, col_start:col_stop:col_step]'''

arr= np.array(
    [[1,4,5], [5,9,6]])

print(arr[0:2, 1:2])

#Example: 2D NumPy Array Slicing

arr= np.array(
    [[1,4,5], [5,9,6], [4,5,6]])

# slice the array to get the first two rows and columns
print(arr[0:2,1:2])

# slice the array to get the last two rows and columns
'''✅ 2. Slice the last two rows and columns
Last 2 rows → indices 1 and 2 → arr[1:3, ...]

Last 2 columns → indices 1 and 2 → arr[..., 1:3]'''
print("slice the array to get the last two rows and columns", arr[1:3 , 1:3])
