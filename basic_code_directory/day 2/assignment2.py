#Create a list of the first 20 positive integers. Print the list.
import random

lst = [20, 12, 4, 23, 21, 32, 11]
print(lst)

#Print the first, middle, and last elements of the list created in Assignment

print(f"First element: {lst[0]}")

lstlen = len(lst)//2
print(f"Middle element: {lst[lstlen]}")
print(f"Last element: {lst[-1]}")

#Print the first five elements, the last five elements, and the elements from index 5 to 15 of the list created in Assignment 1

print(lst[:5])
print(lst[:-5])
print(lst[5:16])

#   "Create a new list containing the squares of the first 10 positive integers using a list comprehension. Print the new list.\n"

squarlist = [x**2 for x in range(1,11) if(x!=0)]
print(squarlist)

#Create a new list containing only the even numbers from the list created in Assignment 1 using a list comprehension. Print the new list.\n",


#basic syntax [expression for item in iterable [expression for item in iterable if condition]
evennumberlist = [x for x in squarlist if(x%2==0)]
print(evennumberlist)

#"Create a list of random numbers and sort it in ascending and descending order. Remove the duplicates from the list and print the modified list.\n",

lst = [x for x in range(10) if x != random.randint(0, 10)]
lst.sort()
print(lst)
lst.reverse()
print(lst)

# "Create a nested list representing a 3x3 matrix and print the matrix. Access and print the element at the second row and third column.\n",

#Nested list Comprehension [expression for item1 in iterable for item2 in iterable2

list_nested = [[x,y] for x in range(10) for y in range(10)]
print(list_nested)

#list comprehension with function call

word = ["hello", "world", "python" , "list", "comprehension"]
length = [len(word) for word in word]
print(length)
length.sort()
data = set(length)
d=sorted(data)
print(d)

#"Create a list of dictionaries where each dictionary represents a student with keys 'name' and 'score'.
# Sort the list of dictionaries by the 'score' in descending order and print the sorted list.\n",

dic_student= [{
    "name":"a",
    "score":200
},{
    "name":"b",
    "score":100},
{
    "name":"c",
    "score":300}]

sorted_student = sorted(dic_student, key=lambda student: student["score"], reverse=False)

print(sorted_student)

# "Write a function that takes a 3x3 matrix (nested list) as input and returns its transpose. Print the original and transposed matrices.\n",
original_matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]
print(f"original_matrix")
for row in original_matrix:
    print(row)
"Transpose matrix [x][y] => [y][x]"
transponse_matrix = [[original_matrix[y][x] for y in range(3)] for x in range(3)]
print(f"transponse_matrix")
for row in transponse_matrix:
    print(row)


#"Write a function that rotates a list by n positions. Print the original and rotated lists.\n",
#Rotate List
list = [ x for x in range(10)]
print(list[::-1])

#Reverse list
#lst[-n:] + lst[:-n] slicing is used for changing the sequence of the list items
list = [x for x in range(1,8)]
print(f"Original list: {list}")
rotateby=-1
rotated_list = lst[-rotateby:] + lst[:-rotateby]
print(f"Right rotated list: {rotated_list}")
rotated_list = lst[rotateby:] + lst[:rotateby]
print(f"Left rotated list: {rotated_list}")

list= [x for x in range(1,8)]

print(f"Original list  {list}")
def Reverse_fucntion(list, n):
    return list[n:] + list[:n]

new= int(input("Enter the number"))
print(f"Rotated list  {Reverse_fucntion(list,new)}")

#"Write a function that takes a nested list and flattens it into a single list. Print the original and flattened lists."

nested_list = [
       [1, 2, 3],
       [4, 5, 6],
       [7, 8, 9],]

print(f"Nested list: {nested_list}")

#[expression for item in iterable condition if any]
#flat_list = [item for sublist in nested_list for item in sublist]

#[1 , [1, [1,2,3], 4], 5]
lst1 =[1 , [1, [1,2,3], 4], 5]
lst2=[]
for sublist in nested_list:
    for flat_list in sublist:
            lst1.append(flat_list)
print(f"Flatternlist {flat_list}")


# "Create a list of the first 10 positive integers.
# Remove the elements at indices 2, 4, and 6, and insert the element '99' at index 5. Print the modified list."

list_no = [item for item in range(1,10)]

print(list_no)
del list_no[2]
del list_no[4]
del list_no[6]
list_no.insert(5,99)
print(list_no)

#list_no[5] = 99

#  "Write a function that takes two lists and returns a new list containing only the elements that are present in both lists. Print the intersected list."
list1 = [1, 2, 3, 4, 5]
list2 = [3, 4, 5, 6, 7]
list1= [x for x in list1 if x in list2]  # if common value found
print(list1)



