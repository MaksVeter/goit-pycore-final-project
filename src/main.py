from contactsbot import parse_input, add_contact, add_phone, add_birthday, get_contact_phones, \
    get_upcoming_birthdays, get_all, show_birthday, change_phone, AddressBook, save_data, \
    load_data, show_banner, show_menu, get_help, print_with_color

def main():

    book = load_data()
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
            elif command == "add-birthday":
                # print(add_birthday(args, book))
                print_with_color(add_birthday(args, book), 'yellow')
            elif command == "show-birthday":
                # print(show_birthday(args, book))
                print_with_color(show_birthday(args, book), 'yellow')
            elif command == "birthdays":
                # print(get_upcoming_birthdays(book))
                print_with_color(get_upcoming_birthdays(book), 'yellow')
            elif command == "all":
                # print(get_all(book))
                print_with_color(get_all(book), 'yellow')
            elif command == "help":
                # print(get_help())
                print_with_color(get_help(), 'yellow')

            else:
                print_with_color("Invalid command.", 'yellow')

        save_data(book)
    except KeyboardInterrupt:
        print("\nProgram interrupted by user. Exiting...")
        save_data(book)


if __name__ == "__main__":
    # show banner
    show_banner()
    # show menu
    show_menu()
    main()
