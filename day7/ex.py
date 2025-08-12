# a class for a single book
class Book:
    """
    this class is for books in a library.
    """

    # this makes a new book object
    def __init__(self, t, a):
        # these are the book's variables
        self.t = t  # t stands for title
        self.a = a  # a stands for author
        self.status = "available"  # is the book on the shelf?

    # this is how you print the book info
    def __str__(self):
        return "{} by {}. status: {}".format(self.t, self.a, self.status)

# a class for the whole library
class Library:
    """
    this class manages the books.
    """
    # a list to hold all the books
    all_books = []

    # a function to put a book in the library
    def add_book(self, book_obj):
        self.all_books.append(book_obj)
        print("added {} to the library!".format(book_obj.t))

    # a function to check out a book
    def borrow_book(self, title):
        for b in self.all_books:
            if b.t == title and b.status == "available":
                b.status = "borrowed"
                print("you got the book '{}'!".format(b.t))
                return
        print("sorry, that book is not here or already checked out.")

    # a function to bring a book back
    def return_book(self, title):
        for b in self.all_books:
            if b.t == title and b.status == "borrowed":
                b.status = "available"
                print("you returned '{}'. thanks!".format(b.t))
                return
        print("i don't think you borrowed that book from us.")

    # a function to show all the books
    def show_books(self):
        print("\n--- all books in the library ---")
        if not self.all_books:
            print("no books right now.")
            return

        for b in self.all_books:
            print(b)
        print("----------------------------------\n")

# ----------------------------------------
# this is where the program starts

# make a library object
my_library = Library()

# make some book objects
book1 = Book("The Hobbit", "J.R.R. Tolkien")
book2 = Book("Harry Potter", "J.K. Rowling")
book3 = Book("The Lion, the Witch and the Wardrobe", "C.S. Lewis")

# put the books in the library
my_library.add_book(book1)
my_library.add_book(book2)
my_library.add_book(book3)

# show the books
my_library.show_books()

# try to borrow a book
my_library.borrow_book("Harry Potter")

# show the books again to see the change
my_library.show_books()

# try to borrow the same book again (it won't work)
my_library.borrow_book("Harry Potter")

# return a book
my_library.return_book("Harry Potter")

# show the books one last time
my_library.show_books()
