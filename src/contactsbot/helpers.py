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


    baner = """
   _       _     _             _       ___       _   
  /_\  ___(_)___| |_ ___ _ __ | |_    / __\ ___ | |_ 
 //_\\/ __| / __| __/ _ \ '_ \| __|  /__\/// _ \| __|
/  _  \__ \ \__ \ ||  __/ | | | |_  / \/  \ (_) | |_ 
\_/ \_/___/_|___/\__\___|_| |_|\__| \_____/\___/ \__|
                                                     
    """
    print(Fore.GREEN + baner + Style.RESET_ALL)



def show_menu():
    """ print preview menu """
    print("Welcome to the assistant bot!\n\n")
    print("List of commands")
    print_with_color("1.FGBS hello BESR say hello to the assistant")
    print_with_color("2.FGBS add [contact_name] [phone_number] BESR adds contact name and phone number to memory")
    print_with_color("3.FGBS change [contact_name] [old_phone_number] [new_phone_number] BESR edits the contact's phone number")
    print_with_color("4.FGBS phone [contact_name] BESR displays the contact's phone number")
    print_with_color("5.FGBS all BESR show contacts phone book")
    print_with_color("6.FGBS close BESR or FGBS exit BESR exit from the assistant")
    print_with_color("7.FGBS add-birthday [contact_name] [day_of_birthday] BESR add birthday of contact name")
    print_with_color("8.FGBS show-birthday [contact_name] BESR display day of birth")
    print_with_color("9.FGBS birthdays BESR show birthdays that will happen in the next week")
    print_with_color("10.FGBS note-add BESR add text note")
    print_with_color("11.FGBS note-show BESR show all notes")
    print_with_color("12.FGBS help BESR help page\n\n")


def get_help():
    """ show help section """
    return """
    Help Page:

    Usage
        contactsbot [command] [values]

    Commands:
        hello                                   say hello to the assistant
        add [name] [phone]                      add contact name and phone number to the memory
        change [name] [old_phone] [new_phone]   edits the contact's phone number
        phone [name]                            displays the contact's phone number
        all                                     show contacts phone book
        close                                   exit from the assistant
        exit                                    exit from the assistant
        add-birthday [name] [birthday]          add birthday of contact name
        show-birthday [name]                    display day of birth
        birthdays                               show birthdays that will happen in the next week
        note-add                                add note
        note-show                               show all notes\n\n
    """