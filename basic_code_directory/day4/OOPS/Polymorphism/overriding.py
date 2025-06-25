'''method overriding allows a child class to provide a specific
implementation of the method which is already define in the parent clas'''

class Animal:
    def speak(self):
        return "sound of the animal"

class Dog(Animal):
    def speak(self):
        return "woof"

class Cat(Animal):
    def speak(self):
        return "meow"

# function demostrate polymorphism
def animal_sound(animal):
    print (f'{animal.speak()}')

c1=animal_sound(Cat())
c2=animal_sound(Dog())
