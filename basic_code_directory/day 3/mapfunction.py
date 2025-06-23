#map function
import functools

#lambda expression x:x**2
# Using generator expression (correctly parenthesized)
squares = list(map(lambda x: x ** 2,(z for z in range(10))))
print(squares)

#map function will apply on list for every element in the list / dic and set

#for list
#syntax [expression for item in iterable]
my_list = [ x * 2 for x in range(10)]
#print(list(map(lambda z : z+2, [k for k in my_list]))) line 12 and 13 is equal
print(list(map(lambda z: z + 2, my_list)))

#for dictionary
my_dict = {'a': 1, 'b': 2, 'c': 3}
my_dic = {key : key * 2 for key , value in my_dict.items()}
keys = my_dic.keys()
valuesdata = my_dic.values()
values = map(lambda v: v + 2, my_dict.values())
new_dict = dict(zip(keys, values))
print(f"{keys} : {new_dict} new_dict")
# expression : iterable items --> [expression for item in iterable]
#{k.upper(): v * 10 for k, v in my_dict.items()}


#for tuple
tupledata = (x**2 for x in range(10)) #expresion for iterable
print(tuple(map(lambda x : x*2 , tupledata))) # datatype map with lambda anonymous function expression , argument)

#"Define a higher-order function that takes two functions, a filter function and a map function,
# along with a list of integers. The higher-order function should first filter
# the integers using the filter function and then apply the map function to the filtered integers.
# Test with different filter and map functions.\n",
numbers = list(range(20))

# Filter: keep even numbers

def funct1_filter(numbers):
    return filter(lambda x: x % 2 == 0 , numbers)

def funct2_map(numbers):
    return (map(lambda y: y**2 , numbers ))

def highorderfunction(data, funct1_filter, funct2_map):
    filtered = funct1_filter(data)
    mapped = funct2_map(filtered)
    return list(mapped)
#return list(funct1_filter(funct2_map(data)))
#[0, 4, 16, 36, 64, 100, 144, 196, 256, 324]
#[0, 4, 16, 36, 64, 100, 144, 196, 256, 324]
print(highorderfunction(numbers, funct1_filter,funct2_map))

#CONCLUSION for DEFINE HIGH ORDER FUNCTION

'''📘 Definition:
A higher-order function (HOF) is a function that:
Takes one or more functions as arguments, OR
Returns another function as a result
it just a example for demonstrate
def function(sum , avg): 
        OR
def function(sum):
    return avg(sum) 
'''
''''🧠 Why Use It?
Higher-order functions are powerful because they allow you to:
1. Reuse logic
2. Abstract behavior
3. Create modular and clean code'''

#highorder function are those function which can take the functions as one or more arguement and return function as a result

# "Define a function that composes two functions,
# f and g, such that the result is f(g(x)).
# Test with different functions f and g.\n",

''''✅ Summary:
Feature	Explanation
Input as function	Passes another function as an argument
Output is function	Returns a function
Purpose	Abstraction and modular code'''

#step 1 define some functions for calling with take argument in function
def double(x):
    return x * 2
def sum(x):
    return x + 2
def power(x):
    return x ** 2
def decrement(x):
   return x - 1

#step 2 create a function to accept the function for output

def mycomposingfunction(funct1, funct2):
    return (lambda x: funct1(funct2(x)))

f1 = mycomposingfunction(sum, decrement)
f2= mycomposingfunction(power, decrement)
print(f1(5)) # 5+2 -1 -->6
print(f2(5)) # 5**2 - 1 -->24

print(power(5))

#"Use the functools.partial function to create a new function that multiplies its input by 2.
# Test the new function with different inputs.\n"

from functools import partial
# Normal multiplication function
def multiply(a, b):
    return a * b

result = partial(multiply, 2)

print(result(2))

'''''Let me know if you'd like to:
Partially apply more than one argument
Use this in a map/filter context
Use partial with class methods or lambdas'''


