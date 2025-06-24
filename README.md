******************Abstraction in Python********************

#abstract implementation class , Method
#✅ Polished Python Code for Tea and Coffee Preparation
from abc import ABC, abstractmethod

class RecipeBook(ABC):
    def __init__(self, drink_type):
        self._drink_type = drink_type

    # Optional method: overridden if needed
    def boilingWater(self):
        print("Boiling water not required.")
        return "Water not required"

    @abstractmethod
    def boilingMilk(self):
        pass

    @abstractmethod
    def recipe(self):
        pass

#concrete class implementation
#🍵 Tea Class
class Tea(RecipeBook):
    def __init__(self):
        super().__init__("Tea")

    def boilingWater(self):
        print("🍵 Boiling water at 90°C")
        return "🍵 Boiling water at 90°C"

    def boilingMilk(self):
        print("🍵 Boiling milk at 80°C")
        return "🍵 Boiling milk at 80°C"

    def recipe(self):
        print("→🍵 Wait until boiled properly.")
        print("→🍵 Add tea leaves and sugar.")
        print("→🍵 Brew for 5 minutes and serve hot in a cup.")

#concrete class implementation
#☕ Coffee Class
class Coffee(RecipeBook):
    def __init__(self):
        super().__init__("Coffee")

    # No boilingWater() — uses default implementation from base class

    def boilingMilk(self):
        print("☕ Boiling milk at 80°C")
        return "☕ Boiling milk at 80°C"

    def recipe(self):
        print("→ ☕ Wait until milk is boiled.")
        print("→☕ Add coffee powder and sugar.")
        print("→☕  Stir well and serve hot in a cup.")

#Calling method
#🧪 Prepare Tea and Coffee

print("***********🍵 Preparing Tea ***********")
tea = Tea()
tea.boilingWater()
tea.boilingMilk()
tea.recipe()

print("\n***********☕ Preparing Coffee ***********")
coffee = Coffee()
coffee.boilingWater()
coffee.boilingMilk()
coffee.recipe()
