# Challenge 5: Handling a Bank Account


# Solution
class Account:
    def __init__(self, title=None, balance=0):
        self.title = title
        self.balance = balance
    
    def withdrawal(self, amount):
        if self.balance >= amount:
            self.balance = self.balance - amount
            print("Withdrawal amount is: ", amount)
            print("Remaining balance is: ", self.balance)
        else:
            print("Insufficient balance")

    def deposit(self, amount):
        self.balance = self.balance + amount
        print("Deposited amount is: ", amount)
        print("Available balance is: ", self.balance)
    
    def getBalance(self):
        print('The current balance is: ',self.balance)

class SavingsAccount(Account):
    def __init__(self, title=None, balance=0, interestRate=0):
            super().__init__(title, balance)
            self.interestRate = interestRate
    
    def interestAmount(self):
        Interest_Amount = ((self.interestRate*self.balance)/100)
        print("Interest Amount: ", Interest_Amount)

print('ACCOUNT DETAILS')
X = Account('Ashish',2000)
X.withdrawal(500)
X.deposit(500)
X.getBalance()


print('SAVINGS ACCOUNT DETAILS')
A = SavingsAccount('Ashish',2000,5)
A.withdrawal(500)
A.deposit(500)
A.interestAmount()