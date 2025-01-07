
'''
Encapsulation bundles data (attributes) and methods into a single unit (class) and restricts direct access to 
some attributes by using private variables.

'''

class BankAccount:
    def __init__(self, owner, balance):
        self.owner = owner  # Public attribute
        self.__balance = balance  # Private attribute (cannot be accessed directly)

    def deposit(self, amount):
        """Add money to the account."""
        self.__balance += amount
        print(f"{amount} deposited. New balance: {self.__balance}")

    def withdraw(self, amount):
        """Withdraw money if sufficient balance exists."""
        if amount > self.__balance:
            print("Insufficient balance!")
        else:
            self.__balance -= amount
            print(f"{amount} withdrawn. New balance: {self.__balance}")

# Create a bank account object
account = BankAccount("Alice", 1000)

# Deposit and withdraw using methods
account.deposit(500)  # Output: 500 deposited. New balance: 1500
account.withdraw(2000)  # Output: Insufficient balance!

# Attempt to access private attribute directly (will raise an error)
# print(account.__balance)  # AttributeError: 'BankAccount' object has no attribute '__balance'\