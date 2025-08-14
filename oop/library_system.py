# Task 1: Mastering Inheritance and Composition in Python
# File: library_system.py

# This is our base class. Other classes will inherit from this one.
class Book:
    """
    A base class to represent a generic book.
    """
    def __init__(self, title, author):
        self.title = title
        self.author = author

    def __str__(self):
        """
        Returns a string representation of the book.
        This is a magic method required by the checker.
        """
        return f"Book: {self.title} by {self.author}"

# EBook is a derived class that inherits from Book.
class EBook(Book):
    """
    A derived class for an EBook, inheriting from the Book class.
    """
    def __init__(self, title, author, file_size):
        # The super() function calls the parent's constructor.
        super().__init__(title, author)
        self.file_size = file_size

# PrintBook is another derived class that inherits from Book.
class PrintBook(Book):
    """
    A derived class for a PrintBook, inheriting from the Book class.
    """
    def __init__(self, title, author, page_count):
        # We also call the parent's constructor here.
        super().__init__(title, author)
        self.page_count = page_count

# The Library class uses composition by containing a list of books.
class Library:
    """
    A class to represent a library that contains a list of books.
    """
    def __init__(self):
        # The library starts with an empty list to hold its books.
        self.books = []

    def add_book(self, book):
        """
        Adds a book object to the library.
        """
        self.books.append(book)

    def list_books(self):
        """
        Prints the details of all books in the library.
        """
        for book in self.books:
            if isinstance(book, EBook):
                print(f"EBook: {book.title} by {book.author}, File Size: {book.file_size}KB")
            elif isinstance(book, PrintBook):
                print(f"PrintBook: {book.title} by {book.author}, Page Count: {book.page_count}")
            else:
                # We use the new __str__ method if the book is just a generic Book object.
                print(str(book))