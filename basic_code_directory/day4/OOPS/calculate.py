# "Create a class named `Calculator` with methods to add,
# subtract, multiply, and divide. Each method should return
# the object itself to allow method chaining. Create an object
# and chain multiple method calls."
import math


class Calculator:
    def __init__(self,value=0):
        self.result  = value
        print(f'Calculator Method Initialized Successfully')
        pass

    def add(self,number):
         self.result  += number
         print(f'Add result is: {self.result}')
         return self

    def sub(self,number):
        self.result  -= number
        print(f'Sub result is: {self.result}')
        return self

    def multiply(self,number):
        self.result  *= number
        print(f'multiply result is: {self.result}')
        return self

    def divide(self,number):
        self.result  /= number
        print(f'divide result is: {self.result}')
        return self

    def show(self):
        print(f"Result: {self.result}")
        return self

f1=Calculator(5)
f1.add(10).sub(4).divide(3).multiply(2).show()