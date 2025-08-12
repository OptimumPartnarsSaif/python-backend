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