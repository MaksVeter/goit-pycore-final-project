"""Contact Field type Address"""
import re

from .Field import Field


class Address(Field):
    """Contact Field type Address class"""

    def __init__(self, value: str):
        if self.__validate_address(value):
            super().__init__(value)
        else:
            raise ValueError(
                'Address string should contain from 10 to 150 symbols')

    def __validate_address(self, value: str) -> bool:
        return bool(re.match(r'^.{10,150}$', value))

    def update_value(self, value: str):
        """method to update field value"""
        if value == self.value:
            raise ValueError('The address shouln\'t be the same')
        if self.__validate_address(value):
            self.value = value
        else:
            raise ValueError('Address string should contain minimum 3 words')
