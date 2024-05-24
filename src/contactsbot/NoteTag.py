from .Field import Field


class NoteTag(Field):
    """

    Class NodeTag - instance for store node tag

    """

    def __init__(self, value: str):
        """ init """
        if self.__validate_note_tag(value):
            super().__init__(value)
        else:
            raise ValueError('err 11')


    def __validate_note_tag(self, value: str) -> bool:
        """ validation """
        return True


    def update_value(self, value: str):
        """ update note text """
        if value == self.value:
            raise ValueError('err 22')
        if self.__validate_note_tag(value):
            self.value = value
        else:
            raise ValueError('err 33')
