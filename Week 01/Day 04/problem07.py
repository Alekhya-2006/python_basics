# reverse number function:

def reverse(n):
    r = 0
    while n > 0:
        digit = n % 10
        r = (r * 10) + digit
        n = n // 10

    return r  

num = int(input("enter a number: "))
print(reverse(num))