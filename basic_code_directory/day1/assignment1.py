#Question 1 : Write a Python program that takes a user input and prints it.from day1.assignment_solution.assignment_solution import fahrenheit

n= input("enter the number")
print(n)

#Question 2 : Write a Python program to check if a number is positive, negative, or zero.

number = int(n)
if(number > 0):
    print(f"{number} is positive")
elif(number < 0):
    print(f"{number} is negative")
else:
    print(f"{number} is zero")

#Question 3: Write a Python program to find the largest of three numbers.

a,b,c = 23, 45, 40
if(a>b and a>c):
    print(f"{a} is greater than {b} and greater than {c}")
elif(b>a and b>c):
    print(f"{b} is greater than {a} and greater than {c}")
else:
    print(f"{c} is greater than {b} and greater than {a}")

#Question 4: Write a Python program to calculate the factorial of a number.
num = 6
def myfunction(num):
    if(num ==0):  #!0 is 1
        return 1
    else:
        return num*myfunction(num-1) # !n * !n-1

print(myfunction(num))


#Question 5: Create variables of different data types: integer, float, string, and boolean. Print their values and types.

a , b, c, d  = 12, 23.4 , "hello" , True
print(f"values is {a} and datatype is {type(a)}")
print(f"values is {b} and datatype is {type(b)}")
print(f"values is {c} and datatype is {type(c)}")
print(f"values is {d} and datatype is {type(d)}")

#Question 6: Write a Python program to swap the values of two variables.

a, b = 12 ,23
print(f"Before Swapped number now {a} : {b}")
temp = a
a= b
b =temp
print(f"After Swapped number now {a} : {b}")


#Question 7 : Write a Python program to convert Celsius to Fahrenheit.

Celsius = 34
Fahrenheit = Celsius * 9/5 + 32
print(f"Celsius to Fahrenheit {Fahrenheit}")

#Question 8 : Write a Python program to concatenate two strings.
a , b= "hello" , "world"
print(a+b)


#Write a Python program to check if a variable is of a specific data type.

def SpecifiedDatatype(data):
    print(f"{data} is {type(data)}")


print(SpecifiedDatatype("Hello"))

print(SpecifiedDatatype(1))

#Question Write a Python program to perform arithmetic operations: addition, subtraction, multiplication, and division.
a= 1+2
b = 3-3
c = 4* 5
d = 10/5
print(a,b,c,d)

#Write a Python program to demonstrate comparison operators: equal to, not equal to, greater than, less than.

def GetComparison(x,y):
    if(x>y):
        return "Greater than"
    elif(x<y):
        return "Less than"
    else:
        return "Equal"

print(GetComparison(10,20))
print(GetComparison(20,20))
print(GetComparison(120,20))


#Question Write a Python program to demonstrate logical operators: and, or, not.
x = True
y = False
def myfunction(x,y):
    if(x and y):
        return True
    elif(x or y):
        return False

print(myfunction(x,y))


#Write a Python program to calculate the square of a number.

num = 5
temp = [num**2]
print(temp)

#Write a Python program to check if a number is even or odd.

num = 8
def myfunction(num):
    if (num > 0):
        if (num % 2 == 0):
            return "Even"
        else:
            return "Odd"
    elif(num==0):
        return "invalid number"
print(myfunction(num))

#Write a Python program to find the sum of the first n natural numbers.

num = 10
def mynauturalno(num):
    return int(num* (num-1)/2)
print(mynauturalno(int(num)))

#Write a Python program to check if a year is a leap year

year = int(input("Enter the year"))
def checkleap(year):
    if(year % 4 == 0):
        if(year % 100 == 0):
            if(year % 400 == 0):
                print("leap year")
            else:
                print("Not leap year")
        else:
            print("Leap year")
    else:
        print("Not leap year")

print(checkleap(year))

#Write a Python program to reverse a string
#it is not required to put the list data it is assuming str also in the slicing
str = "hello"

print(str[::-1])


#Write a Python program to check if a string is a palindrome.

num = "10001"
print(num[::-1])


#Write a Python program to sort a list of numbers in ascending order.

lst = [20, 12, 4, 23, 21, 32, 11]
lst.sort()
print(lst)

