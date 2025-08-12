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