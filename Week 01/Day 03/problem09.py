# factorial of a number

n = int(input("enter a number: "))

factorial = 1

for i in range(n, 0, -1):
    factorial = factorial * i 

print(f'{n}! = {factorial}')