class Book:
    """Базовый класс книги"""

    def __init__(self, name: str, author: str):
        self._name = name
        self._author = author

    @property
    def name(self) -> str:
        return self._name

    @property
    def author(self) -> str:
        return self._author

    def __str__(self) -> str:
        return f"Книга «{self.name}». Автор: {self.author}"

    def __repr__(self) -> str:
        return f"{self.__class__.__name__}(name={self.name!r}, author={self.author!r})"



class PaperBook(Book):
    def __init__(self, name: str, author: str, pages: int):
        super().__init__(name, author)
        self.pages = pages

    @property
    def pages(self) -> int:
        return self._pages

    @pages.setter
    def pages(self, value: int):
        if not isinstance(value, int):
            raise TypeError("pages должно быть целым числом")
        if value <= 0:
            raise ValueError("pages должно быть больше 0")
        self._pages = value

    def __repr__(self) -> str:
        return (
            f"{self.__class__.__name__}("
            f"name={self.name!r}, author={self.author!r}, pages={self.pages})"
        )


class AudioBook(Book):
    """Аудиокнига"""

    def __init__(self, name: str, author: str, duration: float):
        super().__init__(name, author)
        self.duration = duration

    @property
    def duration(self) -> float:
        return self._duration

    @duration.setter
    def duration(self, value: float):
        if not isinstance(value, (int, float)):
            raise TypeError("duration должно быть числом")
        if value <= 0:
            raise ValueError("duration должно быть больше 0")
        self._duration = float(value)

    def __repr__(self) -> str:
        return (
            f"{self.__class__.__name__}("
            f"name={self.name!r}, author={self.author!r}, duration={self.duration})"
        )


book = Book("1984", "Джордж Оруэлл")
paper = PaperBook("Мастер и Маргарита", "Булгаков", 480)
audio = AudioBook("Dune", "Frank Herbert", 21.5)

print(book)
print(paper)
print(audio)

print(repr(paper))
print(repr(audio))