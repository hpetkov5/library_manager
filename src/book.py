"""
This module defines Book class and the corresponding attributes and methods
"""


class BookNotAvailableException(Exception):
    """Raise error when the Book is not available to borrow"""
    pass


class Book:
    """Module defining atributes and behaviour of Book objects."""

    def __init__(self, title: str, author: str, category: str):
        self._title = title
        self._author = author
        self._category = category
        self._is_available = True

    @property
    def title(self) -> str:
        """
        Title of the book.
        :return title of the book
        """
        return self._title

    @property
    def author(self) -> str:
        """
        Author of the book.
        :return author of the book
        """
        return self._author

    @property
    def category(self) -> str:
        """
        Category of the book.
        :return category of the book
        """
        return self._category

    @property
    def is_avalable(self) -> bool:
        """
        Availability of the book.
        :return availability of the book
        """
        return self._is_available

    def borrow_book(self) -> None:
        """
        Changes _is_available attribute to False, if book is available.
        Otherwise, raises a RuntimeError.
        """
        if not self._is_available:
            raise BookNotAvailableException(f"{self._title} is not available.")

        self._is_available = False

    def return_book(self) -> None:
        """Changes _is_available attribute to True"""
        self._is_available = True
