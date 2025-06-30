# "Create a function named `describe_shape` that takes a `Shape` object as an argument and
# calls its `area` method.
# Create objects of `Circle` and `Square` classes and pass them to the `describe_shape` function.\n",
from abc import ABC, abstractmethod


class Shape:
    def area(self):
        pass

    def describe_shape(self):
        print("Shape description")

class Circle(Shape):
    def __init__(self, radius):
        super().__init__()
        self.radius = radius
    def area(self):
        return  3.14159 * self.radius * self.radius
    def describe_shape(self):
        print("Circle description")


class Square(Shape):
    def __init__(self, side):
        super().__init__()
        self.side = side
    def area(self):
        return self.side * self.side

s1=Circle(2)
s1.describe_shape()

#Yes! ✅ Your code is a perfect demonstration of polymorphism in object-oriented programming.
#"Create an abstract base class named `Vehicle` with an abstract method `start_engine`.
# Create derived classes `Car` and `Bike` that implement the `start_engine` method.
# Create objects of the derived classes and call the `start_engine` method.\n",

class Vehicle(ABC):
    @abstractmethod
    def start_engine(self):
        pass
