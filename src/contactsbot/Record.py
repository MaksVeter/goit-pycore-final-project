from typing import Union
from .Name import Name
from .Phone import Phone
from .Birthday import Birthday
from .Address import Address


class Record:
    def __init__(self, name):
        self.name = Name(name)
        self.phones = []
        self.birthday = None
        self.address = None

    def add_phone(self, phone: str):
        if (not self.find_phone(phone)):
            phone = Phone(phone)
            self.phones.append(phone)
        else:
            raise KeyError(f'This Phone {phone} is already exist')

    def remove_phone(self, phone: str):
        if (self.find_phone(phone)):
            for i, phone_obj in enumerate(self.phones):
                if (phone_obj.value == phone):
                    del self.phones[i]
                    break
        else:
            raise KeyError(f'This Phone {phone} is not exist')

    def find_phone(self, phone: str) -> Union[Phone, None]:
        for phone_obj in self.phones:
            if (phone_obj.value == phone):
                return phone_obj
        return None

    def edit_phone(self, old_phone: str, new_phone: str):

        old_phone_obj = self.find_phone(old_phone)
        if (old_phone_obj):
            old_phone_obj.update_value(new_phone)
        else:
            raise KeyError(f'This Phone {old_phone} is not exist')

    def add_birthday(self, birthday: str):
        birthday_obj = Birthday(birthday)
        self.birthday = birthday_obj
        
    def add_address(self, address: str):
        if (self.address == None):
            address_obj = Address(address)
            self.address = address_obj
        else:
            raise KeyError(f'This Record already has address')
        # address_obj = Address(address)
        # self.address = address_obj
    
    def edit_address(self, address: str):
        address_obj = Address(address)
        self.address = address_obj

    def __str__(self) -> str:
        res = f"Contact name: {self.name.value}, phones: {
            '; '.join(p.value for p in self.phones)}"
        if (self.birthday):
            res += f", birthday: {str(self.birthday)}"
        if (self.address):
            res += f", address: {str(self.address)}"   
            # res += f", address: {' '.join(p.value for p in self.address)}"
            
        return res
