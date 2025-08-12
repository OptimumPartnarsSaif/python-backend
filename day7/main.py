# This class is a blueprint for creating saif objects.
class saif:
    """
    A simple class to model a bank account.

    Attributes:
        owner (str): The name of the account owner.
        balance (float): The current balance of the account.
    """

    
    def __init__(self, owner, initial_balance=0.0):
        self.owner = owner
        self.balance = initial_balance
        print(f"Account for {self.owner} created with an initial balance of ${self.balance:.2f}.")

    # This method allows us to deposit money into the account.
    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            print(f"Deposited ${amount:.2f}. New balance is ${self.balance:.2f}.")
        else:
            print("Deposit amount must be positive.")

    # This method allows us to withdraw money from the account.
    def withdraw(self, amount):
        if amount > 0:
            if self.balance >= amount:
                self.balance -= amount
                print(f"Withdrew ${amount:.2f}. New balance is ${self.balance:.2f}.")
            else:
                print("Insufficient funds. Withdrawal denied.")
        else:
            print("Withdrawal amount must be positive.")

    # A simple method to check the current balance.
    def get_balance(self):
        print(f"The current balance for {self.owner} is ${self.balance:.2f}.")
        return self.balance

    # The __str__ method provides a user-friendly string representation of the object.
    def __str__(self):
        return f"Account owner: {self.owner}\nAccount balance: ${self.balance:.2f}"

# ----------------------------------------
# This is a sample usage of the saif class.
# It will only run when this file is executed directly.
if __name__ == "__main__":
    # Create an instance of the saif class.
    # This calls the __init__ method.
    my_account = saif(owner="Alice", initial_balance=1000.0)

    # Use the object's methods to perform actions.
    my_account.deposit(500)
    my_account.withdraw(200)
    my_account.get_balance()

    print("\n--- Trying a failed withdrawal ---")
    my_account.withdraw(1500)  # This should fail due to insufficient funds

    print("\n--- Printing the object directly ---")
    print(my_account) # This calls the __str__ method
