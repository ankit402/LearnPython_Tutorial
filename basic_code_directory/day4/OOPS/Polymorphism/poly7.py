# "Create an abstract base class named `Employee` with an abstract method
# `calculate_salary`.
# Create two derived classes `FullTimeEmployee` and `PartTimeEmployee` that implement
# the `calculate_salary` method. Create objects of the derived classes and call the
# `calculate_salary` method.\n",
from abc import ABC, abstractmethod


class Employee(ABC):
    @abstractmethod
    def calculate_salary(self):
        pass

#derived class
class FullTimeEmployee(Employee):
    def __init__(self, monthly_salary):
        self.monthly_salary = monthly_salary
    def calculate_salary(self):
        return self.monthly_salary
       # print("Full time  employee salary calculated for 30 days ")

class PartTimeEmployee(Employee):
    def __init__(self, hours_worked, hourly_rate):
        self.hours_worked = hours_worked
        self.hourly_rate = hourly_rate
    def calculate_salary(self):
        return self.hours_worked* self.hourly_rate
        #print("Part Time employee salary calculated for hourly")

c=FullTimeEmployee(5000)


w = PartTimeEmployee(80,20)

print("Full-Time Employee Salary:", c.calculate_salary())
print("Part-Time Employee Salary:", w.calculate_salary())