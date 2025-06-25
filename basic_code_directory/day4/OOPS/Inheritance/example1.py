'''Multiple inheritance achieved here'''

# base class 1
class Animal:
    def __init__(self,name):
        self._name = name

    # default parent speak
    def speak(self):
        pass
# base class 2
class Pet:
    def __init__(self,owner):
        self.owner = owner

#derived class
class Dog(Animal):
    def __init__(self,name, owner):
        #super().__init__(name) in case if we have only one parent class for inherit
        Animal.__init__(self,name)
        Pet.__init__(self,owner)

    # class version of speak method
    def speak(self):
        print(f'Dog: {self._name} is woof')


d1= Dog('lucy', 'xyz')
d1.speak()


'''Base_class 1 & Base_class 2 --> property inherit by Derive_class'''