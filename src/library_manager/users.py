"""This module defines User class and the corresponding attributes and methods"""

from library_manager.book import Book

class UserReachedBorrowLimitException(Exception):
    """Raise error when a user tries to borrow a book but have reached the borrow limit"""
    pass


class UserAlreadyBorrowedBookException(Exception):
    """Raise error when a user tries to borrow a book they already borrowed."""
    pass


class User:
    """Module defining atributes and behaviour of User objects."""

    MAX_ALLOWED_BOOKS = 3

    def __init__(self, name: str):
        self._name = name
        self._borrowed_books = []

    @property
    def name(self) -> str:
        """
        Name of user.
        :return name of user
        """
        return self._name

    def can_borrow_book(self) -> bool:
        """
        Verifies if user has reached the borrow limit
        :return if user can borrow book
        """
        return len(self._borrowed_books) < self.MAX_ALLOWED_BOOKS

    def user_borrow_book(self, book: Book) -> None:
        """
        Function adds book to borrow list and changes availability state.
        :param book: Book to be added to borrow list.
        """
        if not self.can_borrow_book():
            raise UserReachedBorrowLimitException("User reached borrow limit")

        if book in self._borrowed_books:
            raise UserAlreadyBorrowedBookException("User has alredy borrowed the book.")

        book.borrow_book()
        self._borrowed_books.append(book)

    def user_return_book(self, book: Book) -> None:
        """
        Function removes book from borrow list and changes availability state.
        :param book: Book to be removed from borrow list.
        """
        book.return_book()
        self._borrowed_books.remove(book)
