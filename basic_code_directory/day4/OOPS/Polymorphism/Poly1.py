# "Create a base class named `Shape` with a method `area`.
# Create two derived classes `Circle` and `Square` that override the `area` method.
# Create a list of `Shape` objects and call the `area` method on each object to demonstrate polymorphism.\n",

'''# Assignment 1: Polymorphism with Methods\n",'''
from abc import abstractmethod


class Shape:
    def area(self):
        pass

class Circle(Shape):
    def __init__(self, radius):
        super().__init__()
        self.radius = radius
    def area(self):
        return  3.14159 * self.radius * self.radius

class Square(Shape):
    def __init__(self, side):
        super().__init__()
        self.side = side
    def area(self):
        return self.side * self.side

s1=Circle(2)
print(s1.area())

s2=Square(3)
print(s2.area())


#Yes! ✅ Your code is a perfect demonstration of polymorphism in object-oriented programming.