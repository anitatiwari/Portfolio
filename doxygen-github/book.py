class Book:
    def __init__(self, title, author, genre):
        """
        Constructor for the Book class.

        :param title: The title of the book.
        :type title: str
        :param author: The author of the book.
        :type author: str
        :param genre: The genre of the book.
        :type genre: str
        """
        # Initialize attributes
        self.title = title 
        self.author = author  
        self.genre = genre  

    def display_info(self):
        """
        Display information about the book.
        """
        print(f"Title: {self.title}")  
        print(f"Author: {self.author}")  
        print(f"Genre: {self.genre}")  


# Creating an instance of Book
my_book = Book("To Kill a Mockingbird", "Harper Lee", "Fiction")
my_book.display_info()
