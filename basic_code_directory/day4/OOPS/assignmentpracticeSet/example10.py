#  "Create a base class named `Bird` with a method `speak`.
#  Create two derived classes `Parrot` and `Penguin` that override the `speak` method.
#  Create a list of `Bird` objects and call the `speak` method on each object to demonstrate polymorphism.\n",

class Bird:
    def speak(self):
        print("Some generic bird sound")

class Parrot(Bird):
    def speak(self):
        print ("Parrot says: Squawk!")

class Penguin(Bird):
    def speak(self):
        print ("Penguin says: Honk!")

#create a object of bird
# List of Bird objects (including derived classes)
b =[Bird(), Parrot(), Penguin()]

for b in b:
    b.speak()
    