# Student Encapsulation System:
# Concepts: Private Attributes, Getters, Setters, Validation

class Student:

    def __init__(self, name, roll_no, marks):

        self.__name = name
        self.__roll_no = roll_no
        self.__marks = marks


    # Getters

    def get_name(self):

        if len(self.__name) == 0:
            return "Name cannot be empty"

        return self.__name


    def get_roll_no(self):

        if 1 <= self.__roll_no <= 100:
            return self.__roll_no

        return "Roll number must be between 1 and 100"


    def get_marks(self):

        if 0 <= self.__marks <= 100:
            return self.__marks

        return "Marks must be between 0 and 100"


    # Setters with validation

    def set_name(self, new_name):

        if len(new_name) > 0:
            self.__name = new_name


    def set_roll_no(self, new_roll_no):

        if 1 <= new_roll_no <= 100:
            self.__roll_no = new_roll_no


    def set_marks(self, new_marks):

        if 0 <= new_marks <= 100:
            self.__marks = new_marks


    # Display

    def display_details(self):

        print(
            f"\nName = {self.get_name()}"
            f"\nRoll No = {self.get_roll_no()}"
            f"\nMarks = {self.get_marks()}"
        )


# Object

s1 = Student("Tanuja", 120, -90)

s1.display_details()


# Update values

s1.set_name("Alekhya")
s1.set_roll_no(12)
s1.set_marks(89)

s1.display_details()