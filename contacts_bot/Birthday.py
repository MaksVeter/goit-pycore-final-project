from datetime import datetime
from .Field import Field


class Birthday(Field):

    def __init__(self, value: str):
        try:
            birthday = datetime.strptime(value, '%d.%m.%Y')
            super().__init__(birthday)
        except ValueError:
            raise ValueError("Invalid date format. Use DD.MM.YYYY")

    def _validate_birthday(self, value: datetime):
        now = datetime.now()
        return now < value
    
    def __str__(self):
        if(self.value):
            return self.value.strftime('%d.%m.%Y')
        else:
            return ''
    