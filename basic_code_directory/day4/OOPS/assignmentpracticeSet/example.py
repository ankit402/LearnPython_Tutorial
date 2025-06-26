# "Create a base class named `Animal` with attributes `name` and `species`.
# Create a derived class named `Dog` that inherits from `Animal` and adds an attribute
# `breed`. Create an object of the `Dog` class and print its attributes.\n",
#question 1
#base calss
class Animal:
    def __init__(self, name, species):
        self.name = name
        self.species = species

#derived class
class Dog(Animal):
    def __init__(self, name, species, breed):
        super().__init__(name, species)
        self.breed = breed

    #question 2
    def __str__(self):
        return f"{self.name} dog having this {self.breed} breed"

    #question 3
    def bark(self):
        return f"Dog says woof woof"

#use case
d1= Dog('lucy','Canis lupus familiaris', 'Labrador Retriever.')
print(d1.breed)

#Note : using dunder method we are overloading the __str__ method --> called magic method

# "In the `Dog` class, override the `__str__` method to return a
# string representation of the object.
# Create an object of the class and print it.\n",
print(d1)

# "In the `Dog` class, add a method named `bark` that prints a barking sound.
# Create an object of the class and call the method.\n",
print(d1.bark())

#