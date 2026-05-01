# Library Management System

## Overview

This project implements a simple **object-oriented Library Management System** in Python.

It demonstrates:
- Encapsulation
- Inheritance
- Separation of concerns
- Validation and error handling

The system allows users to **borrow and return books**, while the library manages books and users.

---

## Features

### Books
- Each book has:
  - Title
  - Author
  - Category
  - Availability status
- Books can be borrowed and returned
- Prevents borrowing already borrowed books

### Users
- Users can borrow multiple books
- Borrow limit enforced (default: 3 books)
- Users can view borrowed books
- Prevents invalid actions (duplicate borrow, invalid return)

### Library
- Stores books and users
- Register new users
- Add new books
- List available books
- Search by author or category

### Testing
- Unit tests
- Covers:
  - Valid flows
  - Edge cases
  - Error scenarios

---

## Project Structure
library_manager/
    ├───src/
    │    └──library_manager/
    │       ├── __init__.py
    │       ├── book.py
    │       ├── user.py
    │       └── library.py
    └── tests/
        ├── test_book.py
        ├── test_users.py
        └── test_library.py


## Installation

### Requirements
- Python 3.11 or higher

### Install locally

Clone the repository and install the package.
```bash
python -m library_manager
```