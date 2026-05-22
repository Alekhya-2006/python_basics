# Constructor OverLoading
# Create a class Person thet allows the constructor to work with:
# name only
# name + age
# name + age + address
# as direct contructor overloading(multiple constructors) are not allowed 
# but we haev to use default parameters to simulte contructor overloading

class Person:

    def __init__(self, name, age=None, address=None):

        self.name = name
        self.age = age
        self.address = address


    def display(self):

        print(
            f"\nName = {self.name}"
            f"\nAge = {self.age if self.age is not None else 'Not Provided'}"
            f"\nAddress = {self.address if self.address is not None else 'Not Provided'}"
        )


p1 = Person("Alekhya")

p2 = Person("Alekhya",20)

p3 = Person("Alekhya",20,"Hyderabad")

p1.display()
p2.display()
p3.display()