'''

Python code that incorporates all the OOP concepts (Class/Object, Encapsulation, Inheritance, Polymorphism, and Abstraction).
The code is simple, with comments explaining where and how each concept is used.

'''

from abc import ABC, abstractmethod  # Import for Abstraction

# **1. Class and Object**
# Base class representing a person
class Person:
    def __init__(self, name, email):
        self.name = name  # Public attribute
        self.email = email  # Public attribute

    def display_details(self):
        """Method to display person details."""
        print(f"Name: {self.name}, Email: {self.email}")


# **2. Encapsulation**
# Class for a library user, inheriting from Person
class LibraryUser(Person):
    def __init__(self, name, email):
        super().__init__(name, email)  # Inherit name and email from Person
        self.__borrowed_books = []  # Private attribute for borrowed books

    def borrow_book(self, book):
        """Method to borrow a book."""
        self.__borrowed_books.append(book)  # Update private attribute
        print(f"{self.name} borrowed {book}")

    def return_book(self, book):
        """Method to return a book."""
        if book in self.__borrowed_books:
            self.__borrowed_books.remove(book)
            print(f"{self.name} returned {book}")
        else:
            print(f"{self.name} does not have {book}")

    def display_borrowed_books(self):
        """Method to display borrowed books."""
        print(f"Borrowed books by {self.name}: {self.__borrowed_books}")


# **3. Inheritance**
# Subclass of LibraryUser for Librarian
class Librarian(LibraryUser):
    def __init__(self, name, email, employee_id):
        super().__init__(name, email)  # Inherit properties from LibraryUser
        self.employee_id = employee_id  # Additional attribute for Librarian

    def add_book(self, book, library):
        """Method for librarian to add a book to the library."""
        library.add_book(book)
        print(f"{self.name} added {book} to the library.")


# **4. Polymorphism**
# Base class for library items
class LibraryItem(ABC):  # Abstract base class (Abstraction)
    @abstractmethod
    def display_info(self):
        """Abstract method to display item info."""
        pass


class Book(LibraryItem):
    def __init__(self, title, author):
        self.title = title
        self.author = author

    def display_info(self):
        """Overridden method to display book info."""
        print(f"Book Title: {self.title}, Author: {self.author}")


class DVD(LibraryItem):
    def __init__(self, title, duration):
        self.title = title
        self.duration = duration

    def display_info(self):
        """Overridden method to display DVD info."""
        print(f"DVD Title: {self.title}, Duration: {self.duration} minutes")


# Library class to manage books and DVDs
class Library:
    def __init__(self):
        self.items = []  # List to hold all items in the library

    def add_book(self, item):
        """Method to add an item to the library."""
        self.items.append(item)

    def display_all_items(self):
        """Method to display all library items."""
        for item in self.items:
            # Demonstrating Polymorphism: Different display methods for Books and DVDs
            item.display_info()


# **Using All Concepts Together**
# Create a library
library = Library()

# Create some items
book1 = Book("1984", "George Orwell")
book2 = Book("To Kill a Mockingbird", "Harper Lee")
dvd1 = DVD("Inception", 148)

# Add items to the library
library.add_book(book1)
library.add_book(book2)
library.add_book(dvd1)

# Create a librarian
librarian = Librarian("Alice", "alice@example.com", "LIB123")

# Librarian adds a book
librarian.add_book(Book("The Great Gatsby", "F. Scott Fitzgerald"), library)

# Display all library items
print("\nLibrary Items:")
library.display_all_items()

# Create a library user
user = LibraryUser("Bob", "bob@example.com")

# User borrows and returns books
user.borrow_book("1984")
user.borrow_book("To Kill a Mockingbird")
user.display_borrowed_books()
user.return_book("1984")
user.display_borrowed_books()

# Abstraction in action: Display info for different library items
print("\nDetailed Item Info:")
for item in library.items:
    item.display_info()
