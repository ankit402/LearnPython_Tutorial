# class Person:
#     def __init__(self, name,age):
#         self.name = name # public variable
#         self.age = age
#
# def get_person(person):
#     return person.name
#
# p=Person('John',20)
# print(get_person(p))
# print(dir(p))



#protected variable

#base Class
# class Person:
#     def __init__(self, name):
#         self._name = name
#
# #derived class
# class Student(Person):
#     def __init__(self, name):
#         super().__init__(name)
#
#
# p=Student('John')
# print(p._name)

#Private variable
class Person:
    def __init__(self, name,age,dob):
        self.__name = name # private variable
        self.__age = age # private variable
        self.dob = dob # public variable
        #private variable can not be access outside the class


    #getter method
    def getname(self):
        return self.__name

    ##setter method
    def setname(self, value):
        self._name = value

# p=Person('John',20,12)
# print(p.getname())

#access and modify the private variable
p=Person('John',24,12)
print(p.getname())
p.setname('ankit')
print(p.getname())