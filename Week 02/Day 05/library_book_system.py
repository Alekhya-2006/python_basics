# Library Book System
# Concepts: Class Variables, Constructors, Instance Methods

class Book:
    total_books = 0

    def __init__(self, title, author):
        self.title = title
        self.author = author
        Book.total_books += 1

    def display_info(self):
        
        print(f'Title: {self.title}'
              f'\nAuthor: {self.author}\n')  
        
book1 = Book("Ask Yourself", "John Carnot")
book2 = Book("A Bad Girl", "Yasmai")        
          
book1.display_info()
book2.display_info()

print("Total Books =", Book.total_books)