#"Create a class named `Vehicle` with a method `start` that prints a starting message.
# Create a derived class `Car` that overrides the `start` method to print a different message.
# Use the `super()` function to call the `start` method of the `Vehicle` class.
# Create an object of the `Car` class and call the `start` method.\n",


        '''Assignment 10: Method Overriding and `super()`\n",'''
class Vehicle:
    #self refers to the current object (the instance of the class) that is calling the method.
    def start(self):
        print(f'Vehicle started....')

'''You're calling super().__init__(), but:
The Vehicle class does not define an __init__() method.
You're trying to call the base class's start() method, not __init__.'''

#derived class
class Car(Vehicle):
    def start(self):
        #super().__init__()
        super().start()  # ✅ Correct: Call Vehicle's start()
        print( f'Car started....')
# create object and call method
c1= Car()
c1.start()


