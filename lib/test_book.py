import unittest
from book import Book

class TestBook(unittest.TestCase):
    def test_book_creation(self):
        book = Book("Python Basics", "John Smith", 200)
        self.assertEqual(book.title, "Python Basics")
        self.assertEqual(book.author, "John Smith")
        self.assertEqual(book.pages, 200)
        self.assertFalse(book.is_open)

    def test_open_close_book(self):
        book = Book("Python Basics", "John Smith", 200)
        book.open()
        self.assertTrue(book.is_open)
        book.close()
        self.assertFalse(book.is_open)

    def test_read_book(self):
        book = Book("Python Basics", "John Smith", 200)
        book.open()
        self.assertTrue(book.is_open)
        
        # Capture the print output to check what's printed
        from io import StringIO
        import sys
        original_stdout = sys.stdout
        sys.stdout = StringIO()
        
        book.read(10)
        
        output = sys.stdout.getvalue()
        sys.stdout = original_stdout
        
        self.assertIn("Reading page 10 of 'Python Basics'.", output)

    def test_read_closed_book(self):
        book = Book("Python Basics", "John Smith", 200)
        book.close()
        self.assertFalse(book.is_open)
        
        # Capture the print output to check what's printed
        from io import StringIO
        import sys
        original_stdout = sys.stdout
        sys.stdout = StringIO()
        
        book.read(10)
        
        output = sys.stdout.getvalue()
        sys.stdout = original_stdout
        
        self.assertIn("Please open the book 'Python Basics' to read.", output)

    def test_has_title_and_page_count(self):
        '''has the title and page_count passed into __init__, and values can be set to new instance.'''
        book = Book("And Then There Were None", "Agatha Christie", 272)
        self.assertEqual(book.title, "And Then There Were None")
        self.assertEqual(book.author, "Agatha Christie")
        self.assertEqual(book.pages, 272)

if __name__ == '__main__':
    unittest.main()
