#  "Create a base class named `Device` with an attribute `brand`.
#  Create a derived class `Phone` that inherits from `Device` and adds an attribute `model`.
#  Create another base class `Camera` with an attribute `resolution`.
#  Create a derived class `Smartphone` that inherits from both `Phone` and `Camera`.
#  Create an object of the `Smartphone` class and print its attributes."

#base class
class Device:
    def __init__(self, brand):
        self.brand = brand
#derived class
class Phone(Device):
    def __init__(self,brand, model):
        super().__init__(brand)
        self.model = model
       # print(f"Phone model is {self.model}")

#base class
class Camera:
    def __init__(self, resolution):
        self.resolution = resolution
       # print(f"Camera resolution is {self.resolution}")

#derived class
class SmartPhone(Phone, Camera):
    def __init__(self, model,brand,resolution):
        Phone.__init__(self,brand, model) # Initialize Phone
        Camera.__init__(self, resolution) # Initialize Camera

    def __str__(self):
        return f"Phone model is {self.model}, and camera resolution is {self.resolution}"
s=SmartPhone("Sony" , "test", '150MP')
print(s)


#this is the last program by me that is not required any modification by ChatGPT.
