from .decorators import input_error_catch, require_n_args
from .NoteRecord import NoteRecord
from .Notes import Notes
from .helpers import print_with_color


@input_error_catch
def note_add_handler(note: Notes):
    """ note add hendler """
    print_with_color('Please enter a note text : ', 'yellow')
    note_text = input()
    note.note_add(NoteRecord(note_text))
    return "Note added"


@input_error_catch
def note_show_handler(note: Notes):
    """ show all notes """
    if len(note) <= 0:
        print_with_color('Notes are empty', 'yellow')
    for id, text in note.data.items():
        print_with_color(f"ID: {id},\nNote text: {text}\n", 'yellow')
    return True


@input_error_catch
@require_n_args(1)
def note_change_handler(args, note: Notes):
    """ change notes by id """
    note_id, *_ = args
    note_id = int(note_id)
    # get note by id
    data = note.get_note_by_id(note_id)
    if data:
        print_with_color('Old note text:', 'yellow')
        print_with_color(str(data.note_text), 'yellow')
        print_with_color('Please entered new note :', 'yellow')
        note.note_add(NoteRecord(input()), note_id)
    else:
        return f'Cant found note with ID:{note_id}'
    return 'Note is updated'


@input_error_catch
@require_n_args(1)
def note_delete_handler(args, note: Notes):
    """ delete note by ID """
    note_id, *_ = args
    note_id = int(note_id)
    # get note by id
    data = note.get_note_by_id(note_id)
    if data:
        note.note_delete_by_id(note_id)
    else:
        return f'Cant found note with ID:{note_id}'
    return f'Note with ID: {note_id} was deleted'


def note_delete_all_handler(note: Notes):
    """ Delete all notes """
    print_with_color('Are you sure, please confirn y/n', 'yellow')
    ansver = input()
    if ansver and ansver.lower() == 'y':
        note.note_delete_all()
        return 'All notes was deleted'
    else:
        return "Ok, it's not (y), but you're a joker, you're scaring me here"

@input_error_catch
@require_n_args(1)
def note_search_handler(args, note: Notes):
    """ Search """
    return 'Not implenebted yet'
