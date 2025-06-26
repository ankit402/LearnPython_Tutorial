#"Create a base class named `Shape` with an attribute `color`.
# Create a derived class named `Circle` that inherits from `Shape` and adds an attribute `radius`.
# Use the `super()` function to initialize the attributes.
# Create an object of the `Circle` class and print its attributes.\n",


class Shape:
    def __init__(self, color):
        self.color = color
        print("Shape initialized")
    #        ❌pass Short Answer:
    # No — if the parent constructor (__init__) only has pass,
    # then it does not store self.color, and you’ll get an error:

class Circle(Shape):
    def __init__(self,color, radius):
        #super().__init__(self)
        '''❌ self.color = color is already handled by the parent class — but you didn't store it there.
        ➤ Since you used pass in the Shape.__init__, it does nothing.
            You should store the color.'''
        super().__init__(color)  # Call parent constructor correctly
        print("Circle initialized")
        self.radius = radius
        #❌self.color = color

    #dunder method or magic method to overloading the inbuilt function
    def __str__(self):
        return f'Circle {self.color} radius {self.radius}'


c= Circle(color = 'red', radius = 2)
print(c)
