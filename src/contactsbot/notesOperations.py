"""Set of user input handlers"""
from .decorators import input_error_catch, require_n_args
from .NoteRecord import NoteRecord, NoteText
from .Notes import Notes
from .helpers import print_with_color


@input_error_catch
def note_add_handler(note: Notes):
    """ note add hendler """
    print_with_color('Please enter a note text : ', 'yellow')
    note_text = input()
    note.note_add(NoteRecord(NoteText(note_text)))
    return "Note added"


@input_error_catch
def note_all_handler(note: Notes):
    """ show all notes """
    print_with_color('List of notes :\n', 'yellow')
    if len(note) <= 0:
        print_with_color('Notes are empty', 'yellow')
    for key, text in note.data.items():
        print(f"Note:{key}")
        print_with_color(f"{text}", 'back-black')
        print('\n')
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
    return "Ok, it's not (y), but you're a joker, you're scaring me here"


def note_search_handler(args, note: Notes):
    """ Search """
    if len(args) < 1:
        print_with_color('Operation Requires 1 or more args', 'red')
        return 0
    criteria, *_ = args
    counter = 0
    if len(note) > 0:
        print_with_color('\nSearch result:\n', 'yellow')
        for key, item in note.data.items():
            if note.note_search(item.note_text.value, criteria):
                print_with_color(f'ID: {key}', 'yellow')
                print_with_color(f'{item.note_text.value}\n', 'yellow')
                counter += 1
        if not counter:
            print_with_color('No data for searching.', 'yellow')
    else:
        print_with_color('No data for searching', 'yellow')
