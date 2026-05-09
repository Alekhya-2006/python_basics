# fuction that returns true if n is a prime number and False otherwise

def is_prime(n):

    if n < 2 :
        return False
    
    for i in range(2, n):

        if n % i == 0:
            return False

    return True
        
num = int(input("enter a number: ")) 

print(is_prime(num))