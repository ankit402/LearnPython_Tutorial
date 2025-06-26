# "Create a base class named `Walker` with a method `walk` that prints a walking message.
# Create another base class named `Runner` with a method `run` that prints a running message.
# Create a derived class named `Athlete` that inherits from both `Walker` and `Runner`.
# Create an object of the `Athlete` class and call both methods.\n",

#base class
# class Walker:
#     def walk(self):
#         return "I am walking"
#
# class Runner:
#     def Run(self):
#         return "I am running..."
#
# #concrete or dervied class
#
# class Athlete(Walker, Runner):
#         pass
#
# a1=Athlete()
# print(a1.walk())
# print(a1.Run())

#"In the `Athlete` class, override the `walk` method to print a different message.
# Create an object of the class and call the `walk` method. Use the `super()`
# function to call the `walk` method of the `Walker` class.\n",

#base class 1
class Walker:
    def walk(self):
        return "I am walking"

#base class 2
class Runner:
    def run(self):  # Use lowercase method name for consistency
        return "I am running..."

# Concrete or derived class
class Athlete(Walker, Runner):
    def __init__(self,training_hours):
        self.training_hours = training_hours
        #derive class overriding the base classes
    def walk(self):
            print("Athlete walking...")
            super().walk()

    def run(self):
            print("Athlete running very fast...")
            super().run()

 # "In the `Athlete` class, add an attribute `training_hours` and a method `train` that prints the training hours.
 # Create an object of the class and call the method.\n",
    #added train method for printing training hours
    def train(self):
        print(f'Athlete training {self.training_hours} hours per day')


a1 = Athlete(5)
a1.train()
a1.walk()
a1.run()







