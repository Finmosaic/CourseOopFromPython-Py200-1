import doctest


class Person:
    """
    Класс Person описывает человека.

    Атрибуты:
        name (str): имя человека
        age (int): возраст (>= 0)
        email (str): электронная почта

    >>> p = Person("Ivan", 30, "ivan@example.com")
    >>> p.age
    30
    >>> p.birthday()
    >>> p.age
    31
    >>> p.change_email("new@mail.com")
    >>> p.email
    'new@mail.com'
    """

    def __init__(self, name: str, age: int, email: str):
        self.name = self._validate_name(name)
        self.age = self._validate_age(age)
        self.email = self._validate_email(email)

    # ---------- validators ----------

    def _validate_name(self, name: str) -> str:
        """Проверка имени."""
        if not isinstance(name, str):
            raise TypeError("name должен быть строкой")
        if not name:
            raise ValueError("name не может быть пустым")
        return name

    def _validate_age(self, age: int) -> int:
        """Проверка возраста."""
        if not isinstance(age, int):
            raise TypeError("age должен быть целым числом")
        if age < 0:
            raise ValueError("age не может быть отрицательным")
        return age

    def _validate_email(self, email: str) -> str:
        """Проверка email."""
        if not isinstance(email, str):
            raise TypeError("email должен быть строкой")
        if "@" not in email:
            raise ValueError("email должен содержать '@'")
        return email

    # ---------- public methods ----------

    def birthday(self) -> None:
        """
        Увеличивает возраст на 1 год.

        >>> p = Person("Anna", 20, "anna@mail.com")
        >>> p.birthday()
        >>> p.age
        21
        """
        self.age += 1

    def change_email(self, new_email: str) -> None:
        """
        Изменяет email.

        >>> p = Person("Oleg", 40, "old@mail.com")
        >>> p.change_email("new@mail.com")
        >>> p.email
        'new@mail.com'
        """
        self.email = self._validate_email(new_email)

    def is_adult(self) -> bool:
        """
        Проверяет, является ли человек совершеннолетним.

        >>> Person("Max", 17, "m@mail.com").is_adult()
        False
        >>> Person("Max", 18, "m@mail.com").is_adult()
        True
        """
        return self.age >= 18


if __name__ == "__main__":
    doctest.testmod()

