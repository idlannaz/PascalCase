import unittest
from book import Book

class TestBook(unittest.TestCase):

    def test_get_info(self):
        book = Book("Author Test", "Title Test")
        self.assertEqual(book.get_info(), "Title: Title Test, Author: Author Test")

    def test_total_books(self):
        initial_count = Book.total_books()
        Book("Author Test 1", "Title Test 1")
        self.assertEqual(Book.total_books(), initial_count + 1)

    def test_is_valid_title(self):
        self.assertTrue(Book.is_valid_title("Valid Title"))
        self.assertFalse(Book.is_valid_title(""))
        self.assertFalse(Book.is_valid_title("   "))
        self.assertFalse(Book.is_valid_title(123))  # Testing non-string input

if __name__ == "__main__":
    unittest.main()
