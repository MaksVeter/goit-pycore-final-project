"""Contacts bot Package entry point"""
from .bookOperations import add_address, add_contact, add_email, add_phone, change_address, \
    change_email, get_contact_emails, delete_contact, get_contact_phones, get_all, add_birthday, \
    get_upcoming_birthdays, change_phone, search_contact, show_birthday
from .notesOperations import note_add_handler, note_all_handler, note_change_handler,  \
    note_delete_handler, note_delete_all_handler, note_search_handler
from .helpers import get_help, parse_input, print_with_color, show_banner, show_menu
from .stateManager import save_data, load_data


def main():
    """main function to run console interaction with contacts bot and user"""
    show_banner()
    show_menu()
    book = load_data()
    note = load_data('notes.pkl')
    try:
        while True:
            user_input = input("Enter a command: ")
            if (not user_input):
                print_with_color("Invalid command.", 'yellow')
                continue
            command, *args = parse_input(user_input)

            if command in ["close", "exit"]:
                print_with_color("Good bye!", 'yellow')
                break
            if command == "hello":
                print_with_color("How can I help you?", 'yellow')
            elif command == "add":
                print_with_color(add_contact(args, book), 'yellow')
            elif command == "add_phone":
                print_with_color(add_phone(args, book), 'yellow')
            elif command == "change":
                print_with_color(change_phone(args, book), 'yellow')
            elif command == "phone":
                print_with_color(get_contact_phones(args, book), 'yellow')
            elif command == "add-email":
                print_with_color(add_email(args, book), 'yellow')
            elif command == "change-email":
                print_with_color(change_email(args, book), 'yellow')
            elif command == "email":
                print_with_color(get_contact_emails(args, book), 'yellow')
            elif command == "add-birthday":
                print_with_color(add_birthday(args, book), 'yellow')
            elif command == "show-birthday":
                print_with_color(show_birthday(args, book), 'yellow')
            elif command == "birthdays":
                print_with_color(get_upcoming_birthdays(args, book), 'yellow')
            elif command == "add-address":
                print_with_color(add_address(args, book), 'yellow')
            elif command == "change-address":
                print_with_color(change_address(args, book), 'yellow')
            elif command == "all":
                print_with_color(get_all(book), 'yellow')
            elif command == "delete":
                print_with_color(delete_contact(args, book), 'yellow')
            elif command == "search":
                print_with_color(search_contact(args, book), 'yellow')
            elif command == "help":
                print_with_color(get_help(), 'yellow')
            elif command == "note-add":
                print_with_color(note_add_handler(note), 'yellow')
            elif command == "note-all":
                note_all_handler(note)
            elif command == "note-change":
                print_with_color(note_change_handler(args, note), 'yellow')
            elif command == "note-delete":
                print_with_color(note_delete_handler(args, note), 'yellow')
            elif command == "note-delete-all":
                print_with_color(note_delete_all_handler(note), 'yellow')
            elif command == "note-search":
                note_search_handler(args, note)
            else:
                print_with_color("Invalid command.", 'yellow')

        save_data(book)
        save_data(note, 'notes.pkl')

    except KeyboardInterrupt:
        print_with_color("\nProgram interrupted by user. Exiting...", 'red')
        save_data(book)
        save_data(note, 'notes.pkl')


if __name__ == "__main__":
    main()
