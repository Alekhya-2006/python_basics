 # reverse a number using for loop

n = input("Enter a number: ")

reverse = ""

for digit in n:
    reverse =  digit + reverse

print(reverse)