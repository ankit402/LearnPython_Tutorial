# "Create a class named `A` with a method `show` that prints a message.
# Create two derived classes `B` and `C` that inherit from `A` and override the `show` method.
# Create a class `D` that inherits from both `B` and `C`.
# Create an object of the `D` class and call the `show` method.
# Observe the method resolution order.\n",


class A:

        def show(self):
            print (f'Hey they A base class here..')

#Inheritance
class B(A):
        #Method Overriding
        def show(self):
            print(f'Hey they B child class here..')

class C(A):
    # Method Overriding
        def show(self):
            print(f'Hey they C child class here..')
#Multiple Inheritance
class D(B, C):  # Multiple inheritance
    pass

# Create object and call show()
d = D()
d.show()


# Check Method Resolution Order (MRO)
print(D.__mro__)