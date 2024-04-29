class Book:
    def __init__(self, title, author, genre):
        
        # Initialize attributes
        self.title = title 
        self.author = author  
        self.genre = genre  

    def display_info(self):
       
        print(f"Title: {self.title}")  
        print(f"Author: {self.author}")  
        print(f"Genre: {self.genre}")  


# Creating an instance of Book
my_book = Book("To Kill a Mockingbird", "Harper Lee", "Fiction")
my_book.display_info()
