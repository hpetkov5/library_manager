"""
This module contains simple OO system for managing books, users, and book loans in a library
"""


class Book:
    """Module defining atributes and behaviour of Book objects."""

    def __init__(self, title: str, author: str, category: str):
        self._title = title
        self._author = author
        self._category = category
        self._is_available = True

    @property
    def title(self) -> str:
        """Title of the book."""
        return self._title

    @property
    def author(self) -> str:
        """Author of the book."""
        return self._author

    @property
    def category(self) -> str:
        """Category of the book."""
        return self._category

    @property
    def is_avalable(self) -> bool:
        """Availability of the book."""
        return self._is_available

    def borrow_book(self) -> None:
        """
        Changes _is_available attribute to False, if book is available.
        Otherwise, raises a RuntimeError.
        """
        if not self._is_available:
            raise RuntimeError(f"{self._title} is not available.")

        self._is_available = False

    def retunn_book(self) -> None:
        """Changes _is_available attribute to True"""
        self._is_available = True


class User:
    """Module defining atributes and behaviour of User objects."""

    def __init__(self, name: str):
        self._name = name
        self._borrowed_books = []

    @property
    def name(self) -> str:
        """Name of user."""
        return self._name
