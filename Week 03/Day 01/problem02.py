# Function Overriding
# Create a class Shape with method area()
# Create subclasses Circle, Rectangle, and Triangle the override the area() method

class Shape:
    def area(self):
        print("Not yet Decided")

class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return 3.14 * self.radius * self.radius    

class Rectangle(Shape):
    def __init__(self, length, breadth):
        self.length = length
        self.breadth = breadth

    def area(self):
        return self.length * self.breadth

class Triangle(Shape):
    def __init__(self, base, height):
        self.base = base
        self. height = height

    def area(self):
        return 1/2 * self.base * self.height
    
c1 = Circle(4)
print(f'Area of the Circle = {c1.area()}')

r1 = Rectangle(4, 3)
print(f'Area of the Rectangle = {r1.area()}')

t1 = Triangle(6, 4)
print(f'Area of the Triangle = {t1.area()}')