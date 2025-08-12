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