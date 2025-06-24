# "Create a class named `Car` with attributes `make`, `model`,
# and `year`. Create an object of the class and print its attributes.\n",
import math


# class Car:
#     def __init__(self, make, model, year):
#         self.make = make
#         self.model = model
#         self.year = year
#
# car1= Car("Chevrolet", "GMC" , 2024)
# print(car1.make)
# print(car1.model)
# print(car1.year)

# "Add a method named `start_engine` to the `Car` class that prints a message
# when the engine starts.
# Create an object of the class and call the method.\n",

#"Create a class named `Student` with attributes `name` and `age`.
# Use a constructor to initialize these attributes.
# Create an object of the class and print its attributes.\n",

# class Student():
#     # constructor
#     def __init__(self, name, age):
#
#         self.name = name
#         self.age = age
#
# stu= Student("ankit", 32)
# print(stu.name)

#"Create a class named `BankAccount` with private attributes `account_number` and `balance`.
# Add methods to deposit and withdraw money, and to check the balance.
# Create an object of the class and perform some operations.\n",

# class BankAccount:
#     def __init__(self, account_number, balance):
#         self.account_number = account_number
#         self.balance = balance
#
#     def deposit(self, amount):
#         self.balance += amount
#         print(f'Deposit amount: {amount}')
#     def withdraw(self, amount):
#         if amount > self.balance:
#             print(f'Insufficient balance: {self.balance}')
#         else:
#             self.balance -= amount
#             print(f'Withdraw amount: {amount}')
#     def balance_check(self):
#         if self.balance < 0:
#             print('Insufficient balance')
#         else:
#             print(f'Balance: {self.balance}')
#
#
# bank1=BankAccount("012345343", 1000)
# bank1.balance_check()


# "Create a base class named `Person` with attributes `name` and `age`.
# Create a derived class named `Employee` that inherits from `Person` and adds an attribute
# `employee_id`.
# Create an object of the derived class and print its attributes.\n",


class Person:
    def __init__(self,name, age):
        self.name = name
        self.age = age

class Employee(Person):
    def __init__(self,name, age, employee_id):
         super().__init__(name, age)# Call Person's constructor correctly
         self.employee_id = employee_id  # Store employee_id separately
         print(f'Employee {self.name} created')

'''The purpose of calling __str__() in Python is to get a readable string
 representation of an object. It is automatically used when you call print(object)
  or str(object).'''
def __str__(self):
        return f"Employee(Name: {self.name}, Age: {self.age}, ID: {self.employee_id})"
p1=Employee("John", 25, "012345343")
p2=Employee("test", 26, "32435647467")

#    "In the `Employee` class, override the `__str__`
#    method to return a string representation of the object.
#    Create an object of the class and print it.\n",

# "Create a class named `Address` with attributes `street`, `city`, and `zipcode`.
# Create a class named `Person` that has an `Address` object as an attribute.
# Create an object of the `Person` class and print its address.\n",

class Address:
    def __init__(self,street,city,state,zipcode):
        self.street = street
        self.city = city
        self.state = state
        self.zipcode = zipcode

class Person(Address):
    def __init__(self,street,city,state,zipcode):
        super().__init__(street,city,state,zipcode)
        print(f'Person Address {street} {city} {state} {zipcode}')


a1=Person("A","B","C","D")


#   "Create a class named `Counter` with a class variable `count`.
#   Each time an object is created, increment the count.
#   Add a method to get the current count.
#   Create multiple objects and print the count.\n",

class Counter:
    def __init__(self,count=0):
        self.count = count

    def Increament(self,count=1):
        self.count += count

    def getcount(self):
        print(f'Current Count {self.count}')

    def reset(self):
        self.count = 0
        print('Counter reset to 0')
c = Counter(5)
c.getcount()       # Output: Current Count: 5

c.Increament()      # Output: Incremented by 1
c.getcount()       # Output: Current Count: 6

c.Increament(4)     # Output: Incremented by 4
c.getcount()       # Output: Current Count: 10

c.reset()          # Output: Counter reset to 0
c.getcount()       # Output: Current Count: 0

#"Create a class named `MathOperations` with a static method to calculate
# the square root of a number.
# Call the static method without creating an object.\n",

class MathOperations:
    '''Why @staticmethod?
It lets you call the method directly using the class name.

It doesn't require self or cls, because it doesn’t depend on instance or class variables.

Let me know if you want to add more operations like power, log, or factorial!'''
    @staticmethod
    def squar_root(number):
        return math.sqrt(number)
result = MathOperations.squar_root(5)
print(f'Square root of the  result is {result}')

# "Create a class named `Rectangle` with private attributes `length` and `width`.
# Use properties to get and set these attributes.
# Create an object of the class and test the properties.\n",

class Rectangle:
    def __init__(self, length, width):
        self._length = length # underscore to indicate "private"
        self._width = width # underscore to indicate "private"

    #getter
    @property
    def length(self):
        return self._length# underscore to indicate "private"

    #setter
    @length.setter
    def length(self, value):
        if value: # simple validation
            self._length = value# underscore to indicate "private"
        else:
            return ValueError("Length cannot be None")
    #getter
    @property
    def width(self):
        return self._width# underscore to indicate "private"

    #setter
    @width.setter
    def width(self, value):
        if value:# simple validation
            self._width = value# underscore to indicate "private"
        else:
            return ValueError("Width cannot be None")

p =Rectangle(12,12)
p.width=12
p.height=12
print(f'rectangle {p.width},{p.height}')



