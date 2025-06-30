# Create an abstract base class named `Worker` with an abstract method `work`.
# Create two derived classes `Engineer` and `Doctor` that implement the `work` method.
#
# Create another derived class `Scientist` that inherits from both `Engineer`
# and `Doctor`.
# Create an object of the `Scientist` class and call the `work` method."
from abc import ABC,abstractmethod

# base class
class Worker(ABC):
   @abstractmethod
   def work(self):
       pass

#derived class
class Engineer(Worker):
    def work(self):
        print("Engineers working with computer or site works")


class Doctor(Worker):
    def work(self):
        print("Doctor working  in the hospital or  clinic")

class Scientist(Engineer,Doctor):
    # Engineer().__init__()
    # Doctor().__init__()

    def work(self):
        print("Scientist works in lab and may be both engineer and doctor.")

a=Scientist()
a.work()
