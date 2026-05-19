# Bank Account Class
# Concepts: Methods modifying object state

class BankAccount:

    def __init__(self, name , balance):
        self.name = name
        self.balance = balance

    def deposit(self, amount):
        self.balance = amount + self.balance

    def withdraw(self, amount):

        if amount <= self.balance:
            self.balance = self.balance - amount   
            print("Withdrawal Successful")

        else:
            print("Insufficient Balance")

    def display_balance(self):
        return self.balance


customer = BankAccount("Alekhya", 6000)

while True: 
    print("\n1. Deposit")
    print("2. Withdrawal")
    print("3. Display Balance")
    print("4. Exit")

    n = int(input("Choose option(1-4): "))

    if n == 4:
        print("Successfully Exited")
        break

    if n > 0 and n < 4:
        
        if n == 1:
            amount = int(input("Enter the amount: "))
            customer.deposit(amount)
            print("Successfully Deposited")

        elif n == 2: 
            amount = int(input("Enter the amount: "))
            
            customer.withdraw(amount)

        else:
            print(f'Balance = {customer.display_balance()}')   


    else:
        print("Invalid Choice")
        break                       