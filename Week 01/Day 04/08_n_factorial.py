# function definition
def fact(n):
    f = 1
    for i in range(1, n+1):
        f *= i
        
    return f    

num = int(input("enter a number: "))

# function call
factorial = fact(num)
print("factorial = ", factorial)