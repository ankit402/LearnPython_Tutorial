#"Create a class named `Person` with an attribute `name`.
# Create a class named `Employee` with an attribute `employee_id`.
# Create a derived class `Manager` that inherits from both `Person` and `Employee`.
# Use the `super()` function to initialize the attributes.
# Create an object of the `Manager` class and print its attributes.\n",

'''Assignment 9: Using `super()` in Multiple Inheritance\n"'''
class Person:
    def __init__(self,name):
        self.name = name

class Employee(Person):
    def __init__(self,name,employee_id):
        self.name = name
        super().__init__(name)
        self.employee_id = employee_id

class Manager(Employee):
    def __init__(self,name,employee_id):
         super().__init__(name,employee_id)
         #Employee.__init__(self,name,employee_id)

    def __str__(self):
        return f'{self.name} having ID {self.employee_id}'
#Manager → Employee → Person

m1= Manager('Varun', 102)
print(m1)
