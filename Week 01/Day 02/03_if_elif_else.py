age = int(input("Enter your age: "))

if age >= 18 and age < 60:
    print("You can Vote")
    print("You can drive")

elif age > 60: 
    print("You can Vote")
    print("You are too old")
    print("so that driving yourself is not safe")

elif age > 0 and age < 18:
    print("You are under aged. So")
    print("You can't vote")
    print("You can't drive") 

else: 
    print("Invalid age")
    print("Please check")
    print("And enter correct age")     