''''Filter function filter()
filter function construct an iterator from elements of an iterable for which a function which return true
it is used to filter out items from the list (or any other iterable based on the condition'''

def even(num):
    if num % 2 == 0:
        return True
    else:
        return False

#syntax for filter function
print(list(filter(even , [x for x in range(5)])))

''''Class function 
function : (T_function),
arguement : (T_iterable)
'''

#filter with lambda function
#syntax the function is define as lambda which is anonymous and applies on the list
''''Class function 
function : (T_function)  --> lambda arguement : expression,
arguement : (T_iterable)
'''
print(f"Calling with lambda function {list(filter(lambda x : x%2==0 , (x for x in range(5))))}")

numbers = [1,2,3,4,5,6,7,8,9,10]
print(list(filter(lambda x : x>5 , numbers)))

#filter multiple condition
numbers = [1,2,3,4,5,6,7,8,9,10]
print(list(filter(lambda x : x>5 and x%2==0 and x%3==0 and x%1==0, numbers  )))

#filter if the age is greater than by 25 in dictionary

dicdata =[
    { 'name' : 'ankit', 'age' : 33},
    { 'name' : 'ashish', 'age' : 40},
    { 'name' : 'xyz', 'age' : 24},
    { 'name' : 'abc', 'age' : 26},
]

def age_greaterthan25(dicdata):
    return dicdata['age'] >= 25

print(list(filter(age_greaterthan25, dicdata)))

#using lambda function Anonymous function can write condition here
print(list(filter(lambda x : x['age']>=25, dicdata)))

print(list(filter(lambda x : x['name'].startswith('a') and x['name'].endswith('t'), dicdata)))

#✅ 1. map() – Apply a function to each element

#numbers = [x for x in range(4)]
print(list(map(lambda x:x+2, (x for x in range(4)))))

#✅ 2. filter() – Keep elements that return True

print(list(filter(lambda x: x<2, (x for x in range(4)))))

#✅ 3. sorted() – Custom sort key

fruits= [{
    "fruit1" : "apple",
    "fruit2" : "banana",
    "fruit3" : "orange",
}]

print(list(sorted(fruits , key=lambda x: len(x) , reverse=False)))

#✅ 4. reduce() – Cumulative function (needs functools)

from functools import reduce
numbers = [1, 2, 3, 4]
print(int(reduce(lambda x, y: x * y, numbers)))

#✅ 5. Conditional Logic in Lambda

check_even = lambda x: "Even" if x % 2 == 0 else "Odd"
print(check_even(5))  # Odd
print(check_even(8))

#✅ 6. With Dictionaries – Filter by key or value

test = [
    { 'name' : 'ankit','age' : 33 },
    { 'name' : 'xyz','age' : 38 },
]

print(list(filter(lambda x : x['age']>=25 and  x['name'].startswith('a'), test)))



def sum_list(numbers):

    return (lambda nums: sum(nums))(numbers)

numbers =[]
print(0 if not numbers else sum_list(numbers))

numbers = [1, 2, 3, 4, 5]
print(sum_list(numbers))

numbers = [10, -5, 7, 8, -2]
print(sum_list(numbers))


list =[]
list.append([1,2,3,4,5])

lst = [1, 1, 1, 1, 1]
setdata = set(lst)
unique_list = []
for x in setdata:
    unique_list.append(x)


print(unique_list)





