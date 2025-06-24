# "Create an abstract base class named `Shape` with an abstract method `area`.
# Create derived classes `Circle` and `Square` that implement the `area` method.
# Create objects of the derived classes and call the `area` method.\n",
import math
'''ABC is the module for abstract'''
from abc import ABC, abstractmethod

class Shape(ABC): # Abstract class
    @abstractmethod
    def area(self):
        pass # Abstract method — no implementation

#subclass must implement the abstract method circle
class Circle(Shape):
    def __init__(self, radius):
        #constructor
        self._radius = radius # underscore to indicate "private"

    def area(self):
        print(f'Circle Area: {math.pi * self._radius ** 2}')
        return math.pi * self._radius ** 2

#subclass must implement the abstract method for square
class Square(Shape):
    def __init__(self, side):
        #constructor
        self._side = side # underscore to indicate "private"
    def area(self):
        print(f'square of side {self._side ** 2}')
        return self._side ** 2

print(f'************* Calculating Square Area *************')
sq=Square(4)
sq.area()
print(f'************* Calculating Circle Area *************')
cir=Circle(2)
cir.area()

#📌Definition for Abstract Class : this class can't be initiated on its own and designed to be
# a base class for other classes.
#define contract -- specifying the certain methods must be implemented by any subclasses.

#You use abstract classes
# when you want to enforce that all 🚫 child classes must override certain behavior.

'''What we can not perform with abstract class
🚫 Instantiating Abstract Classes:
Sh=Shape() # ❌ This will raise TypeError
📌 Why Use Abstract Classes?
Enforce a common interface across multiple classes
Prevent incomplete base classes from being used directly
Improve code structure, especially in large systems (e.g., for shapes, animals, vehicles, etc.)
'''
#📌Definition for Abstract Method
'''🔷 What is an Abstract Method in Python?
An abstract method is a method that is declared in an abstract class but 
contains no implementation. It acts as a 
placeholder — forcing any subclass to provide its own version of the method.'''

#questions

'''✅ Yes, abstract classes in Python support multiple inheritance.'''