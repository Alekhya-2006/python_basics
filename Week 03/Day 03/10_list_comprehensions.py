# List Comprehensions: 
# [output for item in iterable if condition]

# odd squares
sq = [i * i for i in range(1, 6) if (i % 2 != 0)]
print(sq)

# Using loop
squares = []

for i in range(1, 6):
    squares.append(i ** 2)

print(squares)    
