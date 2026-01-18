# TODO Написать 3 класса с документацией и аннотацией типов
from typing import Iterable
import doctest


class DataSummary:
    """
    A simple class for basic data analysis.

    Stores numeric data and provides basic descriptive statistics.

    Example:
        >>> summary = DataSummary([10, 20, 30], "Sales", "USD")
        >>> summary.mean()
        20.0
        >>> summary.minimum()
        10
        >>> summary.maximum()
        30
    """

    def __init__(self, data: Iterable[float], name: str, unit: str):
        """
        Initialize DataSummary with validation.

        Args:
            data: Iterable of numeric values.
            name: Dataset name.
            unit: Measurement unit.

        Raises:
            TypeError: If types are invalid.
            ValueError: If values are invalid.

        Examples:
            >>> DataSummary([1, 2, 3], "Test", "kg")
            DataSummary(name='Test', unit='kg', count=3)

            >>> DataSummary([], "Test", "kg")
            Traceback (most recent call last):
            ...
            ValueError: data cannot be empty
        """

        # --- type validation ---
        if not isinstance(name, str):
            raise TypeError("name must be a string")

        if not isinstance(unit, str):
            raise TypeError("unit must be a string")

        if not isinstance(data, Iterable):
            raise TypeError("data must be an iterable of numbers")

        data = list(data)

        if not all(isinstance(x, (int, float)) for x in data):
            raise TypeError("all elements in data must be int or float")

        # --- value validation ---
        if len(data) == 0:
            raise ValueError("data cannot be empty")

        if name.strip() == "":
            raise ValueError("name cannot be empty")

        if unit.strip() == "":
            raise ValueError("unit cannot be empty")

        # 3 attributes
        self.data = data
        self.name = name
        self.unit = unit

    def mean(self) -> float:
        """
        Calculate the mean value.

        Example:
            >>> DataSummary([2, 4, 6], "Numbers", "n").mean()
            4.0
        """
        return sum(self.data) / len(self.data)

    def minimum(self) -> float:
        """
        Return the minimum value.

        Example:
            >>> DataSummary([3, 1, 2], "Numbers", "n").minimum()
            1
        """
        return min(self.data)

    def maximum(self) -> float:
        """
        Return the maximum value.

        Example:
            >>> DataSummary([3, 1, 2], "Numbers", "n").maximum()
            3
        """
        return max(self.data)

    def __repr__(self):
        """
        Developer-friendly representation.

        Example:
            >>> DataSummary([1, 2], "Test", "m")
            DataSummary(name='Test', unit='m', count=2)
        """
        return (
            f"DataSummary(name={self.name!r}, "
            f"unit={self.unit!r}, "
            f"count={len(self.data)})"
        )

if __name__ == "__main__":
    # TODO работоспособность экземпляров класса проверить с помощью doctest
    doctest.testmod()

