#base class
class Car:
    def __init__(self, type):
        self.type = type

    def EngineType(self):
        pass

class Tesla(Car):
    def __init__(self,type, isdrivingauto):
        super().__init__(type)  # self is not required here calls for set constructor Car init type
        self.isdrivingauto = isdrivingauto

    def is_driving(self):
        print(f"Tesla is {'driving automatically' if self.isdrivingauto else 'being driven manually'}.")


#This overrides the placeholder method from Car.
    def EngineType(self):
        if self.type.lower() == "electric":
            print("Tesla engine type is electric.")
        else:
            print("Tesla engine type is petrol.")


#🔸 Object Creation & Method Calls
c1 = Tesla("electric", True)
c1.EngineType()
c1.is_driving()


#explain about the above code

'''🧱 Class Hierarchy
This code uses inheritance in object-oriented programming (OOP). A base class Car is created, and a child class Tesla extends it.

🔹 class Car

class Car:
    def __init__(self, type):
        self.type = type  # Stores the type of engine (e.g., "electric", "petrol")

    def EngineType(self):
        pass  # Placeholder method (meant to be overridden by child classes)
__init__ method: Constructor that takes type (like "electric" or "petrol") and assigns it to the instance.

EngineType() method: Empty method (placeholder) — it's expected that subclasses will implement this.

🔹 class Tesla(Car)

class Tesla(Car):
    def __init__(self, type, isdrivingauto):
        super().__init__(type)
        self.isdrivingauto = isdrivingauto
Tesla is a child class of Car. It inherits its properties and methods.

super().__init__(type) calls the parent class (Car) constructor to initialize type.

isdrivingauto is a new property that tells whether the Tesla is using autopilot (True) or manual driving (False).

🔹 is_driving() method

    def is_driving(self):
        print(f"Tesla is {'driving automatically' if self.isdrivingauto else 'being driven manually'}.")
This prints a message depending on the value of isdrivingauto.

If True: prints "Tesla is driving automatically."

If False: prints "Tesla is being driven manually."

🔹 EngineType() method

    def EngineType(self):
        if self.type.lower() == "electric":
            print("Tesla engine type is electric.")
        else:
            print("Tesla engine type is petrol.")
This overrides the placeholder method from Car.

It checks the type of the car:

If it's "electric" (case-insensitive), it prints that the engine is electric.

Otherwise, it says the engine is petrol (for fallback/default logic).

🔸 Object Creation & Method Calls

c1 = Tesla("electric", True)
c1.EngineType()
c1.is_driving()
Creates a Tesla object c1:

type = "electric"

isdrivingauto = True (means autopilot is ON)

Calls EngineType() → prints: "Tesla engine type is electric."

Calls is_driving() → prints: "Tesla is driving automatically."

✅ Summary
Concept	Explanation
Inheritance	Tesla inherits from Car
Constructor	Initializes object with type and isdrivingauto
Method Override	Tesla overrides EngineType() from Car
Conditional Logic	Prints different messages based on input values
Object Creation	Creates and uses a Tesla object with behavior'''