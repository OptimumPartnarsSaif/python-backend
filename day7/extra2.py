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