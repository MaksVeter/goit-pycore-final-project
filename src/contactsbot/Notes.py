""" modules import """
from collections import UserDict
from .NoteRecord import NoteRecord
import re


class Notes(UserDict):
    """
    Class Notes - this class can save notes data and has some functionals for notes

    """

    def note_id_creator(self):
        """ create incremental id for dictionary """
        if len(self.data) > 0:
            # get last key and add 1
            last_key = max(self.data.keys())
            return last_key+1
        
        # then we have empty storage, set 1
        return 1

    def note_add(self, note_record: NoteRecord, note_id=0):
        """ add note """
        if note_id == 0:
            self.data[self.note_id_creator()] = note_record
        else:
            self.data[note_id] = note_record

    def get_note_by_id(self, note_id: int) -> bool | NoteRecord:
        """ get note data by note id """
        if note_id in self.data.keys():
            return self.data[note_id]
        return False

    def note_delete_by_id(self, note_id: int):
        """ delete note by id """
        return self.data.pop(note_id)

    def note_delete_all(self):
        """ Delete all notes """
        self.data = {}
        return True

    def note_search(self, s: str, search_term: str):
        """ Search """
        pattern = re.compile(search_term, re.IGNORECASE)
        return pattern.search(str(s))


    def __str__(self) -> str:
        """ String """
        return f'{self.data}'
