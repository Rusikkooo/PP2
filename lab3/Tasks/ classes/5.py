class Account:
    def __init__(self,owner,balance):
        self.owner = owner #владелец
        self.balance = balance
    
    def deposit(self,amount):
        if amount> 0 :
            self.balance+=amount
            print("Your current balance :",self.balance)
        else :
           print("Error")
    def withdraw(self,amount):
        if amount<self.balance:
            self.balance-=amount
            print("Your current balance :",bank.balance)
            
bank = Account("Rusik",10000)

print("Account owner :", bank.owner)

print("Initial balance :",bank.balance)

bank.deposit(1000)

bank.withdraw(3000)

bank.withdraw(2000)

    