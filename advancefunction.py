#Define a recursive function to calculate the nth Fibonacci number using memoization. Test the function with different inputs.
from datetime import time


def FuncationFact(num):
    if num ==0:
        return 1
    else :
        return num*FuncationFact(num-1)

print(FuncationFact(5))
print(FuncationFact(4))

#"Define a function that takes two arguments, a and b,
# where b is a dictionary with a default value of an empty dictionary. The function should add a
# new key-value pair to the dictionary and return it.
# Test the function with different inputs.\n",

def functionArg(a, b=None):
    if b is None:
        b ={}
    b[a] = a**2
    return b

print(functionArg(5))

#Define a function that takes a variable number of keyword arguments and returns a dictionary containing
# only those key-value pairs where the value is an integer.
# Test the function with different inputs.


def GetFunctionintonly(**kwargs):
    #expression : iteration condition {key : value}
    #key: value : for key, value in kwargs.items() iterate key and value from th kwargs items
    #if isinstance (value , int) value should be integer only then add
     return {key: value  for key, value in kwargs.items() if isinstance(value , int)}  # v is value k is key


print(GetFunctionintonly(a=12, b= 4.6 , c = True, d = "ankit"))



def PrintScore(**Kwargs):
        #return {key: value for key, value in Kwargs.items() if isinstance(value, int)}
        for key , value in Kwargs.items():
            if value > 0:
                  print(f"key {key} : {value}")

PrintScore(kohali= 0, rohit = 15, pant = 100, kLRahul = 200 )
print("\U0001F600")  # 😀
print("\U0001F603")  # 😃
print("\U0001F604")  # 😄
print("\U0001F60A")  # 😊

#Define a function that takes another function as a callback and a list of integers.
# The function should apply the callback to
# each integer in the list and return a new list with the results. Test with different callback functions.

def myfunction(callback , lst):
    return [callback(x) for x in lst]
#lambda expression , arguments
print(myfunction(lambda x: x**2 , [1,2,3,4,5]))


def namecall(callback , dic):
    return {key : callback(value)  for  key, value in dic.items() }

#callback takes value only syntax for dic is {key : callback(value) for key , value in dic.items()
print(namecall(lambda x: x + 2, {'a': 1, 'b': 2, 'c': 3}))


#"Define a function that returns another function.
# The returned function should take an integer and return its square.
# Test the returned function with different inputs.\n",

def firstfunction(anotherfunction):
    return anotherfunction
def anotherfunction(number):
    return number**2
print(firstfunction(anotherfunction(8)))

"""" Another way to same request code
def firstfunction():
    def anotherfunction(number):
             return number**2
    return anotherfunction

square =firstfunction()
print(square(8))
"""

#"Define a function that calculates the time taken to execute another function.
# Apply this decorator to a function that performs a complex calculation.
# Test the decorated function with different inputs.\n",

#step 1 define the decorator
import time
def timer(func):
    def wrapper(*args, **kwargs):
        start = time.time()
        result = func(*args, **kwargs)
        end = time.time()
        print(f"{func.__name__} took {end - start} seconds")
        return result
    return wrapper

# Step 2 & 3: Define and decorate a complex function
@timer
def complex_calculation(n):
    return [x ** 2 for x in n]

result = complex_calculation([2,4,6,8,10,12,14,16,18,20])
results = [f() for f in result]
print(results)

