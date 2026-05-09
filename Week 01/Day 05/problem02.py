# function to print all even numbers between two input numbers

def evenNumbers(a, b):

    for i in range(a, b+1):
        
        if i % 2 == 0:
            print(i)
        
n1 = int(input("Enter 1st number: "))
n2 = int(input("enter 2nd number: ")) 

evenNumbers(n1, n2)