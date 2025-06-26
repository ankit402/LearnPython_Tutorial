#"Create a base class named `Animal` and a derived class named `Cat`.
# Create objects of both classes and use the `isinstance` function to check the instance types.\n",

class Animal:
    def __init__(self):
        print("Animal")

class Cat(Animal):
    def __init__(self):
        super().__init__()
        print("Cat")

animal = Animal()
cat= Cat()
print(isinstance(animal, Cat))     # False
