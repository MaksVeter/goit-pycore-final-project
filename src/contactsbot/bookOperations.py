from .decorators import input_error_catch, require_n_args, name_min_length, require_more_eq_n_args
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
@require_more_eq_n_args(4)
@name_min_length
def add_address(args, book: AddressBook):
    name, *address = args
    address = ' '.join(address)
    if (not (name and address)):
        raise ValueError('Name and phone shouldn\'t be empty')

    record = book.find(name)
    record.add_address(address)
    return "Contact updated. Address added."

@input_error_catch
@require_more_eq_n_args(4)
@name_min_length
def change_address(args, book: AddressBook):
    name, *address = args
    address = ' '.join(address)
    if (not (name and address)):
        raise ValueError('Name and phone shouldn\'t be empty')

    record = book.find(name)
    record.edit_address(address)
    return "Contact updated. Address Updated."


@input_error_catch
@require_n_args(2)
@name_min_length
def add_email(args, book: AddressBook):
    name, email = args
    if (not (name and email)):
        raise ValueError('Name and email shouldn\'t be empty')

    record = book.find(name)
    record.add_email(email)
    return "Contact updated. Email added."


@input_error_catch
@require_n_args(3)
@name_min_length
def change_email(args, book: AddressBook):
    name, old_email, new_email = args
    if (not (name and old_email and new_email)):
        raise ValueError('Name , old email and new email shouldn\'t be empty')
    record = book.find(name)
    record.edit_email(old_email, new_email)
    return "Contact updated. Email Updated."

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
def get_contact_emails(args, book: AddressBook):
    if (len(args) != 1):
        raise ValueError('Operation Requires 1 arg: name')
    name = args[0]
    if (not name):
        raise ValueError('Name shouldn\'t be empty')

    record = book.find(name)
    
    if (record.emails == []):
        return "Contact doesn't have emails"
    else:
        return '; '.join(str(email) for email in record.emails)

@input_error_catch
def get_upcoming_birthdays(args, book: AddressBook):
    if (len(args) != 1):
        raise ValueError('Operation Requires 1 arg: days')
    try:        
        days = int(args[0])
    except ValueError:
        raise ValueError("Error: the number of days should be integer, please enter another value")
    
    birthdays = book.get_upcoming_birthdays(days)
    res = ''
    if (not birthdays):
        res += 'There is no upcoming birthdays'
    else:
        i = 0
        for item in birthdays:
            if i < len(birthdays) -1:
                res += f"Contact name: {item['name']}, Congratulation date: {item['congratulation_date']}\n"
            else:
                res += f"Contact name: {item['name']}, Congratulation date: {item['congratulation_date']}"
            i+=1
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


@input_error_catch
def search_contact(args, book: AddressBook):
    if (len(args) != 1):
        raise ValueError('Operation Requires 1 arg: name')
    name = args[0]
    found = None
    not_found = "Contacts not found."
    if (not name):
        raise ValueError('Name shouldn\'t be empty')
    try:
        found = book.find_like(name)
    except KeyError:
        return not_found

    if(found):
        return "\n".join(str(item) for key,item in found.items())
    
    return not_found
