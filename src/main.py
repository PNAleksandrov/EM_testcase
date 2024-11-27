from src.service.service import (add_book,
                  delete_book,
                  find_books,
                  display_books,
                  change_status,
                  save_books_to_file,
                  load_books_from_file)


def main():

    while True:
        print("\nВыберите действие:")
        print("1. Добавить книгу")
        print("2. Удалить книгу")
        print("3. Найти книгу")
        print("4. Вывести все книги")
        print("5. Изменить статус книги")
        print("0. Выход")
        choice = input("Введите номер действия: ")

        if choice == '1':
            title = input("Введите название книги: ")
            author = input("Введите автора книги: ")
            year = int(input("Введите год издания: "))
            add_book(title, author, year)
        elif choice == '2':
            try:
                id = int(input("Введите ID книги для удаления: "))
                delete_book(id)
            except ValueError as e:
                print(e)
        elif choice == '3':
            query = input("Введите запрос для поиска: ")
            found_books = find_books(query)
            if found_books:
                print("Найденные книги:")
                for book in found_books:
                    print(f"{book.id}: {book.title} ({book.author}) - {book.year}")
            else:
                print("Книги не найдены.")
        elif choice == '4':
            display_books()
        elif choice == '5':
            id = int(input("Введите ID книги для изменения статуса: "))
            new_status = input("Введите новый статус ('в наличии' или 'выдана'): ")
            change_status(id, new_status)
        elif choice == '0':
            break


if __name__ == "__main__":
    main()