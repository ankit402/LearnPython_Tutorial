# "Create a class named `BankAccount` with private attributes `account_number` and `balance`.
# Add methods to deposit and withdraw money, and to check the balance.
# Ensure that the balance cannot be accessed directly.\n",


class BankAccount:
    def __init__(self, account_number, balance):
        self.__Account = account_number
        self.__balance = balance

    @property
    def get__Account(self):
           return self.__Account

    @property
    def get__balance(self):
           return self.__balance

    @property
    def set__Account(self,value):
        self.__Account=value
    @property
    def set__balance(self,value):
         self.__balance=value


    def deposit(self, amount):
        if amount > 0:
            amount += self.__balance
            print(f"You have total deposit {amount}")
        else:
            print("Deposit amount must be positive.")
    def withdraw(self, amount):
        if amount > 0:
            amount -= self.__balance
            print(f"You have total withdrawn {amount}")
        else:
            raise ValueError("Balance cannot be negative.")

c1= BankAccount(112133132, 1200)
c1.deposit(100)
c1.withdraw(100)


#"In the `BankAccount` class, use property decorators to get and set the `balance` attribute.
# Ensure that the balance cannot be set to a negative value.\n",
