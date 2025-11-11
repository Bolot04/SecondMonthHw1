class Book:
    def __init__(self, title, author, pages, format="бумажная"):
        self.title = title
        self.author = author
        self.pages = int(pages)
        self.format = format
    """Выводит название обьекта"""
    def __str__(self):
        return f"{self.title}, {self.author}, {self.pages}"
    """Возвращает количество страниц """
    def __len__(self):
        return f"{self.pages}"
    """ Возврашает общее количество страниц"""
    def __add__(self, other):
        return f"Вмевте: {int(self.pages) + int(other.pages)} страниц"
    """Сравнивает у обьекта какие либо атрибуты на равенства"""
    def __eq__(self, other):
        if self.pages == other.pages:
            return True
        else:
            return False

    def __getitem__(self, index):
        return f"Глава: {index} содержание книги '{self.title}"

    @classmethod
    def from_string(cls, s):
        """Создает объект Book из строки вида 'Название, Автор, Кол-во страниц'."""
        title, author, pages = s.split(", ")
        return cls(title, author, int(pages))

    @staticmethod
    def is_thick(pages):
        """Возвращает True, если книга толще 500 страниц."""
        return pages > 500
#Обычное создание
book1 = Book("1984", "Дж. Оруэлл", 328)
#Через класс-метод
book2 = Book.from_string("Гарри Поттер, Дж. Роулинг, 400")

# Магические методы
print(book1)                    # "1984" — Дж. Оруэлл, 328 стр.
print(Book.__len__(book1))               # 328
print(book1 + book2)            # Вместе: 728 страниц
print(book1 == book2)           # False
print(book1[5])                 # Глава 5: содержание книги '1984'

# Статический метод
print(Book.is_thick(600))       # True
print(Book.is_thick(300))       # False

# Формат по умолчанию
book3 = Book("Python", "Гвидо", 200)
print(book3.format)
