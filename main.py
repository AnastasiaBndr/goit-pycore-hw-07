from instances import Record, AddressBook
from command_parser import parse_input


# def main():
#     # Створення нової адресної книги
#     book = AddressBook()

#     # Створення запису для John
#     john_record = Record("John")
#     john_record.add_phone("+380123456789")
#     john_record.add_phone("+380555555555")
#     john_record.add_birthday("25.10.2000")

#     # Додавання запису John до адресної книги
#     book.add_record(john_record)

#     # Створення та додавання нового запису для Jane
#     jane_record = Record("Jane")
#     jane_record.add_phone("+380123456789")
#     jane_record.add_birthday("25.10.2000")
#     book.add_record(jane_record)

#     # Виведення всіх записів у книзі
#     for name, record in book.data.items():
#         print(record)

#     # Знаходження та редагування телефону для John
#     john = book.find("John")
#     john.edit_phone("+380123456789", "+380555555555")

#     print(john)  # Виведення: Contact name: John, phones: 1112223333; 5555555555

#     # Пошук конкретного телефону у записі John
#     found_phone = john.find_phone("+380555555555")
#     print(f"{john.name}: {found_phone}")  # Виведення: 5555555555

#     print(book)

#     print(f"BIRTHDAYS {book.birthdays(book)}")
#     print(book.show_birthday('John'))

def main():
    book = AddressBook()
    print("Welcome to the assistant bot!")
    while True:
        user_input = input("Enter a command: ")
        command, *args = parse_input(user_input)

        name = args[0] if len(args) > 0 else None

        if command in ["close", "exit"]:
            print("Good bye!")
            break

        elif command == "hello":
            print("How can I help you?")

        elif command == "add":
            if name in book:
                user = book.find(name)
                user.add_phone(args[1] if len(args) > 1 else None)
                book.add_record(user)
                print("Contact updated")
            else:
                record = Record(name)
                record.add_phone(args[1] if len(args) > 1 else None)
                book.add_record(record)
                print("Contact added")
        elif command == "change":
            user = book.find(name)
            user.edit_phone(args[1] if len(args) > 1 else None,
                            args[2] if len(args) > 1 else None)
            book.add_record(user)
            print("Contact updated")
        elif command == "phone":
            print(f"Phones for {name}: {book.show_phones(name)}")

        elif command == "all":
            print(book)

        elif command == "add-birthday":
            user = book.find(name)
            user.add_birthday(args[1] if len(args) > 1 else None)
            book.add_record(user)
            print("Contact updated")

        elif command == "show-birthday":
            print(book.show_birthday(name))

        elif command == "birthdays":
            print(book.birthdays(book))

        else:
            print("Invalid command.")


if __name__ == "__main__":
    main()
