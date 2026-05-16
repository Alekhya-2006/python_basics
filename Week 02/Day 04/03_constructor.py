# __init__Method: to initialize our object
# self parameter: current instance of the class

class Student:
    def __init__(self, name, age): # parameterized
        self.name = name
        self.age = age


stu1 = Student("Alekhya", 20)
stu2 = Student("Tanuja", 19)
stu3 = Student("Teena", 21)

print(stu1.name)
print(stu2.name, stu2.age)
print(stu3.name)