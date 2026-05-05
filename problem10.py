# Program 10: input a decimal number.
# output its integer part and fractional part

num = float(input("Enter a decimal number: "))

integer_part = int(num)
fractional_part = round(num - integer_part, 3)

print("Integer part =", integer_part)
print("Fractional part =", fractional_part)