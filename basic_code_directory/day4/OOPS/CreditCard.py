class CreditCards:
    def __init__(self, BankName, Cardlimit, Balance):
        self.BankName = BankName
        self.Cardlimit = Cardlimit
        self.Balance = Balance

    #cash on card
    def CashonCard(self, Amount):
        self.Amount = Amount
        if Amount > self.Cardlimit:
            print(f'Insufficient Cardlimit {self.Cardlimit} limit: {self.Balance} Amount is not possible')
        if Amount == self.Cardlimit:
            print(f'You can take 90 % cash on card limit')
        if Amount > self.Balance:
            print(f'Insufficient balance: {self.Balance} Amount is not possible')
        else:
            self.Balance -= Amount
            print(f'Congratulations you are eligible to get cash on card {Amount} balance amount { self.Balance}')

mybank= CreditCards("ADCB", 20000, 4000)
mybank.CashonCard(1000)

mybank= CreditCards("RAK", 8000, 1400)
mybank.CashonCard(2000)

mybank= CreditCards("ADIB", 20000, 10000)
mybank.CashonCard(1500)