#create class Bank account
class Account:

    def __init__(self, owner, balance=0):
        
        self.owner = owner
        self.balance = balance

    def deposit(self, dep_amount):
        
        self.balance = self.balance + dep_amount
        print(f"Added {dep_amount} to the balance")

    def withdrawl(self, withdraw_amt):

        if self.balance >= withdraw_amt:
            self.balance = self.balance - withdraw_amt
            print(f"withdrawl accepted, total balance : {self.balance}")
        else:
            print("sorry not enough funds")

    def __str__(self):
        return f"owner : {self.owner}  \nBalance: {self.balance}"
    
#Instantiate the class 
acc1 = Account('sanjeev', 500)

print(acc1)

#show the account owneer attribute 
print(acc1.owner)

#show the account owner balance
print(acc1.balance)

#make a deposit of the 1000 and withdrawls
acc1.deposit(1000)

acc1.withdrawl(500)

acc1.withdrawl(5000)