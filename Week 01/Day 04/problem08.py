# Sum of digits function

def sum_digits(n):
    s = 0

    while n > 0:
        digit = n % 10
        s += digit
        n = n // 10

    return s

num = int(input("enter a number: "))

total = sum_digits(num)

print(f'Sum of digits of {num} is {total}')