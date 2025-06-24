# #class Car define with pass
# class Car:
#     pass
#
# #object initialize
# audi=Car()
# telsa=Car()
#
# # set the attribute
# audi.color = 'black'
#
# print(audi.color)

class Dog:
    ## constructor
    def __init__(self, name, age, color):
        self.name = name
        self.age = age
        self.color = color

    def bark(self):
        print(f"the dog {self.name} is says woof")

    def show_color(self):
        print(f" dog {self.name} color is {self.color}")


dog=Dog("john", 32, 'brown')
dog.bark()
#color method name or parameter not possible same
dog.show_color()
