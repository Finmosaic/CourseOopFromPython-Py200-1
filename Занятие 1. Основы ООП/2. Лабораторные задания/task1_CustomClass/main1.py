from collections import Counter
from typing import Iterable
import doctest

class CategoryAnalyzer:
    """
    Класс для анализа категориальных данных.

    Атрибуты:
        data (list[str]): Список категорий (например, названия фруктов)
        name (str): Название набора данных
        total (int): Общее количество элементов в наборе данных

    Пример использования:
        >>> analyzer = CategoryAnalyzer(["Apple", "Banana", "Apple", "Orange"], "Fruits")
        >>> analyzer.total
        4
        >>> analyzer.most_common(2)
        [('Apple', 2), ('Banana', 1)]
        >>> analyzer.unique_count()
        3
    """

    def __init__(self, data: Iterable[str], name: str):
        # Проверка типа названия
        if not isinstance(name, str):
            raise TypeError("name must be a string")
        # Проверка типа данных
        if not isinstance(data, Iterable):
            raise TypeError("data must be an iterable of strings")
        data = list(data)
        # Проверка, что все элементы строки
        if not all(isinstance(x, str) for x in data):
            raise TypeError("all elements in data must be strings")
        # Проверка, что название не пустое
        if name.strip() == "":
            raise ValueError("name cannot be empty")

        # Атрибуты экземпляра
        self.data = data
        self.name = name
        self.total = len(data)

    def most_common(self, n: int = 1):
        """
        Возвращает n наиболее часто встречающихся категорий.

        Пример:
            >>> analyzer = CategoryAnalyzer(["A","B","A"], "Test")
            >>> analyzer.most_common(2)
            [('A', 2), ('B', 1)]
        """
        counter = Counter(self.data)
        return counter.most_common(n)

    def unique_count(self):
        """
        Возвращает количество уникальных категорий.

        Пример:
            >>> analyzer = CategoryAnalyzer(["A","B","A"], "Test")
            >>> analyzer.unique_count()
            2
        """
        return len(set(self.data))

    def proportion(self, category: str):
        """
        Возвращает долю указанной категории в наборе данных.

        Пример:
            >>> analyzer = CategoryAnalyzer(["A","B","A"], "Test")
            >>> analyzer.proportion("A")
            0.6666666666666666
        """
        if category not in self.data:
            return 0.0
        return self.data.count(category) / self.total

    def __repr__(self):
        # Отображение экземпляра в удобной форме
        return f"CategoryAnalyzer(name={self.name!r}, total={self.total})"


if __name__ == "__main__":
    # Запуск doctest для проверки всех примеров
    doctest.testmod()