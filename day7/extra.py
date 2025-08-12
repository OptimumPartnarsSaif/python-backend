# =======================================================
# Exercise 1: Basic Class and Object
# =======================================================
print("--- Exercise 1: Basic Class and Object ---")

class Person:
    """A class to represent a person with a name and age."""
    def __init__(self, name, age):
        # The constructor initializes the instance variables 'name' and 'age'.
        self.name = name
        self.age = age

    def introduce(self):
        # A method that returns a greeting string.
        return f"Hello, my name is {self.name} and I am {self.age} years old."

# Create two instances of the Person class.
person1 = Person("Alice", 30)
person2 = Person("Bob", 25)

# Call the introduce() method for each instance.
print(person1.introduce())
print(person2.introduce())
print("-" * 50 + "\n")


# =======================================================
# Exercise 2: Instance vs Class Variables
# =======================================================
print("--- Exercise 2: Instance vs Class Variables ---")

class Dog:
    """A class to represent a dog."""
    # This is a class variable, shared by all instances of the Dog class.
    species = "Canis familiaris"

    def __init__(self, name, breed):
        # These are instance variables, unique to each Dog object.
        self.name = name
        self.breed = breed

    def describe(self):
        # A method that uses both instance and class variables.
        return f"{self.name} is a {self.breed}. Species: {self.species}."

# Create two Dog instances.
dog1 = Dog("Fido", "Golden Retriever")
dog2 = Dog("Buddy", "Poodle")

print(dog1.describe())
print(dog2.describe())

# Modify the class variable for one instance.
# This actually modifies the class variable for all instances.
Dog.species = "Domestic Dog"
print("\nAfter modifying the class variable:")
print(dog1.describe())
print(dog2.describe())
print("-" * 50 + "\n")


# =======================================================
# Exercise 3: Bank Account with Validation
# =======================================================
print("--- Exercise 3: Bank Account with Validation ---")

class BankAccount:
    """A class to model a bank account with deposit and withdrawal validation."""
    def __init__(self, account_holder, balance=0):
        self.account_holder = account_holder
        self.balance = balance

    def deposit(self, amount):
        # Validate that the deposit amount is positive.
        if amount > 0:
            self.balance += amount
            print(f"Deposited ${amount:.2f}. New balance: ${self.balance:.2f}")
        else:
            print("Invalid deposit amount. Must be greater than 0.")

    def withdraw(self, amount):
        # Validate that the withdrawal amount is positive and there are sufficient funds.
        if amount > 0 and self.balance >= amount:
            self.balance -= amount
            print(f"Withdrew ${amount:.2f}. New balance: ${self.balance:.2f}")
        elif amount <= 0:
            print("Invalid withdrawal amount. Must be greater than 0.")
        else:
            print("Insufficient funds. Withdrawal denied.")

    def get_balance(self):
        # Returns the current balance.
        return self.balance

# Create a bank account instance.
my_account = BankAccount("Charlie", 1000)

my_account.deposit(200)
my_account.withdraw(50)
my_account.withdraw(2000)  # This should fail.
print(f"Final balance: ${my_account.get_balance():.2f}")
print("-" * 50 + "\n")


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


# =======================================================
# Exercise 5: Class Variable Counter
# =======================================================
print("--- Exercise 5: Class Variable Counter ---")

class Car:
    """A class to count the total number of cars created."""
    # A class variable to keep track of the total number of cars.
    total_cars = 0

    def __init__(self, make, model):
        self.make = make
        self.model = model
        # Increment the class variable every time a new instance is created.
        Car.total_cars += 1

    def display_car(self):
        # A method to display the car's details.
        return f"Make: {self.make}, Model: {self.model}"

    @staticmethod
    def get_total_cars():
        # A static method to return the total number of cars.
        return Car.total_cars

# Create some Car objects.
car1 = Car("Toyota", "Camry")
car2 = Car("Honda", "Civic")
car3 = Car("Ford", "Mustang")

print(car1.display_car())
print(car2.display_car())

# Get the total number of cars created using the static method.
print(f"\nTotal cars created: {Car.get_total_cars()}")
