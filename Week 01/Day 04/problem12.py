# choice based 

def add(a, b):
    return a + b

def diff(a, b):
    return a - b

def product(a, b):
    return a * b

def div(a, b):

    if b == 0: 
        return "cannot be divided by zero"

    else:
        return a / b  


print("1. Addition") 
print("2. Difference")
print("3. Product")
print("4. Division")
print("5. Exit")   

choice = int(input("enter number from 1-5 as per your choice: "))

if choice == 5:
    print("Exit successful")
    
elif ( choice >= 1 and choice <= 4):

    n1 = int(input("enter 1st number: "))
    n2 = int(input("enter 2nd number: "))
    
    if choice == 1:
        print("Addition =", add(n1, n2))

    elif choice == 2:
        print("Difference =", diff(n1, n2))    

    elif choice == 3:
        print("Product =", product(n1, n2))

    else:
        print("Quotient =", div(n1, n2))

else:
    print("Invalid")