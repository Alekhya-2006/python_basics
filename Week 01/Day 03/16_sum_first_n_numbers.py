n = int(input("enter number: "))

sum = 0

for i in range(1, n + 1):
    sum += i

print(f'The sum of first {n} numbers is {sum}')