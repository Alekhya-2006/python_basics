# Even or odd function

# function definition
def evenOdd(n):
    return "even" if n%2 == 0 else "Odd"

num = int(input("Enter a number to check even or Odd: "))

print(evenOdd(num))