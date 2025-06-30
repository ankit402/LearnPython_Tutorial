#Create a class named `Flyer` with a method `fly`.
# Create a class named `Swimmer` with a method `swim`.
# Create a class named `Superhero` that inherits from both `Flyer` and `Swimmer`
# and overrides both methods. Create an object of the `Superhero`
# class and call both methods.\n",

'''Polymorphism with Multiple Inheritance'''

class Flyer:
    def fly(self):
        print("Flyer initialized")
class Swimmer:
    def  swim(self):
        print("Swimmer initialized")
class Superhero(Flyer,Swimmer):
    # Flyer().__init__()
    # Swimmer().__init__()
    #No, Flyer().__init__() and Swimmer().__init__() are not required for
    # inheritance in Python unless the base classes define
    # their own __init__() constructors that need to be called.
    def fly(self):
        return "Superman can fly if required"
    def swim(self):
        return "Superman can swim if needed"

q=Superhero()
print(q.fly())
print(q.swim())
