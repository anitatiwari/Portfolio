import unittest
from book import Book  # Import the Book class from Book.py

class TestBook(unittest.TestCase):
    def test_display_info(self):
        # Create an instance of Book
        my_book = Book("To Kill a Mockingbird", "Harper Lee", "Fiction")

        # Redirect stdout to capture printed output
        import io
        import sys
        captured_output = io.StringIO()
        sys.stdout = captured_output

        # Call display_info method
        my_book.display_info()

        # Reset stdout
        sys.stdout = sys.__stdout__

        # Get the printed output
        printed_output = captured_output.getvalue()

        # Check if the output matches expected
        expected_output = "Title: To Kill a Mockingbird\nAuthor: Harper Lee\nGenre: Fiction\n"
        self.assertEqual(printed_output, expected_output)

if __name__ == '__main__':
    unittest.main()
