# Task 1: Mastering Inheritance and Composition in Python
# File: library_system.py

# This is our base class. Other classes will inherit from this one.
class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author

# EBook is a derived class that inherits from Book.
class EBook(Book):
    def __init__(self, title, author, file_size):
        # The super() function calls the parent's constructor.
        super().__init__(title, author)
        self.file_size = file_size

# PrintBook is another derived class that inherits from Book.
class PrintBook(Book):
    def __init__(self, title, author, page_count):
        # We also call the parent's constructor here.
        super().__init__(title, author)
        self.page_count = page_count

# The Library class uses composition by containing a list of books.
class Library:
    def __init__(self):
        # The library starts with an empty list to hold its books.
        self.books = []

    def add_book(self, book):
        # We add a book object to the list.
        self.books.append(book)

    def list_books(self):
        # We loop through all the books and print their details.
        for book in self.books:
            if isinstance(book, EBook):
                print(f"EBook: {book.title} by {book.author}, File Size: {book.file_size}KB")
            elif isinstance(book, PrintBook):
                print(f"PrintBook: {book.title} by {book.author}, Page Count: {book.page_count}")
            else:
                print(f"Book: {book.title} by {book.author}")