# return the count of the digits in a number

def digits(num):

    count = 0

    while num > 0:
        count += 1
        num = num // 10
        
    return count    

n = int(input("enter a number: "))

print(digits(n))