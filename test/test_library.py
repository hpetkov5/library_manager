'''
Unit tests for Library class.

This module uses Python's unittest framework to validate the correctness of Library's methods.
'''

import unittest
from library_manager.book import Book
from library_manager.users import User
from library_manager.library import Library
from library_manager.library import UserAlreadyExistInLibraryException
from library_manager.library import BookAlreadyExistInLibraryException

class TestLibrary(unittest.TestCase):
    """Test class defining the test cases to confirm validation of Library class"""

    def test_add_new_book_success(self):
        """Test add new book to library"""

        test_library = Library("Test")
        test_book = Book("Six of Crows", "Leigh Bardugo", "Fantasy")

        test_library.add_new_book(test_book)

        expected_result = 1
        actual_result = len(test_library._books)
        self.assertEqual(expected_result, actual_result)

    def test_add_new_book_twice_raises_error(self):
        """Test add new book twice to library raises error"""

        test_library = Library("Test")
        test_book = Book("Six of Crows", "Leigh Bardugo", "Fantasy")

        test_library.add_new_book(test_book)

        with self.assertRaises(BookAlreadyExistInLibraryException):
            test_library.add_new_book(test_book)

    def test_add_new_user_success(self):
        """Test add new user to library"""

        test_library = Library("Test")
        test_user = User("Ivan")

        test_library.add_new_user(test_user)

        expected_result = 1
        actual_result = len(test_library._users)
        self.assertEqual(expected_result, actual_result)

    def test_add_existing_user_raises_error(self):
        """Test add user twice to library raises error"""

        test_library = Library("Test")
        test_user = User("Ivan")

        test_library.add_new_user(test_user)

        with self.assertRaises(UserAlreadyExistInLibraryException):
            test_library.add_new_user(test_user)

    def test_list_available_books(self):
        """Test list available books to borrow"""
        test_library = Library("Test")
        test_book = Book("Six of Crows", "Leigh Bardugo", "Fantasy")

        test_library.add_new_book(test_book)

        expected_result = [test_book]
        actual_result = test_library.list_available_books()
        self.assertEqual(expected_result, actual_result)

    def test_search_by_author(self):
        """Test search by author"""
        test_library = Library("Test")
        test_book = Book("Six of Crows", "Leigh Bardugo", "Fantasy")

        test_library.add_new_book(test_book)

        expected_result = 1
        actual_result = len(test_library.search_by_author("Leigh Bardugo"))
        self.assertEqual(expected_result, actual_result)

    def test_search_by_category(self):
        """Test search by category"""
        test_library = Library("Test")
        test_book = Book("Six of Crows", "Leigh Bardugo", "Fantasy")

        test_library.add_new_book(test_book)

        expected_result = 1
        actual_result = len(test_library.search_by_category("Fantasy"))
        self.assertEqual(expected_result, actual_result)


if __name__ == '__main__':
    unittest.main()
