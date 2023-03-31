class Bankaccount:
    balance = 500000
    def deposit(self):
        print("Deposit")
    def withdraw(self):
        print("Withdraw")
    def checkbalance(self):
        print("Check Balance")
    def transfer(self):
        print("Transfer")

class Interestaccount(Bankaccount):
    def interest(self):
        print("Interest")
    def deposit(self):
        print("Deposit")

class Chargingaccount(Interestaccount):
    def fee(self):
        print("fee")
    def withdraw(self):
        print("Withdraw")

b = Bankaccount()
b.deposit()
b.withdraw()
b.checkbalance()
b.transfer()


i = Interestaccount()

i.interest()

c = Chargingaccount()
c.fee()
