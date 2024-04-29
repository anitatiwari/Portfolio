class Book:
    def __init__(self, title, author, genre):
        self.title = title
        self.author = author
        self.genre = genre

    def __str__(self):
        return f"{self.title} by {self.author}, Genre: {self.genre}"

class Bookstore:
    def __init__(self, name, books):
        self.name = name
        self.books = books

    def search_book(self, title):
        for book in self.books:
            if book.title == title:
                return book
        return None

    def get_book(self, title):
        book = self.search_book(title)
        if book:
            print(f"Book '{title}' is available at {self.name}.")
            return book
        else:
            print(f"Sorry, '{title}' is not available at {self.name}.")
            return None

# Creating some books
book1 = Book("Harry Potter and the Philosopher's Stone", "J.K. Rowling", "Fantasy")
book2 = Book("To Kill a Mockingbird", "Harper Lee", "Fiction")
book3 = Book("The Great Gatsby", "F. Scott Fitzgerald", "Classic")

# Creating a bookstore with the books
bookstore = Bookstore("My Bookstore", [book1, book2, book3])

# Get a book from the bookstore
requested_book = bookstore.get_book("To Kill a Mockingbird")

if requested_book:
    print("Book Details:")
    print(requested_book)
