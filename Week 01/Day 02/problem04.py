# Grade calculator

marks = int(input("enter your marks(0-100): "))

if (marks > 90 and  marks < 100):
    print("Grade A")
elif (marks > 75 and marks <= 90):
    print("Grade B")
elif (marks > 50 and marks <= 75):
    print("Grade C")
elif (marks >= 35 and marks <= 50):
    print("Grade D")
elif ( marks >= 0 and marks < 35):
    print("Fail")   
else:
    print("Invalid marks")               