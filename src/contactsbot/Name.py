"""Contact Field type Name"""
from .Field import Field


class Name(Field):
    """Contact Field type Name class"""

    def __init__(self, value:str): # pylint: disable=W0246
        super().__init__(value)
