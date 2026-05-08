n1 = int(input("enter 1st number: "))
n2 = int(input("enter 2nd number: "))
n3 = int(input("enter 3rd number: "))

sum = lambda a, b, c: a + b + c
print("The sum of the given numbers is ", sum(n1, n2,n3))

avg = lambda a, b, c: (a + b + c) / 3 
print("The average of the given numbers is", avg(n1, n2, n3))