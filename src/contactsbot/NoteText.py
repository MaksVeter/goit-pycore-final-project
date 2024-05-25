from .Field import Field


class NoteText(Field):
    """

    Class NodeText - instance for store node text

    """

    def __init__(self, value: str):
        """ init """
        if self.__validate_note_text(value):
            super().__init__(value)
            self.value = value
        else:
            raise ValueError('err 1')


    def __validate_note_text(self, value: str) -> bool:
        """ validation """
        return True


    def update_value(self, value: str):
        """ update note text """
        if value == self.value:
            raise ValueError('err 2')
        if self.__validate_note_text(value):
            self.value = value
        else:
            raise ValueError('err 3')


    def __str__(self):
        return f'{self.value}'
