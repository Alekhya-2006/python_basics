# ATM withdrawal Simulation

acc_balance = int(input("Enter the account balance: "))
withdrawal_amount = int(input("Enter the withdrawal amount: "))

if acc_balance < 0 or withdrawal_amount < 0:
    print("Invalid input")

elif (acc_balance >= withdrawal_amount and
    withdrawal_amount % 100 == 0 and 
    acc_balance - withdrawal_amount >= 500):

    print("Withdrawal successful")
    print("The remaining balance is ", acc_balance - withdrawal_amount)

else:
    print("Withdrawal Cancelled")

    if(withdrawal_amount % 100 != 0):
        print("Invalid withdrawal amount")
      
    elif(acc_balance < withdrawal_amount):
        print("Insufficient balance") 

    elif(acc_balance - withdrawal_amount < 500):
        print("Minimum balance after withdrawal should be 500")

    else:
        print("try again")             