from contactsbot import parse_input, add_contact, add_phone, add_birthday, get_contact_phones, \
    get_upcoming_birthdays, get_all, show_birthday, change_phone, AddressBook, save_data, \
    load_data, show_banner, show_menu, get_help, print_with_color, note_add_handler, \
    note_show_handler, note_change_handler, note_delete_handler, note_delete_all_handler, \
    note_search_handler, delete_contact, search_contact


def main():

    book = load_data()
    note = load_data('notes.pkl')
    try:
        while True:
            user_input = input("Enter a command: ")
            command, *args = parse_input(user_input)

            if command in ["close", "exit"]:
                # print("Good bye!")
                print_with_color("Good bye!", 'yellow')
                break
            elif command == "hello":
                # print("How can I help you?")
                print_with_color("How can I help you?", 'yellow')
            elif command == "add":
                # print(add_contact(args, book))
                print_with_color(add_contact(args, book), 'yellow')
            elif command == "add_phone":
                # print(add_phone(args, book))
                print_with_color(add_phone(args, book), 'yellow')
            elif command == "change":
                # print(change_phone(args, book))
                print_with_color(change_phone(args, book), 'yellow')
            elif command == "phone":
                # print(get_contact_phones(args, book))
                print_with_color(get_contact_phones(args, book), 'yellow')
            elif command == "add-email":
                # print(add_phone(args, book))
                print_with_color(add_email(args, book), 'yellow')
            elif command == "change-email":
                # print(change_phone(args, book))
                print_with_color(change_email(args, book), 'yellow')
            elif command == "email":
                # print(get_contact_phones(args, book))
                print_with_color(get_contact_emails(args, book), 'yellow')
            elif command == "add-birthday":
                # print(add_birthday(args, book))
                print_with_color(add_birthday(args, book), 'yellow')
            elif command == "show-birthday":
                # print(show_birthday(args, book))
                print_with_color(show_birthday(args, book), 'yellow')
            elif command == "birthdays":
                # print(get_upcoming_birthdays(book))
                print_with_color(get_upcoming_birthdays(args, book), 'yellow')
            elif command == "add-address":
                print_with_color(add_address(args, book),'yellow')
                # print(add_address(args, book))
            elif command == "change-address":
                print_with_color(change_address(args, book), 'yellow')
                # print(change_address(args, book))
            elif command == "all":
                # print(get_all(book))
                print_with_color(get_all(book), 'yellow')
            elif command == "delete":
                print_with_color(delete_contact(args, book), 'yellow')
            elif command == "search":
                print_with_color(search_contact(args, book), 'yellow')
            elif command == "help":
                # print(get_help())
                print_with_color(get_help(), 'yellow')
            elif command == "note-add":
                print_with_color(note_add_handler(note), 'yellow')
            elif command == "note-show":
                note_show_handler(note)
            elif command == "note-change":
                print_with_color(note_change_handler(args, note), 'yellow')
            elif command == "note-delete":
                print_with_color(note_delete_handler(args, note), 'yellow')
            elif command == "note-delete-all":
                print_with_color(note_delete_all_handler(note), 'yellow')
            elif command == "note-search":
                print_with_color(note_search_handler(args, note), 'yellow')
            else:
                print_with_color("Invalid command.", 'yellow')

        save_data(book)
        save_data(note, 'notes.pkl')

    except KeyboardInterrupt:
        print("\nProgram interrupted by user. Exiting...")
        save_data(book)
        save_data(note, 'notes.pkl')


if __name__ == "__main__":
    # show banner
    show_banner()
    # show menu
    show_menu()
    main()
