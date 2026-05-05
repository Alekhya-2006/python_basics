# Program 03: take 3 inputs, convert all to float and print average of them

num1 = int(input("enter 1st number: "))
num2 = int(input("enter 2nd number: "))
num3 = float(input("enter 3rd number in floating points: "))

num1 = float(num1)
num2 = float(num2)

avg = (num1 + num2 + num3) / 3

print("The average of the 3 input numbers is ", avg)
