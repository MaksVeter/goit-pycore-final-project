from .decorators import input_error_catch, require_n_args, name_min_length
from .Record import Record
from .AddressBook import AddressBook


@input_error_catch
@require_n_args(2)
@name_min_length
def add_contact(args, book: AddressBook):
    name, phone = args
    if (not (name and phone)):
        raise ValueError('Name and phone shouldn\'t be empty')
    message = "Contact updated."
    try:
        record = book.find(name)
    except:
        message = "Contact added."
        record = Record(name)
        book.add_record(record)

    record.add_phone(phone)
    return message


@input_error_catch
@require_n_args(2)
@name_min_length
def add_phone(args, book: AddressBook):
    name, phone = args
    if (not (name and phone)):
        raise ValueError('Name and phone shouldn\'t be empty')

    record = book.find(name)
    record.add_phone(phone)
    return "Contact updated. Phone added."


@input_error_catch
@require_n_args(3)
@name_min_length
def change_phone(args, book: AddressBook):
    name, old_phone, new_phone = args
    if (not (name and old_phone and new_phone)):
        raise ValueError('Name , old phone and new phone shouldn\'t be empty')
    record = book.find(name)
    record.edit_phone(old_phone, new_phone)
    return "Contact updated. Phone Updated."


@input_error_catch
@require_n_args(2)
@name_min_length
def add_birthday(args, book: AddressBook):
    name, birthday = args
    if (not (name and birthday)):
        raise ValueError('Name and phone shouldn\'t be empty')

    record = book.find(name)
    record.add_birthday(birthday)
    return "Contact updated. Birthday added."


@input_error_catch
@name_min_length
def show_birthday(args, book: AddressBook):
    if (len(args) != 1):
        raise ValueError('Operation Requires 1 arg: name')
    name = args[0]

    record = book.find(name)
    if (record.birthday):
        return str(record.birthday)
    else:
        return 'Contact don\'t have birthday jet'


@input_error_catch
def get_contact_phones(args, book: AddressBook):
    if (len(args) != 1):
        raise ValueError('Operation Requires 1 arg: name')
    name = args[0]
    if (not name):
        raise ValueError('Name shouldn\'t be empty')

    record = book.find(name)

    return '; '.join(str(phone) for phone in record.phones)


@input_error_catch
def get_upcoming_birthdays(book: AddressBook):
    birthdays = book.get_upcoming_birthdays()
    res = ''
    if (not birthdays):
        res += 'There is no upcoming birthdays'
    else:
        for item in birthdays:
            res += f"Contact name: {item['name']}, Congratulation date: {item['congratulation_date']}"
    return res


@input_error_catch
def get_all(book: AddressBook):
    return str(book)


@input_error_catch
def delete_contact(args, book: AddressBook):
    if (len(args) != 1):
        raise ValueError('Operation Requires 1 arg: name')
    name = args[0]
    if (not name):
        raise ValueError('Name shouldn\'t be empty')
    try:
        book.delete(name)
    except KeyError:
        return "Contact doesn't exist."

    return "Contact deleted."
