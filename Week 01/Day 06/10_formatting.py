a = 4
b = 11
sum = a + b

# normal formatting
print("sum is {}".format(sum)) 
print("sum of {} and {} is {}".format(a, b, sum))

print("language is {}".format("python"))

# index based formatting
print("sum of {1} and {0} is {2}".format(a, b, sum))

# value based formatting
print("sum of {a} and {b} is {sum} ".format(a = 5, b = 10, sum = a + b))