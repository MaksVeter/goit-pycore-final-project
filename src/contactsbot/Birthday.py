"""Contact Field type Birthday"""
from datetime import datetime
from .Field import Field


class Birthday(Field):
    """Contact Field type Birthday class"""

    def __init__(self, value: str):
        try:
            birthday = datetime.strptime(value, '%d.%m.%Y')
            super().__init__(birthday)
        except ValueError:
            raise ValueError(  # pylint: disable=W0707
                "Invalid date format. Use DD.MM.YYYY")  # pylint: disable=W0707

    def _validate_birthday(self, value: datetime):
        now = datetime.now()
        return now < value

    def __str__(self):
        if self.value:
            return self.value.strftime('%d.%m.%Y')
        return ''
