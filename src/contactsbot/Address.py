from .Field import Field
import re


class Address(Field):

    def __init__(self, value: str):
        if (self.__validate_address(value)):
            super().__init__(value)
        else:
            raise ValueError('Address string should contain from 10 to 150 symbols')

    def __validate_address(self, value: str) -> bool:
        return bool(re.match(r'^.{10,150}$', value))

    def update_value(self, value: str):
        if (value == self.value):
            raise ValueError('The address shouln\'t be the same')
        if (self.__validate_address(value)):
            self.value = value
        else:
            raise ValueError('Address string should contain minimum 3 words')