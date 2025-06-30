#"Create a data class named `Product` with private attributes `product_id`,
# `name`, and `price`.
# Add methods to get and set these attributes.
# Ensure that the price cannot be set to a negative value.\n",


class Product:
    def __init__(self,product_id, name, price):
        self.__product_id=product_id
        self.__name = name
        self.__price= price

    @property
    def get_product_id(self):
        return self.__product_id

    @get_product_id.setter
    def set_product_id(self, product_id):
        self.__product_id = product_id

    @property
    def getname(self):
        return self.__name

    @getname.setter
    def setname(self, name):
        self.__name = name
    @property
    def getprice(self):
        return self.__price

    @getprice.setter
    def  setprice(self, price):
        if price < 0:
            raise ValueError("Value should not be less than zero")
        self.__price=price

p = Product(101, "Laptop", 1500)
print("Product ID:", p.get_product_id)
print("Name:", p.getname)
print("Price:", p.getprice)