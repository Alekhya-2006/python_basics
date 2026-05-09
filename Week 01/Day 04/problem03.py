# largest of Two numbers

def largest(x, y):
    if x > y:
        return x 
    elif x < y:
        return y
    else:
        return "equal"
    
a = int(input("enter 1st number: "))
b = int(input("enter 2nd number: "))

print(largest(a, b))