# Task 0: Dive into Python Magic Methods
# File: book_class.py

class Book:
    # This is the constructor method. It initializes a new Book object.
    def __init__(self, title, author, year):
        self.title = title
        self.author = author
        self.year = year

    # This is the destructor method. It runs when the object is deleted.
    def __del__(self):
        print(f"Deleting {self.title}")

    # This is the string representation method.
    # It returns a human-readable string for the object.
    def __str__(self):
        return f"{self.title} by {self.author}, published in {self.year}"

    # This is the official representation method.
    # It returns a string that can recreate the object.
    def __repr__(self):
        return f"Book('{self.title}', '{self.author}', {self.year})"