# Program 04: user enters a string containing a number.
# Then convert into an integer, a float, a string again.

val = input("Enter a number: ")
print(val, type(val))

val = int(val)
print(val, type(val))

val = float(val)
print(val, type(val))

val = str(val)
print(val, type(val))