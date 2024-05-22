from .Field import Field
import re


class Address(Field):

    def __init__(self, value: str):
        if (self.__validate_address(value)):
            super().__init__(value)
        else:
            raise ValueError('Address string should contain symbols and digits')

    def __validate_address(self, value: str) -> bool:
        return bool(re.match(r"(?P<text>[a-zA-Z]+)(?P<digits>\d+)", value))

    def update_value(self, value: str):
        if (value == self.value):
            raise ValueError('The address shouln\'t be the same')
        if (self.__validate_address(value)):
            self.value = value
        else:
            raise ValueError('Address string should contain symbols and digits')