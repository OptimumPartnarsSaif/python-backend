# Base class
class Account:
    def __init__(self, account_number, account_holder, balance=0.0):
        self.account_number = account_number
        self.account_holder = account_holder
        self.__balance = balance  # private attribute

    def deposit(self, amount):
        if amount > 0:
            self.__balance += amount
            print(f"Deposited {amount:.2f}. New balance: {self.__balance:.2f}")
        else:
            print("Deposit amount must be positive.")

    def withdraw(self, amount):
        if amount > 0 and amount <= self.__balance:
            self.__balance -= amount
            print(f"Withdrew {amount:.2f}. New balance: {self.__balance:.2f}")
        else:
            print("Withdrawal denied.")

    def display_balance(self):
        print(f"Balance: {self.__balance:.2f}")

    # Getter for private balance
    def get_balance(self):
        return self.__balance

    # Magic methods
    def __str__(self):
        return f"Account[{self.account_number}] - Holder: {self.account_holder}, Balance: {self.__balance:.2f}"

    def __eq__(self, other):
        return isinstance(other, Account) and self.account_number == other.account_number


# Subclass: SavingsAccount
class SavingsAccount(Account):
    def __init__(self, account_number, account_holder, balance=0.0, interest_rate=0.02):
        super().__init__(account_number, account_holder, balance)
        self.interest_rate = interest_rate

    def withdraw(self, amount):
        if self.get_balance() - amount < 100:
            print("Withdrawal denied. Minimum balance of 100 required.")
        else:
            super().withdraw(amount)


# Subclass: CheckingAccount
class CheckingAccount(Account):
    def __init__(self, account_number, account_holder, balance=0.0, overdraft_limit=500):
        super().__init__(account_number, account_holder, balance)
        self.overdraft_limit = overdraft_limit

    def withdraw(self, amount):
        if self.get_balance() - amount < -self.overdraft_limit:
            print("Withdrawal denied. Overdraft limit exceeded.")
        else:
            # Access private balance via deposit/withdraw logic in base
            current_balance = self.get_balance()
            new_balance = current_balance - amount
            # Simulate withdrawal
            self._Account__balance = new_balance  # Access private var by name mangling
            print(f"Withdrew {amount:.2f}. New balance: {new_balance:.2f}")


# Example usage
if __name__ == "__main__":
    acc1 = SavingsAccount("S001", "saif", 500, 0.03)
    acc2 = CheckingAccount("C001", "nour", 200, 300)

    print(acc1)
    print(acc2)

    acc1.withdraw(450)  # Should be denied
    acc2.withdraw(400)  # Should be allowed (overdraft)

    acc1.deposit(100)
    acc1.display_balance()

    # Comparing accounts
    acc3 = SavingsAccount("S001", "Alice Clone", 1000)
    print("acc1 == acc3?", acc1 == acc3)  # True (same account_number)
