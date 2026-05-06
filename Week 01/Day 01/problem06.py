# Program 06: swap values of two numbers entered by the user

a = int(input("Enter 1st number: "))
b = int(input("Enter 2nd number: "))

a, b = b, a

print("1st number is ", a)
print("2nd number is ", b)