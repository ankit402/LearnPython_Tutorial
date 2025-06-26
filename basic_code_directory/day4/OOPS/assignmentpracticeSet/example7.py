# "Create a class named `Flyer` with a method `fly` that prints a flying message.
# Create a class named `Swimmer` with a method `swim` that prints a swimming message.
# Create a derived class `Superhero` that inherits from both `Flyer` and `Swimmer`.
# Create an object of the `Superhero` class and call both methods.\n",

#base class
class Flyer:
    def fly(self):
        print (f'✅Flying started....')
#base class
class Swimmer:
    def swim(self):
        print(f'✅Swimming started....')
#multiple inheritance for concrete or derived class
class Superhero(Flyer, Swimmer):
    def __init__(self):
        # Flyer.fly(self)    #✅
        # Swimmer.swim(self) #✅
        super().fly()  #✅ Allowed for inheritance
        super().swim()  #❌ not allowed Flyer__init__(self) // Swimmer__init__(self)
q=Superhero()
print(Superhero.__mro__)
