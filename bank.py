from dataclasses import dataclass

@dataclass
class BankAccount:
    owner: str
    _balance: float = 0.0

    def balance(self) -> float:
        return self._balance

    def deposit(self, amount: float) -> None:
        if amount <= 0:
            raise ValueError("amount must be > 0")
        self._balance += amount

    def withdraw(self, amount: float) -> None:
        if amount <= 0:
            raise ValueError("amount must be > 0")
        if amount > self._balance:
            raise ValueError("insufficient funds")
        self._balance -= amount

    def transfer(self, other: "BankAccount", amount: float) -> None:
        if amount <= 0:
            raise ValueError("amount must be > 0")
        if amount > self._balance:
            raise ValueError("insufficient funds")
        self._balance -= amount
        other._balance += amount
