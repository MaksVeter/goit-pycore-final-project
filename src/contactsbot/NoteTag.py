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
            raise ValueError('The tag must contain at least 2 and no more than 15 characters')


    def __validate_note_tag(self, value: str) -> bool:
        """ validation """
        return len(value) > 2 and len(value) < 15
    
    def __str__(self):
        """ string presentation """
        return f'{self.value}'
    

    def __len__(self):
        """ lenght """
        return len(self.value)
