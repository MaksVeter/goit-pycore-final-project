from .Field import Field
import re


class Email(Field):

    def __init__(self, value: str):
        if (self.__validate_email(value)):
            super().__init__(value)
        else:
            raise ValueError('Email string must be like text@text.text')

    def __validate_email(self, value: str) -> bool:
        return bool(re.match(r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$', value))

    def update_value(self, value: str):
        if (value == self.value):
            raise ValueError('The emails shouln\'t be the same')
        if (self.__validate_email(value)):
            self.value = value
        else:
            raise ValueError('Email string must be like text@text.text')