from models.models import Book
from typing import List
import json


def save_books_to_file(books: List[Book]) -> None:
    """
    Сохраняет новую(измененную) книгу в файл
    """
    with open('db/books.json', 'w') as file:
        json.dump([book.to_dict() for book in books], file, ensure_ascii=False, indent=4)


def load_books_from_file() -> List[Book]:
    """
    Loads books from the JSON file and returns them as a list of Book objects.
    """
    file_path = 'db/books.json'
    books = []

    try:
        with open(file_path, 'r') as file:
            data = json.load(file)
            print(f"Loaded JSON data: {data}")  # Debugging statement

            for book_data in data:
                try:
                    book = Book(**book_data)
                    books.append(book)
                except Exception as e:
                    print(f"Error parsing book: {book_data}. Error: {str(e)}")

    except FileNotFoundError:
        print(f"File not found: {file_path}")
    except json.JSONDecodeError:
        print(f"Failed to parse JSON in file: {file_path}")
    except Exception as e:
        print(f"Unexpected error loading books: {str(e)}")

    print(f"Loaded {len(books)} books.")  # Debugging statement

    return books


def add_book(title: str, author: str, year: int) -> None:
    """
     Добавляет новую книгу в библиотеку.

    :param title: Название книги
    :param author: Автор книги
    :param year: Год издания
    """
    books = load_books_from_file()
    new_id = len(books) + 1 if not books else max([book.id for book in books]) + 1
    book = Book(new_id, title, author, year, "в наличии")
    books.append(book)
    save_books_to_file(books)


def delete_book(id: str) -> None:
    """
    Удаляет книгу по номеру ID
    :param id: уникальный идентификационный номер
    """
    books = load_books_from_file()
    books = [book for book in books if book.id != id]
    book_index = next((index for index, book in enumerate(books) if book.id == id), None)
    if book_index is None:
        raise ValueError(f"Книга с ID {id} не найдена.")
    del books[book_index]
    save_books_to_file(books)


def find_books(query: str) -> List[Book]:
    """
    Ищет книги в библиотеке по названию, по автору, по году издания.
    """
    books = load_books_from_file()
    return [book for book in books if query.lower() in book.title.lower() or
            query.lower() in book.author.lower() or
            str(query).lower() in str(book.year)]


def display_books() -> None:
    """
    Отображает список всех книг в библиотеке
    """
    books = load_books_from_file()
    for book in books:
        print(f"ID: {book.id}, Title: {book.title}, Author: {book.author}, Year: {book.year}, Status: {book.status}")


def change_status(id: str, new_status: str) -> None:
    """
    Меняет статус книги по ID: статус "в наличии" и "выдана"
    """
    books = load_books_from_file()
    for book in books:
        if book.id == id:
            book.status = new_status
            break
    save_books_to_file(books)