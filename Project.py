class Bank(): 
    def __init__(self, initial_amount=0):
        self.balance=initial_amount
    
    def withdraw(self, amount_money):
        try:
            amount_money=float(amount_money)
        except ValueError:
            amount_money=0
        self.balance-=amount_money
        self.log_transaction(f"Withdrew {amount_money}")
    
    def deposit(self, amount_money):
        try:
            amount_money=float(amount_money)
        except ValueError:
            amount_money=0
        self.balance+=amount_money
        self.log_transaction(f"Deposited {amount_money}")
    
    def log_transaction(self, transaction_activity):
        with open("bankActivities.txt","a") as file:
            file.write(f"{transaction_activity}, the new balance is: {self.balance}.\n")


initial_balance = input("Please enter the initial balance: ")
default_balance=50000
if(initial_balance.isdigit()):
    acount = Bank(initial_amount=float(initial_balance))
else:
        acount = Bank(initial_amount=default_balance)

with open("bankActivities.txt","w") as file:
            file.write(f"Bank activities:\n")
            file.write(len("Bank activities:")*'-'+"\n")
            if initial_balance.isdigit():
                file.write(f"Starting balance: {initial_balance}.\n")
            else:
                file.write(f"Starting balance: {default_balance}.\n")

while(True):
    action = input("Please enter your action (withdraw / deposit / stop): ")
    if action.lower() in ["deposit", "withdraw", "stop"]:
        if action.lower()=="deposit":
            amount_money = input("How much do you want to put in? ")
            acount.deposit(amount_money)
        elif action.lower()=="withdraw":
            amount_money = input("How much do you want to take out? ")
            acount.withdraw(amount_money)
        else: # action.lower()=="stop"
            print("Leaving the ATM.\n")
            break
        print(f"The new balance is: {acount.balance}.\n")
    else:
        print("Please enter a valid input...")
