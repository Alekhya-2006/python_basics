# add elements to set

numbers_set = set()

n = int(input("How many elements do you want to add: "))

for i in range(1, n + 1):
    element = int(input(f"Enter the {i}th element: "))
    numbers_set.add(element)

print(numbers_set)