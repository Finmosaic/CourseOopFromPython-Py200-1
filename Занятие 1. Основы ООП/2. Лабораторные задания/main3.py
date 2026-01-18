class DataSet:
    """
    Класс для работы с набором числовых данных.

    Атрибуты:
    - data (list[float]): список чисел
    - name (str): название набора данных
    - source (str): источник данных

    >>> ds = DataSet([1.0, 2.0, 3.0], "Sample", "Sensor A")
    >>> ds.name
    'Sample'
    >>> ds.source
    'Sensor A'
    >>> ds.count()
    3
    """

    def __init__(self, data: list, name: str, source: str):
        """
        Инициализация DataSet с проверкой типов и значений.

        >>> DataSet([1, 2, 3], "Test", "File").total()
        6
        """
        # Проверка типа и значения data
        if not isinstance(data, list):
            raise TypeError("data must be a list")
        if not data:
            raise ValueError("data must not be empty")
        if not all(isinstance(x, (int, float)) for x in data):
            raise TypeError("all elements in data must be numbers")

        # Проверка типа и значения name
        if not isinstance(name, str):
            raise TypeError("name must be a string")
        if not name:
            raise ValueError("name must not be empty")

        # Проверка типа и значения source
        if not isinstance(source, str):
            raise TypeError("source must be a string")
        if not source:
            raise ValueError("source must not be empty")

        self.data = data
        self.name = name
        self.source = source

    def count(self) -> int:
        """
        Возвращает количество элементов в наборе данных.

        >>> DataSet([10, 20, 30], "Numbers", "API").count()
        3
        """
        return len(self.data)

    def total(self) -> float:
        """
        Возвращает сумму всех значений.

        >>> DataSet([1, 2, 3], "Sum", "Manual").total()
        6
        """
        return sum(self.data)

    def average(self) -> float:
        """
        Возвращает среднее значение набора данных.

        >>> DataSet([2, 4, 6], "Avg", "Calc").average()
        4.0
        """
        return sum(self.data) / len(self.data)


if __name__ == "__main__":
    import doctest
    doctest.testmod()
