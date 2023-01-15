# Challenge 4: Implement a Banking Account

# Solution
class Account:

    def __init__(self,title=None,balance=0):
        self.title = title
        self.balance = balance
    def GetTitle(self):
        print('Title:',self.title)
    def GetBalance(self):
        print('Balance:',self.balance)

class SavingsAccount(Account):

    def __init__(self,title=None,balance=0,interestRate=0):
        super().__init__(title,balance)
        self.interestRate = interestRate
    def getInterestRate(self):
        print('Rate of interest:',self.interestRate)
        
        
print('Account Details')
X = Account('Ashish',5000)
X.GetTitle()
X.GetBalance()


print('SavingsAccount Details')
A = SavingsAccount('Ashish',5000,5)
A.GetTitle()
A.GetBalance()
A.getInterestRate()