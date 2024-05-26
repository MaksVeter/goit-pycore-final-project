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
            raise ValueError('The note must contain at least 2 and no more than 2000 characters')


    def __validate_note_text(self, value: str) -> bool:
        """ validation """
        return len(value) > 2 and len(value) < 2000


    def __str__(self):
        """ string presentation """
        return f'{self.value}'
    

    def __len__(self):
        """ lenght """
        return len(self.value)
    
