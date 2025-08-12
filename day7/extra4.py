# =======================================================
# Exercise 4: Library System
# =======================================================
print("--- Exercise 4: Library System ---")

class Book:
    """A class to represent a book with a title, author, and ISBN."""
    def __init__(self, title, author, isbn):
        self.title = title
        self.author = author
        self.isbn = isbn

    def display_info(self):
        # Returns a formatted string with the book's details.
        return f"Title: {self.title}, Author: {self.author}, ISBN: {self.isbn}"

class Library:
    """A class to manage a collection of books."""
    def __init__(self):
        self.books = []

    def add_book(self, book):
        # Adds a Book object to the list.
        self.books.append(book)
        print(f"Book '{book.title}' added to the library.")

    def remove_book(self, isbn):
        # Removes a book from the list by its ISBN.
        for book in self.books:
            if book.isbn == isbn:
                self.books.remove(book)
                print(f"Book with ISBN '{isbn}' removed.")
                return
        print(f"Book with ISBN '{isbn}' not found.")

    def list_books(self):
        # Returns a list of strings, each containing the info of a book.
        if not self.books:
            return ["No books in the library."]
        return [book.display_info() for book in self.books]

# Create a library and some book objects.
my_library = Library()
book1 = Book("The Hitchhiker's Guide", "Douglas Adams", "978-0345391803")
book2 = Book("Dune", "Frank Herbert", "978-0441172719")

my_library.add_book(book1)
my_library.add_book(book2)
print("\nCurrent library books:")
for info in my_library.list_books():
    print(info)

my_library.remove_book("978-0345391803")
print("\nAfter removing a book:")
for info in my_library.list_books():
    print(info)
print("-" * 50 + "\n")