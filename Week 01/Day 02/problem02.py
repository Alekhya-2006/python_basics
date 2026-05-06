# Largest of Two numbers

n1 = int(input("Enter 1st number: "))
n2 = int(input("Enter 2nd number: "))

if(n1 > n2):
    print(f'The largest number among {n1} and {n2} is {n1}')
elif(n1 < n2): 
    print(f'The largest number among {n1} and {n2} is {n2}')
else:
    print("Both are equal")        