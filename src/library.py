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

    def __init__(self, name: str):
        self._name = name
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

    def list_available_books(self) -> list:
        """
        Shows the available for borrow books in the library
        :return list of available books
        """
        return [book for book in self._books if book.is_available]

    def search_by_author(self, author) -> list:
        """
        Shows books based on the provided author.
        :return list of books by the provided author
        """

        return [book for book in self._books if book.author == author]

    def search_by_category(self, category) -> list:
        """
        Shows books based on the provided category.
        :return list of books by the provided category
        """

        return [book for book in self._books if book.category == category]
