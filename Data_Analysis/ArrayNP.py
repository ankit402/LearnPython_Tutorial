from logging import exception

import numpy as np

listdata = np.array([1,2,3,5])
print(listdata)

print(type(listdata))
#shape for array
arr1= np.array([[1,4,5,6],[1,2,3,5]])
#arr1 = np.array([[1, 0, 0, 0], [1, 2, 3, 5]])
print(arr1.shape)

#Use a tuple to create a NumPy array:
arra1= np.array((1,2,3,5))
print(arra1)

#Create a 0-D array with value 42
arr2= np.array(40)
print(arr2)

#Check Number of Dimensions?
b = np.array([1, 2, 3, 4, 5])
print(b.ndim)
c= np.array([
            [1, 2, 3, 4, 5],
             [4, 5, 6,8,9]
             ])
print(c.ndim)
k = np.array([
    [
        [2,3,4],
        [2,5,12],
        [5,7,8]
    ]
])
# print(k.ndim)
#
# #Higher Dimensional Arrays
# arr= np.array([1,4,5,6] , ndmin=5)
#
# print(arr)
# print('number of dimensions :', arr.ndim)
arr1= np.array([1,4,5,7,6])
arr1.reshape(1,5) # 1 row 5 column

print(arr1)
arr2= np.array([[1,4,5,7,6],[2,3,4,6,7]])
#arr2.reshape(2,5) # 1 row 5 column
print(arr2.shape)

a3= np.arange(0,10,2).reshape(5,1)
print(a3)

a4= np.ones((3,4))
print(a4)

#identity matrix
a= np.eye(2)
print(a)

arr2= np.array([[1,4,5,7,6],[2,3,4,6,7]])
k = arr2.dtype
print(k)
print(arr2.itemsize)


index = np.array([1,2,3,4,5])
print("indexing for 2 value is : " , index[2])

#Get third and fourth elements from the following array and add them.
index = np.array([1,2,3,4,5])
index2 = np.array([4,5,6,7,8])
print("index value addition : " , index[3]+ index2[4])

arr = np.array([[1,2,3,4,5], [6,7,8,9,10]])
print('Last element from 2nd dim: ', arr[1, -1])

#array slicing
arr = np.array([1, 2, 3, 4, 5, 6, 7])
#slicing concept is same like list
print(arr[::-1])

arr = np.array([1, 2, 3, 4, 5, 6, 7])
print(arr[:9])

#numpy works with array and linear algebra and matrices


#Checking the Data Type of an Array
arr = np.array([1, 2, 3, 4, 5, 6, 7])
print(arr.dtype)

ar2= np.array(["apple", "graphs", "Banana"])
print(ar2.dtype)

arr = np.array([1, 2, 3, 4], dtype='S')
print(arr.dtype)

#Change data type from float to integer by using int as parameter value:
arr = np.array([1.1, 2.1, 3.1])
newarr = arr.astype(int)

print(newarr)
print(newarr.dtype)

# arr2 = np.array(["apple"])
# try:
#     newarr2 = arr2.astype(int)
#     print(newarr2)
#     print(newarr2.dtype)
# except Exception as ex:  # ← 'Exception' should be capitalized
#     raise ValueError(ex)  # ← Raise a new ValueError with original exception message

arr = np.array([1, 0, 3])
newarr = arr.astype(bool)
print(newarr)
print(newarr.dtype)