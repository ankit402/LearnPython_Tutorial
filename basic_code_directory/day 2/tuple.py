#"Create a set containing tuples, where each tuple contains two elements. Print the set."

set_data = {(1, "hello"), (2, 4), (9,0)}
print(f"set of tuples: {set_data}")

# "Create a tuple with the first 10 positive integers. Print the tuple.\n",
#tuple keyword need to specify
tuple_data = tuple(x for x in range(1,20))
print(f"Original tuple: {tuple_data}")

#"Print the first, middle, and last elements of the tuple created in Assignment 1.\n",

print(f"tuple first element: {tuple_data[0]}")
print(f"tuple last element: {tuple_data[-1]}")
print(f"Middle element {tuple_data[len(tuple_data)//2-1]}")


#Print the first three elements, the last three elements, and the elements from index 2 to 5 of the tuple created in Assignment 1.\n",

print(f"tuple first element: {tuple_data[0:3:]}")
print(f"tuple first element: {tuple_data[-3:]}")
print(f"tuple middle element: {len(tuple_data)//2-1}")

# "Concatenate two tuples: (1, 2, 3) and (4, 5, 6). Print the resulting tuple.\n",

tuple1 = (1, 2, 3)
tuple2 = (4, 5, 6)
tuple3 = tuple1 + tuple2
print(f"Original tuple1: {tuple3}")

# "Create a nested tuple representing a 3x3
# matrix and print the matrix. Access and print the element at the second row and third column.\n",
#matrix and print the matrix. Access and print the element at the first row and second column.\n",
# Assuming matrix is defined as:
matrix = (
    (1, 2, 3),
    (4, 5, 6),
    (7, 8, 9)
)
for row in matrix:
    print(row)

# Access element at second row (index 1), third column (index 2)
element = matrix[1][2]

element2 = matrix[0][1]
print(element)
print(element2)


# "Create a tuple with duplicate elements and count the occurrences of an element.
# Find the index of the first occurrence of an element in the tuple.\n",

my_tuple = (1,2,2,3,3,3,4,4,4,4,5,5,5,5,5)
# Element to check
element = 2

# Count occurrences of the element
count = my_tuple.count(element)

# Find index of the first occurrence of the element
first_index = my_tuple.index(element)

# Print results
print(f"Tuple: {my_tuple}")
print(f"Occurrences of {element}: {count}")
print(f"First occurrence of {element} is at index: {first_index}")

"Create a tuple with 5 elements and unpack it into 5 variables. Print the variables.\n",
my_tuple = (x for x in range(1,6))
a,b,c,d,e = my_tuple
print(a,b,c,d,e)

#"Convert a list of the first 5 positive integers to a tuple. Print the tuple.\n",

list = [x for x in range(1,6)]
tuple_list = tuple(list)
print(tuple_list)

# "Create a tuple containing 3 tuples, each with 3 elements. Print the tuple of tuples.\n",

tupledata= ((1,2,3), ("hello", "hey", "bye"), (True, False, 0))
# Print the tuple of tuples
print("Tuple of tuples:")
for item in tupledata:
    print(item)

#"Create a tuple with the characters of a string. Join the tuple elements into a single string. Print the string.\n",
strdata =""
tuple =("h", "e" , "l","l" ,"o")
join_string = ''.join(tuple)
print(f"python function: {join_string}")
for item in tuple:
    strdata += item
print(f"Ordinary method: {strdata}")


#"Create a dictionary with tuple keys and integer values. Print the dictionary.\n",

dictionary_data = { (1,2) : 3, (3,2) : 4}
print(dictionary_data)

# "Create a nested tuple and iterate over the elements, printing each element.\n",
tupledata = ((1,2), (3,2), (5,6))
#nested_tuple =[x for sub_tuple in tupledata for x in sub_tuple]
for subtuple in tupledata:
    for item in subtuple:
        print(item, end=" ") # 1 2  newline
    print() #for changing line

#"Create a tuple with duplicate elements. Convert it to a set to remove duplicates and print the resulting set.\n",

tupledata = (1,2,2,3,4,5,6,6,6)
setdata = set(tupledata)
print(setdata)

#"Write functions that take a tuple and return the minimum, maximum, and sum of the elements. Print the results for a sample tuple."

def functiontupleMinMax(tupledata, flag):
        if flag == "Min":
            return min(tupledata)
        if flag == "Max":
            return max(tupledata)
        if flag == "Sum":
            return sum(tupledata)

print(functiontupleMinMax(tupledata, "Min"))
print(functiontupleMinMax(tupledata, "Max"))
print(functiontupleMinMax(tupledata, "Sum"))