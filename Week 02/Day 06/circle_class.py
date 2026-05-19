# Circle Class with Static Method

# Create class Circle.

# Requirements:

# Constructor takes radius
# Method to calculate area
# Static method to return value of π (3.14)

# Concepts:

# Constructor
# Instance methods
# Static methods

class Circle:

    def __init__(self, radius):
        self.radius = radius
    
    
    def calc_area(self):
        return Circle.get_pi() * self.radius * self.radius
    
    @staticmethod
    def get_pi():
        return 3.14
        
radius = int(input("Enter the radius: "))

circle = Circle(radius)

print("Area =", circle.calc_area())