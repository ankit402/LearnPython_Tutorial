# can we pass function as an argument in python ?

# def add(a,b):
#     return a+b
#
# def apply_func(func, a,b):
#     return func(a,b)
#
# #The add function is passed as an argument to apply_func, which applies it to 3 and 5.
# print(apply_func(add(3,4)))


'''A higher-order function (HOF) is a function that does one or both of these:

Takes another function as an argument, or

Returns a function as a result

In simple words:

A higher-order function works with functions just like normal values.
'''
#
# def greet(name):
#     return f'Hello, {name}!'
#
# def highorderfunction(func, args):  #higher-order function
#     return func(args)
#
# print(highorderfunction(greet, 'ankit'))
#
#
# #Real time highorder function
#
# list = [1,2,3,4,5]
#
# input = list(map(lambda x : x *2 , list))
#
# #lambda arguments: expression
#
#
# #kwargs
#
# def printscore(**kwargs):   # dictionary
#     for key , value in kwargs.items():
#         if key >0:
#             print(f'{key}: {value}')
#
# def mypositional(*args):  #tuple
#     print(args)
#
#
# result = list(filter(lambda x: x * 2 , range(10)))
# #range(10) 0 1,2,3,4,5,6,7,8,9
# # syntax lambda expression
# print(result)

def is_even(num):
    if num > 0:
        return num % 2 == 0
    else:
        return 0

result2 = list(is_even(i) for i in range(5) if i != 0)
#[(lambda x: x * x)(n) for n in range(1,6) condition]
print(result2)

x ="ankitpandey"

result = lambda x : x.upper()

print(result(x))

x = 3
test = [
    { 'name' : 'ankit','age' : 33 },
    { 'name' : 'xyz','age' : 38 },
]

print(list(filter(lambda x : x['age']>=25 and  x['name'].startswith('a'), test)))


def fun(*args):
    for arg in args:
        print(arg)

fun("hello", "Are", "you", "good")


def func2(**kwargs):
    for key, value in kwargs.items():
        print("%s == %s" % (key, value))

func2(name ="ankit", age = 23, gender = 'male')


