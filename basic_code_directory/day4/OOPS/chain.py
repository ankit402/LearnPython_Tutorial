''' "Create a class named `Calculator` with
methods to add, subtract, multiply, and divide.
Each method should return the object itself to allow method chaining.
Create an object and chain multiple method calls."
  '''


class Calculator:
    def __init__(self, value):
        self._result =value
        print(f'Calculator Method Initialize')
    print("**************Addition Chain Started************")
    def add(self, number):
        self._result += number
        print(f'Result of Addition is: {self._result}')
        return self

    print("**************Substraction Chain Started************")
    def sub(self, number):
        self._result -= number
        print(f'Result of Subtraction is: {self._result}')
        return self

    print("**************multiply Chain Started************")
    def multiply(self, number):
        self._result *= number
        print(f'Result of Multiplication is: {self._result}')
        return self

    print("**************divide Chain Started************")
    def divide(self, number):
        self._result /= number
        print(f'Result of Division is: {self._result}')
        return self

    print("**************Final Result************")
    def ShowResult(self):
        print(f'Result: {self._result}')
        return self

c1=Calculator(6)
c1.add(100).sub(12).multiply(3).divide(5).ShowResult()
