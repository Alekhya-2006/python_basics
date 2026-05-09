# prime number function

def isPrime(a):

    if a <= 1:
        return "Not Prime"

    for i in range(2, a):

        if a % i == 0:
            return "Not Prime"

    return "Prime"


n = int(input("Enter a number: "))

print(isPrime(n))