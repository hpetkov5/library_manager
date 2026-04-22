"""
This module contains the all Library Manager functionalities.
"""


class Book:
    """
    Class Book
    """

    def __init__(self, title: str, author: str, category: str):
        self._title = title
        self._author = author
        self._category = category
        self._is_available = True

    @property
    def set_title(self) -> str:
        return self._title

    @property
    def set_author(self) -> str:
        return self._author

    @property
    def set_category(self) -> str:
        return self._category

    @property
    def set_is_avalable(self) -> bool:
        return self._is_available
