# "Create a class named `Vector` with attributes `x` and `y`.
# Overload the `+` operator to add two `Vector` objects.
# Create objects of the class and test the operator overloading.\n",

'''Polymorphism with Operator Overloading'''

class Vector:
    def __init__(self,x,y):
            self.x=x
            self.y=y
            # Overload the + operator

    def __add__(self, other):
        if isinstance(other, Vector):
            return Vector(self.x + other.x, self.y + other.y)
        return NotImplemented

    def __str__(self):
        return f"Vector({self.x}, {self.y})"

v=Vector(12,23)
