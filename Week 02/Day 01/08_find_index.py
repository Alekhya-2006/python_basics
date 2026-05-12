nums = [1, 4, 5, 34, 2, 7]
x = int(input("enter the number: "))

idx = 0
found = False

for i in nums:

    if(i == x):
        print(f'{x} found at idx = {idx}')
        found = True
        break
    idx += 1    

if not found:
    print("number not found")