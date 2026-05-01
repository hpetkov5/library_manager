'''
Unit tests for User class.

This module uses Python's unittest framework to validate the correctness of User's methods.
'''

import unittest
from library_manager.book import Book
from library_manager.users import User, UserReachedBorrowLimitException
from library_manager.users import UserAlreadyBorrowedBookException


class TestUsers(unittest.TestCase):
    """Test class defining the test cases to confirm validation of User class"""

    def test_valid_user_creation(self):
        """Test instance creation of User class"""
        test_user = User("Ivan")
        expected_result = "Ivan"
        actual_result = test_user.name
        self.assertEqual(expected_result, actual_result)

    def test_book_changed_state_after_user_borrow_book_success(self):
        """Test when user borrows book the availability state is changed"""
        test_user = User("Ivan")
        test_book = Book("Six of Crows", "Leigh Bardugo", "Fantasy")

        test_user.user_borrow_book(test_book)

        self.assertFalse(test_book.is_avalable)

    def test_book_is_recorded_in_borrowed_list_after_user_borrow_book_success(self):
        """Test when user borrows book the book is recorded in borrow list"""
        test_user = User("Ivan")
        test_book = Book("Six of Crows", "Leigh Bardugo", "Fantasy")

        test_user.user_borrow_book(test_book)

        expected_result = 1
        actual_result = len(test_user._borrowed_books)
        self.assertEqual(expected_result, actual_result)

    def test_user_borrow_limit_exceeded_raises_error(self):
        """Test when user exceeded borrow limit an error is raised"""
        test_user = User("Ivan")
        test_book = [Book(f"Title{i}", f"Author{i}", f"Category{i}") for i in range(3)]

        for book in test_book:
            test_user.user_borrow_book(book)

        with self.assertRaises(UserReachedBorrowLimitException):
            test_user.user_borrow_book(Book("Title4", "Author4", "Category4"))

    def test_user_borrow_book_twise_rases_error(self):
        """Test when user borrows the same book twice an error is raised"""
        test_user = User("Ivan")
        test_book = Book("Six of Crows", "Leigh Bardugo", "Fantasy")

        test_user.user_borrow_book(test_book)

        with self.assertRaises(UserAlreadyBorrowedBookException):
            test_user.user_borrow_book(test_book)

    def test_book_is_available_after_user_return_book_success(self):
        """Test when user returns book the availability state is True"""
        test_user = User("Ivan")
        test_book = Book("Six of Crows", "Leigh Bardugo", "Fantasy")

        test_user.user_borrow_book(test_book)
        test_user.user_return_book(test_book)

        self.assertTrue(test_book.is_avalable)


if __name__ == '__main__':
    unittest.main()
