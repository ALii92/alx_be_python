class BankAccount:
    def __init__(self, account_balance ) :
        self.account_balance = account_balance 
        # account_balance = 0
    def deposit(self, amount):
        # amount = int(input("Enter the amount to deposit: "))
        self.account_balance += amount
    def withdraw(self, amount):
        # amount = int(input("Enter the amount to withdraw: "))
        if self.account_balance >= amount:
            
            self.account_balance -= amount
            return True
        else :
            return False
        
    def display_balance (self):
        print(f"Current Balance: ${self.account_balance:.2f}")
