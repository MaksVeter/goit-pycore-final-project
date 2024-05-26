"""Contacts dict class"""
from collections import UserDict
from datetime import datetime, timedelta
import re
from typing import Union
from .Record import Record


class AddressBook(UserDict):
    """Contact dict class"""

    def add_record(self, record: Record):
        """Add new record method"""
        if (not self.__exists(record.name)):
            self.data[record.name.value] = record
        else:
            raise KeyError(f'Record with name "{
                           record.name}" is already exist')

    def find(self, name: str) -> Record:
        """Find the record by name method"""
        if (self.__exists(name)):
            return self.data[name]
        else:
            raise KeyError(f'Record with name "{name}" is not exist')

    def find_like(self, search_term: str) -> Record:
        """Search records by search term method"""
        pattern = re.compile(search_term, re.IGNORECASE)
        matches = {key: value for key, value in self.data.items()
                   if pattern.search(key)}
        if matches:
            return matches
        raise KeyError(f'Record with name "{search_term}" is not exist')

    def delete(self, name: str):
        """Delete record by name method"""
        if (self.__exists(name)):
            del self.data[name]
        else:
            raise KeyError(f'Record with name "{name}" is not exist')

    def __exists(self, name: str) -> bool:
        return name in self.data

    @staticmethod
    def check_potential_congrats_date(date: datetime, now: datetime, days) -> Union[datetime, None]:
        """Check if the date is in days from another date static method"""
        congratulation_date = None
        # check if date is weekend and move it to next monday
        if date.weekday() > 4:
            date = date + timedelta(days=(7-date.weekday()))

        # check if date is in 7 days range from today
        if 0 <= (date-now).days < days:
            congratulation_date = date

        return congratulation_date

    # @todo update
    def get_upcoming_birthdays(self, days=7) -> list:
        """Search for records with birthday in days from now method"""
        now_date = datetime.today()
        date_format = "%d.%m.%Y"
        res = []
        for name, record in self.data.items():
            congratulation_date = None
            if record.birthday:
                user_birth_date = record.birthday.value
                # use current and next years to check to cover cases
                # when today is the end of the year
                for case in range(0, 1):
                    user_potential_congrat_date = user_birth_date.replace(
                        year=now_date.year+case)
                    congratulation_date = AddressBook.check_potential_congrats_date(
                        user_potential_congrat_date, now_date, days)
                    if congratulation_date:
                        break

                if congratulation_date:
                    res.append(
                        {
                            "name": name,
                            "congratulation_date": congratulation_date.strftime(date_format)
                        })

        return res

    def __str__(self) -> str:
        return '\n'.join(str(record) for record in self.data.values())
