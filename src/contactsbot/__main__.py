#Тимчасово не звертайте уваги на цей файл
from .bookOperations import add_contact, add_phone, get_contact_phones, get_all, add_birthday, get_upcoming_birthdays, change_phone, show_birthday
from .notesOperations import note_add_hendler, note_show_handler
from .helpers import parse_input
from .stateManager import save_data, load_data


def main():
    book = load_data()
    note = load_data('notes.pkl')

    print("Welcome to the assistant bot!")
    try:
        while True:
            user_input = input("Enter a command: ")
            command, *args = parse_input(user_input)

            if command in ["close", "exit"]:
                print("Good bye!")
                break
            elif command == "hello":
                print("How can I help you?")
            elif command == "add":
                print(add_contact(args, book))
            elif command == "add_phone":
                print(add_phone(args, book))
            elif command == "change":
                print(change_phone(args, book))
            elif command == "phone":
                print(get_contact_phones(args, book))
            elif command == "add-birthday":
                print(add_birthday(args, book))
            elif command == "show-birthday":
                print(show_birthday(args, book))
            elif command == "birthdays":
                print(get_upcoming_birthdays(book))
            elif command == "all":
                print(get_all(book))
            elif command == "note-add":
                print(note_add_handler(note))
            elif command == "note-show":
                print(note_show_handler(note))
            else:
                print("Invalid command.")

        save_data(book)
        save_data(note, 'notes.pkl')

    except KeyboardInterrupt:
        print("\nProgram interrupted by user. Exiting...")
        save_data(book)
        save_data(note, 'notes.pkl')


if __name__ == "__main__":
    main()
