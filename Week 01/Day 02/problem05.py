# Simple calculator

n1 = int(input("Enter the first number: "))
Operator = input("Enter the operator(+, -, *, /): ")
n2 = int(input("Enter the second number: "))

if (Operator == "+"):
    print(f'{n1} + {n2} = {n1 + n2}')
elif (Operator == "-"):
    print(f'{n1} - {n2} = {n1 - n2}')
elif (Operator == "*"):
    print(f'{n1} * {n2} = {n1 * n2}')        
elif (Operator == "/" ):
    if(n2 != 0):
        print(f'{n1} / {n2} = {n1 / n2}')
    else:
        print("Infinite")
else:
    print("Invalid")            