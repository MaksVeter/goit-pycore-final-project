import os
from colorama import Fore, Style

def parse_input(user_input):
    cmd, *args = user_input.split()
    cmd = cmd.strip().lower()
    return cmd, *args



def print_with_color(data: str, color: str = 'green'):
    """ 
    print word in text with color 

     - data: text string
     - color: 
       - green: color is green (by default)
       - yellow: color is yellow


     - FG color green
     - BS open (start) bold marker
     - BE close (end) bild marker
     - SR reset all styles  
    """

    # color case
    
    if color == 'yellow':
        print(Fore.YELLOW + data + Style.RESET_ALL)
    elif color == 'red':
        print(Fore.RED + data + Style.RESET_ALL)
    else:
        use_color = Fore.GREEN
        # parsing text string
        data = data.replace('FG', use_color)
        data = data.replace('BS', '\033[1m')
        data = data.replace('BE', '\033[0m')
        data = data.replace('SR', Style.RESET_ALL)
        print(data)




def show_banner():
    """ print banner """


    baner = r"""
   ____            _             _         ____        _   
  / ___|___  _ __ | |_ __ _  ___| |_ ___  | __ )  ___ | |_ 
 | |   / _ \| '_ \| __/ _` |/ __| __/ __| |  _ \ / _ \| __|
 | |__| (_) | | | | || (_| | (__| |_\__ \ | |_) | (_) | |_ 
  \____\___/|_| |_|\__\__,_|\___|\__|___/ |____/ \___/ \__|
                                                           
    """
    print(Fore.GREEN + baner + Style.RESET_ALL)


def get_commands():
    current_dir = os.path.dirname(__file__)
    file_path = os.path.join(current_dir, 'commands.txt')
    rows = None

    def load_rows():
        nonlocal rows
        if rows is None:
            with open(file_path, 'r') as file:
                rows = [row.strip() for row in file.readlines()]
        return rows

    return load_rows


def show_menu():
    """ print preview menu """
    print("Welcome to the assistant bot!\n\n")
    print("List of commands")
    load_rows = get_commands()
    rows = load_rows() 
    for i in range(len(rows)):
        index_str = f"{i+1}."
        print_with_color(f"{index_str:<3}FGBS {rows[i]}")



def get_help():
    """ show help section """
    return """
    Help Page:

    Usage
        contactsbot [command] [values]

    Commands:
        hello                                        Say hello to the assistant
        add [name] [phone]                           Add contact name and phone number to the memory
        change [name] [old_phone] [new_phone]        Edits the contact's phone number
        phone [name]                                 Displays the contact's phone number
        all                                          Show contacts phone book
        search [search_term]                         Search contacts by name
        delete [name]                                Delete contact by name
        close                                        Exit from the assistant
        exit                                         Exit from the assistant
        add-birthday [name] [birthday]               Add birthday of contact name
        show-birthday [name]                         Display day of birth
        birthdays                                    Show birthdays that will happen in the next week
        add-email [name] [email]                     Adds email of contact name
        change-email [name] [old_email] [new_email]  Edits the contact's email
        email [name]                                 Show contacts emails
        add-address [name] [addrress]                Add address of contact name
        change-address [name] [new_address]          Change address of contact name
        note-add                                     Add note
        note-show                                    Show all notes
        note-change [note_id]                        Change note by ID
        note-delete [note_id]                        Delete note by ID
        note-delete-all                              Delete all notes
        note-search [search_term]                    Search in all notes by text
        help                                         Show help page
    """