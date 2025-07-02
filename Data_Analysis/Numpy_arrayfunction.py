#Numpy intro
from numpy.ma.extras import ndenumerate

print("*********Numpy intro*************")
print("Numpy is working with working with arrays.functions for working in domain of linear algebra, fourier transform, and matrices."
      "aims to provide an array object that is up to 50x faster than traditional Python lists.The array object in NumPy is called ndarray, "
      "it provides a lot of supporting functions that make working with ndarray very easy.")
import numpy as np

#Numpy Get Started
print("*********Numpy Get Started*************")
arr1= np.array([1])
print(arr1)

#Numpy Creating Arrays
arr2 =np.array([1,4,5,6,7])
print(arr2)

#Numpy Array Indexing
arr3 = np.array([1,4,5,6,7])
print("Indexing for 4 value is " , arr3[4])
#Numpy Array Slicing
arr4 = np.array([1,4,5,6,7])
print("Array Slicing for arr4", arr4[4:])

ar3= np.array([1,4,5,6,7])

print("Array Slicing for arr3 Reverse", ar3[::-1])

#Numpy Data Types
arr5= np.array([1,4,5,6,7])
print("Array datatype" , arr5.dtype)

#Numpy 1-D array
a= np.array([1])
print("1-D Array" , a.ndim)

a2 = np.array([[1,4,5,6,7], [3,4,5,6,7]])
print("2-D Array" , a2.ndim)

a3 = np.array([[[1,4,5,6,7], [3,4,5,6,7],[4,5,6,7,8]]])
print("3-D Array" , a3.ndim)

#Numpy changing the datatype of the array
arr6 = np.array([1,0,1])
newarr= arr6.astype(bool)
print("changing the datatype of the existing array", newarr)
print("After changing the datatype of the existing array", newarr.dtype)

#Numpy Dimension
arr = np.array([1, 4, 5, 6], ndmin=5)
print(arr)

#Numpy Reshape
arr2 = np.array([1, 4, 5, 6, 8])
arr2.reshape(1,5)
print(arr2)

#Numpy Copy -->Make a copy, change the original array, and display both arrays:
arr4= np.array([3,6,8,10])
arr6 = arr4.copy()
print(arr6)

#Make a view, change the original array, and display both arrays:
ar7 = np.array([[1,4,5,6,7], [3,4,5,6,7]])
x= ar7.view()
print(ar7)
print(x)

#Check if Array Owns its Data (base)
#As mentioned above, copies owns the data, and views does not own the data, but how can we check this?
ar7 = np.array([[1,4,5,6,7], [3,4,5,6,7]])
y =ar7.copy()
x= ar7.view()
print(y.base) #None
print(x.base) #[1,4,5,6,7], [3,4,5,6,7]

#iteration for the array
print("1D Array")
s= np.array([[1,4,5,6,7]])
for k in s:
    print(k)
print("2D Array")
arr = np.array([[1, 2, 3], [4, 5, 6]])

for x in arr:
  print(x)

print("3D Array")
arr = np.array([[[1, 2, 3], [4, 5, 6],[8,9,5]]])

for x in arr:
  for y in x:
    print(y)

arr = np.array(['a', 'b', 'c'])
for x in arr:
  print('Hello ' + x)

#Iterating Array With Different Data Types
#op_dtypes
#NumPy does not change the data type of the element in-place (where the element is in array)
# so it needs some other space to perform this action, that extra space is called buffer,
# and in order to enable it in nditer() we pass flags=['buffered'].
#np.nditer()
arr = np.array([1, 2, 3])
for x in np.nditer(arr, flags=['buffered'], op_dtypes=['S']):
    print(x)

#Iterating With Different Step Size
arr = np.array([[1, 2, 3, 4], [5, 6, 7, 8]])
for x in np.nditer(arr[:,::2]):  #skip 1 element
    print(x)
for x in np.nditer(arr[:,::3]):  #skip 1 element
    print(x)

#Enumerated Iteration Using ndenumerate()
arr = np.array([7,8,9])
for idx, x in ndenumerate(arr):
    print(idx, x)

#NumPy Joining Array
#joining two array in the single array
#concatenate() function, along with the axis. If axis is not explicitly passed, it is taken as 0.

arr = np.array([1,2,3,5])
arr2 = np.array([4,5,6,7])
#Join two arrays
final =np.concatenate((arr,arr2), axis=0)
print(final)

#2D array
arr= np.array([[1,2],[2,3]])
arr3 = np.array([[1,2],[4,5]])
final = np.concatenate((arr,arr3), axis=1)
print(final)


#Stacking Along Rows
#NumPy provides a helper function: horizontal stack() to stack along rows.

a= np.array([1,2,3])
b= np.array([8,5,6])
final = np.hstack((a,b)) #merging with hstack
print(final)

#Stacking Along Columns

#vstack vertical stack
a= np.array([1,2,3])
b= np.array([8,5,6])
final = np.vstack((a,b)) #merging with vstack
print(final)


#Splitting NumPy Arrays
#reverse operation of joining
a= np.array([1,2,3,5,6,7,9])
newarr= np.array_split(a,3)
print(newarr[0])

#NumPy Searching Arrays
#searching Array
#To search an array, use the where() method.

a= np.array([1,2,3,5,6,7,9])
search = np.where(a == 4)
print(search)

d= np.array(["ankit", "ashish", "xyz", "hello"])
search = np.where(d== "ashish")
print(search)

#Find the indexes where the values are even:
search = np.where(a%2 ==0 ) # where are values are even
print("where the value are even ", search)
search2= np.where( a%2 == 1)
print("Where the values are odd" , search2)

#Find the indexes where the value 7 should be inserted:
sorrted = np.array([1,2,3,5,6,7,9])
#inputdata = int(input("enter the digit"))
sortedarray =np.searchsorted(sorrted, 5)
print("seach and found ", sortedarray)

#Find the indexes where the value 7 should be inserted, starting from the right:
sorrted = np.array([1,2,3,5,6,7,9])
#inputdata = int(input("enter the digit"))
sortedarray =np.searchsorted(sorrted, 5, side = 'right')
print("seach and found ", sortedarray)


#Sorting Arrays
a= np.array([9,7,1,34,6,12])
asd= np.sort(a)
print(asd)

arr = np.array(['banana', 'cherry', 'apple'])

print(np.sort(arr))

arr = np.array([True, False, True])

print(np.sort(arr))

#2-D array
arr = np.array([[3, 2, 4], [5, 0, 1]])

print(np.sort(arr))


#NumPy Filter Array
#If the value at an index is True that element is contained in the filtered array, if the value at that index is False that element is excluded from the filtered array.
arr= np.array([1,2,5,6])
x = [True, False, True, False]
newarr = arr[x] # true place value should be filter 1, 5 are on true index
print(newarr)


#Creating the Filter Array
# if the data contain on the position it will take as true while not contain false
'''Creating the Filter Array'''
arr= np.array([40,56,12,54,1,6])
filterarray =[]
filter_arr= []
for k in arr:
    if k > 6:
        filterarray.append(True)
    else:
        filterarray.append(False)

for element in arr:
  # if the element is completely divisble by 2, set the value to True, otherwise False
  if element % 2 == 0:
    filter_arr.append(True)
  else:
    filter_arr.append(False)

newarr = arr[filter_arr]

print(filterarray)
newarr = arr[filterarray]
print("My filtered array list" , newarr)

print(filter_arr)
newarr2 = arr[filter_arr]
print("My filtered array list" , newarr2)

#Create a filter array that will return only even elements from the original array:
arr= np.array([40,56,12,54,1,6])
filterarray = arr%2 == 0
newarr = arr[filterarray]
print("My filtered array list 23" , newarr)