#    "Create an abstract base class named `Vehicle` with an abstract method `start_engine`.
#    Create derived classes `Car` and `Bike` that implement the `start_engine` method.
#    Create objects of the derived classes and call the `start_engine` method.\n",
from abc import ABC, abstractmethod


class Vehicle(ABC):
    #abstract method
    @abstractmethod
    def start_engine(self):
        pass
    def fuel_type(self):
        return "Generic fuel"
#derive class
class Car(Vehicle):
    def start_engine(self):
        print("Car engine started with a key.")
    def fuel_type(self):
        print("Car Engine fuel type petrol or diesel")
#derive class
class Bike(Vehicle):
    def start_engine(self):
        print("Bike engine started with a kick.")
    def fuel_type(self):
        print("Bike Engine fuel type petrol")

car = Car()
bike = Bike()
car.start_engine()
bike.start_engine()
car.fuel_type()
bike.fuel_type()

#"In the `Vehicle` class, add a concrete method `fuel_type` that returns a generic fuel type.
# Override this method in `Car` and `Bike` classes to return specific fuel types.
# Create objects of the derived classes and call the `fuel_type` method.\n",

car.fuel_type()
bike.fuel_type()


