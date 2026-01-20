import doctest


class Product:
    """
    Класс Product описывает товар в магазине.

    Атрибуты:
        name (str): название товара
        price (float): цена (>= 0)
        quantity (int): количество на складе (>= 0)

    >>> p = Product("Apple", 1.5, 10)
    >>> p.total_cost()
    15.0
    >>> p.sell(3)
    >>> p.quantity
    7
    >>> p.restock(5)
    >>> p.quantity
    12
    """

    def __init__(self, name: str, price: float, quantity: int):
        self.name = self._validate_name(name)
        self.price = self._validate_price(price)
        self.quantity = self._validate_quantity(quantity)

    # ---------- validators ----------

    def _validate_name(self, name: str) -> str:
        """Проверка названия товара."""
        if not isinstance(name, str):
            raise TypeError("name должен быть строкой")
        if not name:
            raise ValueError("name не может быть пустым")
        return name

    def _validate_price(self, price: float) -> float:
        """Проверка цены."""
        if not isinstance(price, (int, float)):
            raise TypeError("price должен быть числом")
        if price < 0:
            raise ValueError("price не может быть отрицательной")
        return float(price)

    def _validate_quantity(self, quantity: int) -> int:
        """Проверка количества."""
        if not isinstance(quantity, int):
            raise TypeError("quantity должен быть целым числом")
        if quantity < 0:
            raise ValueError("quantity не может быть отрицательным")
        return quantity

    # ---------- public methods ----------

    def sell(self, amount: int) -> None:
        """
        Продажа товара.

        >>> p = Product("Book", 10, 5)
        >>> p.sell(2)
        >>> p.quantity
        3
        """
        amount = self._validate_quantity(amount)
        if amount > self.quantity:
            raise ValueError("Недостаточно товара на складе")

        self.quantity -= amount

    def restock(self, amount: int) -> None:
        """
        Пополнение склада.

        >>> p = Product("Pen", 1, 0)
        >>> p.restock(10)
        >>> p.quantity
        10
        """
        amount = self._validate_quantity(amount)
        self.quantity += amount

    def total_cost(self) -> float:
        """
        Общая стоимость товара на складе.

        >>> Product("Laptop", 1000, 2).total_cost()
        2000.0
        """
        return self.price * self.quantity


if __name__ == "__main__":
    doctest.testmod()

