import doctest

class Person:
    """
    Класс, описывающий человека.

    Атрибуты:
    name (str): имя человека (не пустая строка)
    age (int): возраст (целое число, >= 0)
    city (str): город проживания (не пустая строка)

    >>> p = Person("Anna", 25, "Belgrade")
    >>> p.name
    'Anna'
    >>> p.age
    25
    >>> p.city
    'Belgrade'
    """

    def __init__(self, name: str, age: int, city: str):
        """
        Инициализация объекта Person с проверкой типов и значений.

        >>> Person("Ivan", 17, "Moscow").is_adult()
        False
        >>> Person("Olga", 18, "Berlin").is_adult()
        True
        """
        # Проверка типа и значения имени
        if not isinstance(name, str):
            raise TypeError("name must be a string")
        if not name:
            raise ValueError("name must not be empty")

        # Проверка типа и значения возраста
        if not isinstance(age, int):
            raise TypeError("age must be an integer")
        if age < 0:
            raise ValueError("age must be >= 0")

        # Проверка типа и значения города
        if not isinstance(city, str):
            raise TypeError("city must be a string")
        if not city:
            raise ValueError("city must not be empty")

        self.name = name
        self.age = age
        self.city = city

    def greet(self) -> str:
        """
        Возвращает приветствие с именем человека.

        >>> Person("Anna", 25, "Belgrade").greet()
        'Hello, my name is Anna'
        """
        return f"Hello, my name is {self.name}"

    def is_adult(self) -> bool:
        """
        Проверяет, является ли человек совершеннолетним (18+).

        >>> Person("Petr", 18, "Prague").is_adult()
        True
        >>> Person("Olga", 16, "Berlin").is_adult()
        False
        """
        return self.age >= 18

    def relocate(self, new_city: str) -> None:
        """
        Меняет город проживания человека.

        >>> p = Person("Anna", 25, "Belgrade")
        >>> p.relocate("Novi Sad")
        >>> p.city
        'Novi Sad'
        """
        if not isinstance(new_city, str):
            raise TypeError("new_city must be a string")
        if not new_city:
            raise ValueError("new_city must not be empty")

        self.city = new_city


if __name__ == "__main__":

    doctest.testmod()
