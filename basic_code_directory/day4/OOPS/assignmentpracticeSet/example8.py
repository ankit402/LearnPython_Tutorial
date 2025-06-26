#"Create a class named `Base1` with an attribute `a`.
# Create a class named `Base2` with an attribute `b`.
# Create a class named `Derived` that inherits from both `Base1` and `Base2` and adds an attribute `c`.
# Initialize all attributes using the `super()` function.
# Create an object of the `Derived` class and print its attributes.\n",

'''Assignment 12: Complex Multiple Inheritance\n'''

class Base1:
    def __init__(self,a):
        self.a = a
        print(f'Base1 started....')

class Base2:
    def __init__(self,b):
        self.b = b
        print(f'Base2 started....')

class Derived(Base1,Base2):
    def __init__(self,a,b,c):
        self.c = c
        Base1.__init__(self, a)  #❌ Initialize Base1 and Base2 via super()
        Base2.__init__(self ,b) # Initialize Base1 and Base2 via multiple inheritance


#call object for Derived
obj = Derived(a=10, b=20, c=30)
print(obj)
