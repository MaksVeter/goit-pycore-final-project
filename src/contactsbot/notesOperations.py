from .decorators import input_error_catch, require_n_args, name_min_length
from .NoteRecord import NoteRecord
from .Notes import Notes
from .helpers import print_with_color


def note_add_handler(note: Notes):
    """ note add hendler """
    print_with_color('Please enter a note text : ', 'yellow')
    note_text = input()
    note.note_add(NoteRecord(note_text))
    return "Note added"


def note_show_handler(note: Notes):
    """ show all notes """
    if len(note) <= 0:
        print_with_color('Notes are empty', 'yellow')
    for id, text in note.data.items():
        print_with_color(f"ID: {id},\nNote text: {text}\n", 'yellow')
    return True
