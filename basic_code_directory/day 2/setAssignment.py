#"Create a set with the first 10 positive integers. Print the set.\n",

sec_data ={1,2,3,4,6}
sec_data.add(11)
#sec_data.remove(111)
sec_data.discard(1)
print(sec_data)

# "Create two sets: one with the first 5 positive integers and another with the first 5 even integers.
# Perform and print the results of union, intersection, difference, and symmetric difference operations on these sets.\n",

set_1 = {x for x in range(1,5)}
set_2 = {x for x in range(1,6) if(x%2==0)}
print(f"Set 1: {set_1} | Set 2: {set_2}")
#union result
union_set = set.union(set_1, set_2)
print(f"Union set: {union_set}") #combination of the set result showing
#Intersection
intersection_set = set.intersection(set_1, set_2)
print(f"Intersection: {intersection_set}") #common present in both set showing
#difference
diffenence_set = set.difference(set_1, set_2)
print(f"Difference: {diffenence_set}") # not present in set2 showing difference

#"Create a new set containing the squares of the first 10 positive integers using a set comprehension.
# Print the new set.\n",

set_data = {x**2 for x in range(1,11)}
sorted_data = sorted(set_data)
print(f"Set data: {sorted_data}")

# "Create a set with duplicate elements and remove the duplicates using set methods. Print the modified set.\n",

set_data = {1,1,1,1,2,3,3,2}
print(f"Set data: {set(set_data)}")

#"Create two sets: one with the first 5 positive integers and another with the first 3 positive integers. Check if the second set is a subset of the first set and if the first set is a superset of the second set. Print the results.\n",

set_data = {x for x in range(5)}
set_data2 = {y for y in range(3)}
if(set_data2.issubset(set_data)):
    print("Set subset of data")
if(set_data.issuperset(set_data2)):
    print("Set superset of data")

#frozenset
set = frozenset(set_data)
print(f"Set frozenset: {set}")

#"Create a set with the first 5 positive integers. Convert it to a list, append the number 6,
# and convert it back to a set. Print the resulting set.\n",

set_data3 = {x for x in range(5)}
list_Data1 = list(set_data3)
list_Data1.append(6)
set_data2 = frozenset(list_Data1)  # => {0, 1, 2, 3, 4, 6}
print(f"Set data: {set_data2}")

#Create a set and iterate over the elements, printing each element.\n",

set_2 = {x for x in range(1,5)}
for x in set_2:
    print(x)

# "Create a set and remove elements from it until it is empty. Print the set after each removal.\n",


set_2 = {x for x in range(1,5)}
for x in set_2.copy(): #shallow copy
    set_2.discard(x)
print(f"Set 2: {set_2}")

set_2 = {x for x in range(1,5)}
print(f"Set 2: {set_2}")
set_2_copy = set_2.copy()
set_2_copy.add(11)
print(f"Set 2 copy: {set_2_copy}")

#"Create two sets and update the first set with the
# symmetric difference of the two sets. Print the modified first set.\n",

set_ = {x for x in range(1,5)}
set_2 = {x for x in range(1,5)}
set_.add(12)
diff = set.symmetric_difference(set_)
print(f"symmetric_difference {diff}")

#"Create a set and test if certain elements are present in the set. Print the results.\n",
set_ = {x for x in range(1,5)}
# Test if certain elements are in the set
print("Is 1 in the set?", 1 in set_)
print("Is 2 in the set?", 2 in set_)
print("Is 50 in the set?", 50 in set_)