'''
Unit tests for Book class.

This module uses Python's unittest framework to validate the correctness of Book's methods.
'''

import unittest
from src.book import Book, BookNotAvailableException


class TestBook(unittest.TestCase):
    """Test class defining the test cases to confirm validation of Book class"""

    def test_valid_creation_book_title(self):
        """Test instance creation of Book class - title"""
        test_book = Book("Six of Crows", "Leigh Bardugo", "Fantasy")
        expected_result = test_book.title
        actual_result = "Six of Crows"
        self.assertEqual(expected_result,actual_result)

    def test_valid_creation_book_availability(self):
        """Test instance creation of Book class - availability"""
        test_book = Book("Six of Crows", "Leigh Bardugo", "Fantasy")
        self.assertTrue(test_book.is_avalable)

    def test_successful_book_borrow(self):
        """Test book changes availability status when borrow method is called"""
        test_book = Book("Six of Crows", "Leigh Bardugo", "Fantasy")
        test_book.borrow_book()
        self.assertFalse(test_book.is_avalable)

    def test_borrow_book_twice_rases_error(self):
        """Test borrow is raises an error when book is borrowed twice"""
        test_book = Book("Six of Crows", "Leigh Bardugo", "Fantasy")
        test_book.borrow_book()

        with self.assertRaises(BookNotAvailableException):
            test_book.borrow_book()

    def test_return_book_is_successful(self):
        """Test return book is successful after book is borrowed"""
        test_book = Book("Six of Crows", "Leigh Bardugo", "Fantasy")
        test_book.borrow_book()
        test_book.return_book()
        self.assertTrue(test_book.is_avalable)
