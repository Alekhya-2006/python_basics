class Student:
    college_name = "BDC"  # class attribute

    def __init__(self, name, marks):
        self.name = name # instance attributes
        self.marks = marks

stu1 = Student("Alekhya", 542)

print(stu1.name)
print(stu1.college_name)
# print(Student.college_name)