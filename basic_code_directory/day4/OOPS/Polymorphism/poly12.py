#"Create a base class named `Account` with private attributes `account_number`
# and `balance`.
# Add methods to get and set these attributes.
# Create a derived class named `SavingsAccount`
# that adds an attribute `interest_rate`.
# Create an object of the `SavingsAccount`
# class and test the encapsulation.\n",
'''Encapsulation in Class Hierarchies'''

class Account:
    def __init__(self,account_number,balance):
        self.__account_number =account_number
        self.__balance = balance
    @property
    def accountNumber(self):
        return self.__account_number
    @accountNumber.setter
    def accountNumber(self,account_number):
        self.__account_number= account_number

    @property
    def balance(self):
        return self.__balance

    @balance.setter
    def balance(self, balance):
        self.__balance = balance


class SavingAccount(Account):
    def __init__(self,account_number, balance, interest_rate):
        super().__init__(account_number, balance)
        # all property should be private
        self.__interest_rate = interest_rate
        print("saving account have  good interest rate")

    @property
    # Getter for interest_rate
    def interest_rate(self):
        return self.__interest_rate

    @interest_rate.setter
    # Setter for interest_rate
    def interest_rate(self, interest_rate):
        if interest_rate < 0:
            raise ValueError("Interest rate cannot be negative")
        self.__interest_rate = interest_rate

sa= SavingAccount(12222,1000, 7)

print("Account Number:", sa.accountNumber)  # via getter setter we can access  it means encapsulation works well
print("Balance:", sa.balance)
print("Interest Rate:", sa.interest_rate)