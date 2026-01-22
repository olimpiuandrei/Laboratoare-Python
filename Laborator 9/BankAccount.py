class BankAccount:
    def __init__(self, initial_balance=0):
        if initial_balance < 0:
            raise ValueError("Initial balance cannot be negative")
        self._balance = initial_balance

    def deposit(self, amount):
        if amount <= 0:
            raise ValueError("Deposit amount must be positive")
        self._balance += amount

    def withdraw(self, amount):
        if amount <= 0:
            raise ValueError("Withdraw amount must be positive")
        if amount > self._balance:
            raise ValueError("Insufficient funds")
        self._balance -= amount

    def get_balance(self):
        return self._balance

try:
    initial_balance = float(input("Enter initial balance: "))
    account = BankAccount(initial_balance)

    while True:
        print("\n1. Deposit")
        print("2. Withdraw")
        print("3. Check balance")
        print("4. Exit")

        choice = input("Choose an option: ")

        if choice == "1":
            amount = float(input("Enter deposit amount: "))
            account.deposit(amount)
            print("Deposit successful")

        elif choice == "2":
            amount = float(input("Enter withdraw amount: "))
            account.withdraw(amount)
            print("Withdraw successful")

        elif choice == "3":
            print("Current balance:", account.get_balance())

        elif choice == "4":
            print("Goodbye!")
            break

        else:
            print("Invalid option")

except ValueError as e:
    print("Error:", e)
