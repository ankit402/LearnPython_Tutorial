'''🔁 Polymorphism in Python — Explained Simply
Polymorphism means "many forms". In Python (and other OOP languages),
it allows objects of different classes to be treated the same way,
especially when they share method names.

✅ Real-Life Analogy:
Think of a remote control:
You can use it for a TV, AC, or projector.
The remote performs the same "press button" action, but each device responds differently.

🧱 Types of Polymorphism in Python:
1. Compile-time Polymorphism (via method overloading)
👉 Python does not support method overloading natively like C++/Java, but you can simulate it using default arguments or *args.

2. Runtime Polymorphism (via method overriding) ✅
👉 The most common form in Python — achieved through inheritance.'''

#🧪 Example: Runtime Polymorphism

class Car:
    def EngineType(self):
        print(f'Generic Engine')
    def Engine(self):
        print(f'1.0')

class Motor(Car):
    def EngineType(self):
        print(f'Powerful Engine')
        print(f'2.0')
class Buss(Car):
    def EngineType(self):
        print(f'Heavy Vehicle Engine')
        print(f'5.0')
class GMC(Car):
    def EngineType(self):
        print(f'Most Powerful Engine')
        print(f'3.8')
class Chevrolet(Car):
    def EngineType(self):
        print(f'Turbo Engine')
        print(f'1.5T')
class Nissan(Car):
    def EngineType(self):
        print(f'Nissan Engine')
        print(f'2.5')
# Polymorphic behavior
cars = [GMC(), Chevrolet()]
for car in cars:
    car.EngineType()

'''✅ What's Happening:
Each object (Tesla, BMW) is treated as a Car.
When we call EngineType(), the appropriate version is run based on the object.
This is polymorphism — same method name, different behavior.

'''

'''✅ Summary
Type	Description	Example
Method Overriding	--> Subclass redefines parent method	
Tesla.EngineType() --> overrides Car.EngineType()
Duck Typing	Different classes with same method name	obj.speak() in Duck and Human
Interface-Like	Functions accept any object with required method	
test_drive(vehicle)'''