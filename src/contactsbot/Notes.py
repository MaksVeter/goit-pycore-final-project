from collections import UserDict
from datetime import datetime, timedelta
from .NoteRecord import NoteRecord


class Notes(UserDict):
    """

    Class Notes - this class can save notes data and has some functionals for notes

    data = {
        0: [
            instance of NoteText
            instance of NoteTag
            instance of NoteDate - #todo
        ],
        1: [
            intance of NoteText
            ...
        ...
    }
    """


    def note_add(self, note_record: NoteRecord):
        """ add note """
        self.data[datetime.now().timestamp()] = note_record



    def __str__(self) -> str:
        return f'{self.data}'
