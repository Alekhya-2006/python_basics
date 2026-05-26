try:
    x = int(input("enter x: "))
    ans = 10/x

except ZeroDivisionError:
    print("Division by zero is not allowed")

except ValueError:
    print("Please enter a valid number")
else:
    print(f'ans = {ans}')

finally:
    print("End of program")    