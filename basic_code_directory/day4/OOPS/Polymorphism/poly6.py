# "Create a base class named `Animal` with a method `speak`.
# Create two derived classes `Dog` and `Cat` that override the `speak` method.
# Create a list of `Animal` objects and call the `speak` method on each object to demonstrate
# polymorphism.\n",
'''Polymorphism with Inheritance'''

class Animal:
    def speak(self):
        print("animal sound")
class Dog(Animal):
    def speak(self):
        print("dog says woof")
class Cat(Animal):
    def speak(self):
        print("cat is meow")

#classes demostrate in the list

animals= [Dog() , Cat()]

for animal in animals:
    animal.speak()





