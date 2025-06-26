#diamond inheritance,


class Person:
    def __init__(self, name):
        self.name = name
        print('Person created')

class Employee(Person):
    def __init__(self,name, employee_id):
        super().__init__(name)  #parent called
        self.employee_id = employee_id
        print('Employee created')

class Trainer(Person):
    def __init__(self,name, trainer_subject):
        super().__init__(name)
        self.trainer_subject = trainer_subject
        print('Trainer created')

class Manager(Employee,Trainer):
    def __init__(self, name, employee_id, trainer_subject):
       # super().__init__( name, employee_id) # Only one call to super() #apply here
       # self.trainer_subject = trainer_subject
       Employee.__init__(self, name, employee_id)
       Trainer.__init__(self, name, trainer_subject)
       print('Manager created')

    def __str__(self):
        return f'{self.name} having ID {self.employee_id} and Trainer {self.trainer_subject}'

    def introduce(self):
        print(f"Hi, I’m {self.name}, employee #{self.employee_id}, and I train in {self.trainer_subject}.")

print(Manager.__mro__)
#Create a object
#m1 = Manager("Varun", 102, 'python')

#✅ Solution: Use super() to Follow MRO
# Python uses Method Resolution Order (MRO) to ensure the parent class (Person) is called only once,
# even in a diamond inheritance setup.