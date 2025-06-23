my_list = [1,2,3,4,5,6,7,8,9]
my_list.insert(1,10)
print(my_list)

my_list.pop()
print(my_list)
n = my_list.pop()
print(f"Popped {n}")

index = my_list.index(5)

print(f"index is {index}")
print(my_list)

my_list.sort()
my_list.reverse()
print(my_list)

print([x**2 for x in range(10)])

lst1= [1,2,3,4,5,6,7,8,9]
lst2= ['a','b','c','d','e','f']

pair = [ [lst1,lst2]  for i in lst1 for j in lst2]

print(pair)

words = ["hello", "this" , "is" , "my" , "python", "program"]

#expression for item in iterable
length = [len(word) for word in words]

print(length)

