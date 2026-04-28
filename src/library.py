"""This module defines Library class and the corresponding attributes and methods"""

from src.book import Book
from src.users import User


class BookAlreadyExistInLibraryException(Exception):
    """Rases an error when librarian tries to add a book which already exists"""
    pass


class UserAlreadyExistInLibraryException(Exception):
    """Rases an error when librarian tries to add a user which already exists"""
    pass


class Library():
    """Represents a Library that manages Users and Books"""

    def __init__(self):
        self._books = []
        self._users = []

    def add_new_book(self, book: Book) -> None:
        """Adds new book in library"""

        if book in self._books:
            raise BookAlreadyExistInLibraryException("The Book already exists in the library")

        self._books.append(book)

    def add_new_user(self, user: User) -> None:
        """Adds new user in library"""

        if user in self._users:
            raise UserAlreadyExistInLibraryException("The User already exists in the library")

        self._users.append(user)
