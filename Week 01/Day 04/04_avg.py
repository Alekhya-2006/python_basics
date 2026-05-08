# function definition
def avg(a, b, c):
    average = (a + b + c) / 3
    return average

n1 = int(input("enter 1st number: "))
n2 = int(input("enter 2nd number: "))
n3 = int(input("enter 3rd number: "))

# function call 
ans = avg(n1, n2, n3)
print(ans)