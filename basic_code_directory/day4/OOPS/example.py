#  "Create a class named `Vector` with attributes `x` and `y`.
#  Overload the `+` operator to add two `Vector` objects.
#  Create objects of the class and test the operator overloading.\n",

class Vector:
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y

    # Overloading the + operator
    def __add__(self, other):
        if isinstance(other, Vector):
                return Vector(self.x + other.x, self.y + other.y)
        raise  TypeError("Operand must be type Vector")

    def __str__(self):
        return f"Vector({self.x}, {self.y})"

v1 = Vector(2, 3)
v2 = Vector(4, 1)

v3 = v1 + v2  # calls v1.__add__(v2)
print(v3)     # Output: Vector(6, 4)
