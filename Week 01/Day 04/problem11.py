# Calculator function

def calculator(a, operator, b):

    if operator == "+":
        return a + b

    elif operator == "-":
        return a - b

    elif operator == "*":
        return a * b

    elif operator == "/":

        if b == 0:
            return "Cannot divide by zero"

        return a / b

    else:
        return "Invalid operator"
    
n1 = int(input("enter 1st number: "))
op = input("enter (+, -, *, /): ")
n2 = int(input("enter 2nd number: "))

print(calculator(n1, op, n2))