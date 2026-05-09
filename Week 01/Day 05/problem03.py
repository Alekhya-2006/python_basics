# function to print the digits of a number

def digits(n):

    for digit in str(n):
        print(digit)

num = int(input("enter a number: "))

digits(num)   