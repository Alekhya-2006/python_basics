# search element in tuple

t = (4, 6, 3, 45, 87, 24, 1)

n = int(input("enter target element: "))
found = False

for i in t:
    if i == n:
        print(f'{n} exists in tuple')
        found = True
        break

if not found:
    print("Doesn't exists")