from typing import Iterable
import doctest


class DataSummary:
    """
    Класс для базового анализа числовых данных.

    Хранит числовой набор данных и предоставляет
    простые описательные статистики.

    Атрибуты:
        data (list[float]): Числовые данные
        name (str): Название набора данных
        unit (str): Единица измерения данных

    Пример использования:
        >>> summary = DataSummary([10, 20, 30], "Sales", "USD")
        >>> summary.mean()
        20.0
        >>> summary.minimum()
        10
        >>> summary.maximum()
        30
        >>> summary.report()
        'Sales summary: mean=20.0 USD, min=10 USD, max=30 USD'
    """

    def __init__(self, data: Iterable[float], name: str, unit: str):
        """
        Инициализация объекта DataSummary с проверкой типов и значений.

        Аргументы:
            data: Итерируемая последовательность чисел
            name: Название набора данных
            unit: Единица измерения

        Исключения:
            TypeError: Если типы аргументов неверны
            ValueError: Если значения аргументов некорректны

        Примеры:
            >>> DataSummary([1, 2, 3], "Test", "kg")
            DataSummary(name='Test', unit='kg', count=3)

            >>> DataSummary([], "Test", "kg")
            Traceback (most recent call last):
            ...
            ValueError: data cannot be empty
        """

        # Проверка типа имени
        if not isinstance(name, str):
            raise TypeError("name must be a string")

        # Проверка типа единицы измерения
        if not isinstance(unit, str):
            raise TypeError("unit must be a string")

        # Проверка, что данные итерируемые
        if not isinstance(data, Iterable):
            raise TypeError("data must be an iterable of numbers")

        # Преобразование данных в список
        data = list(data)

        # Проверка, что все элементы являются числами
        if not all(isinstance(x, (int, float)) for x in data):
            raise TypeError("all elements in data must be int or float")

        # Проверка, что список данных не пустой
        if len(data) == 0:
            raise ValueError("data cannot be empty")

        # Проверка, что имя не пустое
        if name.strip() == "":
            raise ValueError("name cannot be empty")

        # Проверка, что единица измерения не пустая
        if unit.strip() == "":
            raise ValueError("unit cannot be empty")

        # Атрибуты экземпляра
        self.data = data
        self.name = name
        self.unit = unit

    def mean(self) -> float:
        """
        Возвращает среднее арифметическое значений.

        Пример:
            >>> DataSummary([2, 4, 6], "Numbers", "n").mean()
            4.0
        """
        return sum(self.data) / len(self.data)

    def minimum(self) -> float:
        """
        Возвращает минимальное значение набора данных.

        Пример:
            >>> DataSummary([3, 1, 2], "Numbers", "n").minimum()
            1
        """
        return min(self.data)

    def maximum(self) -> float:
        """
        Возвращает максимальное значение набора данных.

        Пример:
            >>> DataSummary([3, 1, 2], "Numbers", "n").maximum()
            3
        """
        return max(self.data)

    def report(self) -> str:
        """
        Возвращает текстовый отчёт с учётом единиц измерения.

        Пример:
            >>> summary = DataSummary([10, 20, 30], "Sales", "USD")
            >>> summary.report()
            'Sales summary: mean=20.0 USD, min=10 USD, max=30 USD'
        """
        return (
            f"{self.name} summary: "
            f"mean={self.mean()} {self.unit}, "
            f"min={self.minimum()} {self.unit}, "
            f"max={self.maximum()} {self.unit}"
        )

    def __repr__(self):
        """
        Представление объекта для разработчика.

        Пример:
            >>> DataSummary([1, 2], "Test", "m")
            DataSummary(name='Test', unit='m', count=2)
        """
        return (
            f"DataSummary(name={self.name!r}, "
            f"unit={self.unit!r}, "
            f"count={len(self.data)})"
        )


if __name__ == "__main__":
    # Запуск всех doctest-тестов в модуле
    doctest.testmod()