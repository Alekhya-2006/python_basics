age = int(input("Enter your age: "))

if age > 0 and age < 13:
    print("child")
elif age >= 13 and age <= 18:
    print("Teenage")
elif age > 18:
    print("adult")
else:
    print("Please enter a valid age")            