#allows us to modify the behavior of a function or class method
#they are commonly used to add functionality to functions or methods without modifying their existing code

#function_copy
def my_function():
    return "my function is called"

myfunction_copy=my_function
print(myfunction_copy())
del my_function

#closure method is method within the method

def welcome_greeting(msg):
    print("Greeting from welcome greeting")
    def sub_weclome_method():
        print("Welcome from submain method")
    return sub_weclome_method()

welcome_greeting('hello world')


def getlength(func, list):
    print("calculate length")
    def calc_length():
        print(func(list))
    return calc_length()

listdata = [1,2,3,5]
getlength(len,[listdata])