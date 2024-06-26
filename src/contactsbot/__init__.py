"""Module export functions to comunicate with contacts bot."""

from .bookOperations import add_contact, add_phone, get_contact_phones, get_all, add_birthday, \
    get_upcoming_birthdays, change_phone, show_birthday, delete_contact, search_contact, \
    add_email, change_email, get_contact_emails, add_address, change_address
from .notesOperations import note_add_handler, note_all_handler, note_change_handler, \
    note_delete_handler, note_delete_all_handler, note_search_handler
from .helpers import parse_input, show_banner, print_with_color, show_menu, get_help
from .AddressBook import AddressBook
from .stateManager import save_data, load_data
__all__ = [
    'parse_input',
    'show_banner',
    'print_with_color',
    'show_menu',
    'get_help',
    'add_contact',
    'add_phone',
    'add_email',
    'add_birthday',
    'get_upcoming_birthdays',
    'show_birthday',
    'change_phone',
    'change_email',
    'get_contact_phones',
    'get_contact_emails',
    'get_all',
    'AddressBook',
    'save_data',
    'load_data',
    'delete_contact',
    'search_contact',
    'note_add_handler',
    'note_all_handler',
    'note_change_handler',
    'note_delete_handler',
    'note_delete_all_handler',
    'note_search_handler',
    'add_address',
    'change_address'
]
