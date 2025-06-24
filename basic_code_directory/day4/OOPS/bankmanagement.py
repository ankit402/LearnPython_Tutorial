#define bankaccount class
class BankAccount:
      def __init__(self, owner, balance=0,):
          self.owner = owner
          self.balance = balance
      # deposit
      def deposit(self, amount):
          self.balance += amount
          print(f"After Deposit {amount} balance: {self.balance}")
      #withdraw
      def withdraw(self, amount):
          if amount > self.balance:
              print(f'Insufficient balance: {self.balance}')
          else:
              self.balance -= amount
          print(f"After Withdrawal {amount} balance: {self.balance}")
     #get_balance
      def get_balance(self):
          print(f'My balance is {self.balance}')

myaccount=BankAccount("john", 4000)
myaccount.deposit(100)
myaccount.withdraw(500)
myaccount.get_balance()