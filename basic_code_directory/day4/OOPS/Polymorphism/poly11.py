# "Create an abstract base class named `Appliance` with an abstract property `power`.
# Create two derived classes `WashingMachine` and `Refrigerator` that implement the `power`
# property. Create objects of the derived classes and access the `power` property.\n",
from abc import ABC, abstractmethod


class Appliance(ABC):
    @property
    @abstractmethod
    def power(self):
        """Abstract property for power"""
        pass

#derived class
class Washingmachine(Appliance):
    @property
    def power(self):
        print("washing machine more power than refrigerator")

class Refrigerator(Appliance):
    @property #Abstract Properties
    def power(self):
        print("refrigerator is taking good energy power")


a=Washingmachine()
a.power()

s=Refrigerator()
s.power()

