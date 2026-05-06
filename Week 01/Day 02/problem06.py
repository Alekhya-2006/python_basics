# Triangle validity checker

a1 = int(input("enter 1st angle: "))
a2 = int(input("enter 2nd angle: "))
a3 = int(input("enter 3rd angle: "))

if(a1 + a2 + a3 == 180):
    if(a1 == a2 == a3):
        print("Equilateral Triangle")
    elif(a1 != a2 and a2 != a3 and a3 != a1):
        print("Scalene Triangle")
    else:
        print("Isosceles Triangle")
else:
    print("Invalid")                