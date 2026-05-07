# Check palindrome number:

n = input("Enter a number: ")

reverse = ""

for digit in n:
    reverse =  digit + reverse

if n == reverse:
    print("Palindrome")
else:
    print("Not Palindrome")    