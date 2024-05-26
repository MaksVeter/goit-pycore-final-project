"""Contact Field type Phone"""
import re

from .Field import Field


class Phone(Field):
    """Contact Field type Phone"""

    def __init__(self, value: str):
        if self.__validate_phone(value):
            super().__init__(value)
        else:
            raise ValueError('Phone string should contain 10 digits')

    def __validate_phone(self, value: str) -> bool:
        return bool(re.match(r'^\d{10}$', value))

    def update_value(self, value: str):
        """update field value mthod"""
        if value == self.value:
            raise ValueError('The phones shouln\'t be the same')
        if self.__validate_phone(value):
            self.value = value
        else:
            raise ValueError('Phone string should contain 10 digits')
