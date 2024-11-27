from typing import List


class Book:
    """
    Модель книги представленной в библиотеке
    """
    def __init__(self, id, title, author, year, status):
        self.id = id
        self.title = title
        self.author = author
        self.year = year
        self.status = status

    def to_dict(self) -> dict[str, str]:
        """
        Преобразование списка в словарь
        :return: dict
        """
        return {
            'id': self.id,
            'title': self.title,
            'author': self.author,
            'year': self.year,
            'status': self.status
        }