class BankAccount:
    def __init__(self, account_number: str, account_holder: str, balance: float = 0.0):
        self.account_number = account_number
        self.account_holder = account_holder
        self.balance = balance

    def deposite(self, amount: float) -> None:
        if amount > 0:
            self.balance += amount
        else:
            raise ValueError("Deposit amount must be positive")

    def withdraw(self, amount: float) -> bool:
        if 0 < amount <= self.balance:
            self.balance -= amount
            return True
        else:
            return False

    def get_balance(self) -> float:
        return self.balance

account = BankAccount("123456789", "Praneetha", 10000.0)
account.deposite(500.0)
print("Balance after deposite:", account.get_balance())  # Output: Balance after deposit: 1500.0
successful_withdrawal = account.withdraw(2000.0)
print("Withdrawal successful:", successful_withdrawal)  # Output: Withdrawal successful: True
print("Balance after withdrawal:", account.get_balance())  # Output: Balance after withdrawal: 1300.0
unsuccessful_withdrawal = account.withdraw(1500.0)
print("Withdrawal successful:", unsuccessful_withdrawal)  # Output: Withdrawal successful: False
print("Balance after unsuccessful withdrawal:", account.get_balance())  # Output: Balance after unsuccessful withdrawal: 1300.0
