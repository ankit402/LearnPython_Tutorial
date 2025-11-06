

class Vehicle:
    def __init__(self,make, model, year):
        self._make= make
        self._model = model
        self._year = year

    def EngineType(self):
        pass

class Car(Vehicle):
    def __init__(self,drivetype):
        self.drivetpye = drivetype

class Tesla(Car):
    def __init__(self,make,model,year,drivetype):
        Vehicle.__init__(self,make,model,year)
        Car.__init__(self,drivetype)

    def __str__(self):
        return f"Vehicle ({self._make}, {self._model} , {self._year}, {self.drivetpye})"
    def EngineType(self):
        print("Engine type is Electric")



print(Tesla("T", "L", 2023, "Autmatic"))