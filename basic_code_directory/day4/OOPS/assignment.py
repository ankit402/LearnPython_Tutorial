# "Create a custom exception named `InsufficientBalanceError`.
# In the `BankAccount` class, raise this exception when a withdrawal amount
# is greater than the balance. Handle the exception and print an appropriate message.\n",
from logging import exception

class BankAccount:
    def __init__(self,balance):
        self._balance = balance

    #withdraw
    def withdraw(self,amount):
        try:
            if amount > self._balance:
                print(f'Insufficient balance: {self._balance}')
                raise ("insufficient balance")
            else:
                self._balance -= amount
                print(f'Withdrawn: {amount}')
        except exception as Ex:
            raise  print(Ex)

c1=BankAccount(100)
c1.withdraw(100)

