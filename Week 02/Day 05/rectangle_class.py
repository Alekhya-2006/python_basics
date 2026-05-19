# Rectangle Class
# Concepts: Constructor, Instance methods

class Rectangle:
    def __init__(self, length, width):
        self.length = length
        self.width = width

    def get_area(self):
        return self.length * self.width
        

    def get_perimeter(self):
        return 2 * (self.length + self.width)    
        
while True: 

    print("\n1. area")
    print("2. perimeter")
    print("3. Exit")

    n = int(input("choose option (1 - 3): "))
    
    if n == 3:
        print("Successfully exited") 
        break
     
    if n > 0 and n <= 2:
        
        length = int(input("Enter the length of the Rectangle: "))
        width = int(input("Enter width of the Rectangle: "))
        rect = Rectangle(length, width)

        if n == 1:
            print(rect.get_area())

        elif n == 2:
            print(rect.get_perimeter())

    else:
        print("Invalid Choice")
        break       