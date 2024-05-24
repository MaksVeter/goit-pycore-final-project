from .Field import Field


class Name(Field):
    """ class Name - contact name """

    def __init__(self, value:str):
        super().__init__(value)
