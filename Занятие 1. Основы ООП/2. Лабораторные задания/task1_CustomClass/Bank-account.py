import doctest


class BankAccount:
    """
    Простой класс банковского счёта.

    Атрибуты:
        owner (str): имя владельца
        balance (float): баланс (>= 0)
        currency (str): валюта счёта

    >>> acc = BankAccount("Ivan", 100, "USD")
    >>> acc.balance
    100.0
    >>> acc.deposit(50)
    >>> acc.balance
    150.0
    >>> acc.withdraw(30)
    >>> acc.balance
    120.0
    """

    def __init__(self, owner: str, balance: float, currency: str):
        self.owner = self._validate_owner(owner)
        self.balance = self._validate_balance(balance)
        self.currency = self._validate_currency(currency)

    # ---------- validators ----------

    def _validate_owner(self, owner: str) -> str:
        """Проверка имени владельца."""
        if not isinstance(owner, str):
            raise TypeError("owner должен быть строкой")
        if not owner:
            raise ValueError("owner не может быть пустым")
        return owner

    def _validate_balance(self, balance: float) -> float:
        """Проверка баланса."""
        if not isinstance(balance, (int, float)):
            raise TypeError("balance должен быть числом")
        if balance < 0:
            raise ValueError("balance не может быть отрицательным")
        return float(balance)

    def _validate_currency(self, currency: str) -> str:
        """Проверка валюты."""
        if not isinstance(currency, str):
            raise TypeError("currency должен быть строкой")
        if not currency:
            raise ValueError("currency не может быть пустой")
        return currency

    def _validate_amount(self, amount: float) -> float:
        """Проверка суммы операции."""
        if not isinstance(amount, (int, float)):
            raise TypeError("amount должен быть числом")
        if amount <= 0:
            raise ValueError("amount должен быть больше 0")
        return float(amount)

    # ---------- public methods ----------

    def deposit(self, amount: float) -> None:
        """
        Пополнение счёта.

        >>> acc = BankAccount("Anna", 0, "EUR")
        >>> acc.deposit(100)
        >>> acc.balance
        100.0
        """
        amount = self._validate_amount(amount)
        self.balance += amount

    def withdraw(self, amount: float) -> None:
        """
        Снятие средств.

        >>> acc = BankAccount("Oleg", 50, "USD")
        >>> acc.withdraw(20)
        >>> acc.balance
        30.0
        """
        amount = self._validate_amount(amount)

        if amount > self.balance:
            raise ValueError("Недостаточно средств")

        self.balance -= amount


if __name__ == "__main__":
    doctest.testmod()
