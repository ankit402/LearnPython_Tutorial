from abc import ABC,abstractmethod
class RecipeBook(ABC):
    # Optional: give default implementation for boilingWater
    #this is not an abstract method
    def boilingWater(self):
        print("Boiling water not required.")
        return "Water not required"
    @abstractmethod
    def boilingMlik(self):
        pass
    @abstractmethod
    def Recipe(self):
        pass
# Concrete subclass
class Tea(RecipeBook):
    def __init__(self, drink_type):
        #constructor
        self._method = drink_type
    #abstract Method
    def boilingWater(self):
        print(f'Boiling water temperature 90°C')
        return "Boiling water temperature 90°C"
    def boilingMlik(self):
        print(f'Boiling milk temperature 80°C')
        return "Boiling milk temperature 80°C"
    def Recipe(self):
        print(f'Wait until boiled properly then mix some tea and sugar and get ready with cup of tea after 5 minutes')
# Concrete subclass
class Coffee(RecipeBook):
    def __init__(self, drink_type):
        #constructor
        self._method = drink_type

    def boilingMlik(self):
        print(f'Boiling milk temperature 80°C')
        return "Boiling milk temperature 80°C"

    def Recipe(self):
        print(f'Wait until boiled properly then mix some coffee and sugar and get ready with cup of Coffee after 5 minutes')
    #
# Create objects and call methods
print('f***********Prepare tea will use the below recipe***********************')
t=Tea("Tea")
t.boilingWater()
t.boilingMlik()
t.Recipe()
print('f***********Prepare tea will use the below recipe***********************')
c=Coffee("Coffee")
c.boilingMlik()
c.Recipe()