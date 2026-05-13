# largest element

t = (3, 5, 67, 89, 2, 4, 10)
# print(max(t))

largest = t[0]

for i in t:
    if largest < i:
        largest = i

print("largest num =", largest)