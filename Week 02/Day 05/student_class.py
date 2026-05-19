# Student Class
# Concepts: class attributes, instance attributes, instance methods

class Student:
    college = "BDC"
    
    def __init__(self, name , age):
        self.name = name
        self.age = age
        

    def get_info(self):
        print(f'Age of {self.name} is {self.age} and studying in {self.college}')

s1 = Student("Alekhya", 20)        

s1.get_info()