from typing import Union
from .Name import Name
from .Phone import Phone
from .Birthday import Birthday
from .Address import Address
from .Email import Email

class Record:
    def __init__(self, name):
        self.name = Name(name)
        self.phones = []
        self.birthday = None
        self.address = None
        self.emails = []

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
        
    def add_email(self, email: str):
        if (not self.find_email(email)):
            email = Email(email)
            self.emails.append(email)
        else:
            raise KeyError(f'This Email {email} is already exist')

    def remove_email(self, email: str):
        if (self.find_email(email)):
            for i, email_obj in enumerate(self.emails):
                if (email_obj.value == email):
                    del self.emails[i]
                    break
        else:
            raise KeyError(f'This Email {email} is not exist')

    def find_email(self, email: str) -> Union[Email, None]:
        for email_obj in self.emails:
            if (email_obj.value == email):
                return email_obj
        return None

    def edit_email(self, old_email: str, new_email: str):

        old_email_obj = self.find_email(old_email)
        if (old_email_obj):
            old_email_obj.update_value(new_email)
        else:
            raise KeyError(f'This Email {old_email} is not exist')

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
        res = f"Contact name: {self.name.value}, \n {'phones:':<12} {'; '.join(p.value for p in self.phones)}"
        if (self.birthday):
            res += f", \n {'birthday:':<12} {str(self.birthday)}"
        if (self.address):
            res += f", \n {'address:':<12} {str(self.address)}"   
            # res += f", address: {' '.join(p.value for p in self.address)}"            
        if (self.emails):
            res += f", \n {'emails:':<12} {'; '.join(p.value for p in self.emails)}"
        return res
