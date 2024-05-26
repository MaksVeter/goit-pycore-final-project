"""Note Record main class"""
from .NoteText import NoteText


class NoteRecord:
    """ note record """
    def __init__(self, note_text):
        self.note_text = NoteText(note_text)
        self.note_tag = []


    def note_text_add(self, note_text: str):
        """ add text note """
        self.note_text = NoteText(note_text)

    def __str__(self):
        return f'{self.note_text}'
