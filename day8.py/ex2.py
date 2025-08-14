# Base class
class Product:
    def __init__(self, product_id, name, price, quantity):
        self.product_id = product_id
        self.name = name
        self.__price = price  # private
        self.quantity = quantity

    def apply_discount(self, percent):
        if 0 < percent < 100:
            self.__price -= self.__price * (percent / 100)
            print(f"Discount applied. New price: ${self.__price:.2f}")
        else:
            print("Invalid discount percentage.")

    def restock(self, amount):
        if amount > 0:
            self.quantity += amount
            print(f"Restocked {amount} units. New quantity: {self.quantity}")
        else:
            print("Restock amount must be positive.")

    # Getter for price
    def get_price(self):
        return self.__price

    # Setter for price (if needed)
    def set_price(self, new_price):
        if new_price > 0:
            self.__price = new_price
        else:
            print("Price must be positive.")

    # Magic 
    def __add__(self, other):
        if isinstance(other, Product) and self.product_id == other.product_id:
            total_quantity = self.quantity + other.quantity
            return f"Total quantity of {self.name}: {total_quantity}"
        return "Cannot add different products."

    def __call__(self):
        print(f"Product: {self.name} (ID: {self.product_id})")
        print(f"Price: ${self.__price:.2f}")
        print(f"Quantity: {self.quantity}")

    def __str__(self):
        return f"{self.name} - ${self.__price:.2f} ({self.quantity} in stock)"


# Subclass: DigitalProduct
class DigitalProduct(Product):
    def __init__(self, product_id, name, price, quantity, file_size):
        super().__init__(product_id, name, price, quantity)
        self.file_size = file_size

    def apply_discount(self, percent):
        if percent > 20:
            percent = 20  # cap discount at 20%
            print("Max discount for digital products is 20%.")
        super().apply_discount(percent)


# Subclass: PhysicalProduct
class PhysicalProduct(Product):
    def __init__(self, product_id, name, price, quantity, weight):
        super().__init__(product_id, name, price, quantity)
        self.weight = weight

    def apply_discount(self, percent):
        original_price = self.get_price()
        new_price = original_price - (original_price * (percent / 100))
        if new_price < 5:
            print("Cannot reduce price below $5.")
        else:
            super().apply_discount(percent)


# Example usage
if __name__ == "__main__":
    dp1 = DigitalProduct("D001", "E-book", 15.00, 100, "5MB")
    pp1 = PhysicalProduct("P001", "Laptop", 1000.00, 5, "2kg")

    dp1()
    pp1()

    dp1.apply_discount(30)  # should cap at 20%
    pp1.apply_discount(99)  # should not allow price < $5

    dp2 = DigitalProduct("D001", "E-book", 15.00, 50, "5MB")
    print(dp1 + dp2)  # combine quantities if same product

    dp1.restock(20)
    dp1()
