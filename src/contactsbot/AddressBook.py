from collections import UserDict
from datetime import datetime, timedelta
from typing import Union
from .Record import Record


class AddressBook(UserDict):
    def add_record(self, record: Record):
        if (not self.__exists(record.name)):
            self.data[record.name.value] = record
        else:
            raise KeyError(f'Record with name "{
                           record.name}" is already exist')

    def find(self, name: str) -> Record:
        if (self.__exists(name)):
            return self.data[name]
        else:
            raise KeyError(f'Record with name "{name}" is not exist')

    def delete(self, name: str):
        if (self.__exists(name)):
            del self.data[name]
        else:
            raise KeyError(f'Record with name "{name}" is not exist')

    def __exists(self, name: str) -> bool:
        return name in self.data


    @staticmethod
    def check_potential_congrats_date(date: datetime, now: datetime) -> Union[datetime, None]:
        congratulation_date = None
        # check if date is weekend and move it to next monday
        if date.weekday() > 4:
            date = date + timedelta(days=(7-date.weekday()))

        # check if date is in 7 days range from today
        if (0 <= (date-now).days < 7):
            congratulation_date = date

        return congratulation_date

    # @todo update
    def get_upcoming_birthdays(self) -> list:
        now_date = datetime.today()
        format = "%d.%m.%Y"
        res = []
        for name, record in self.data.items():
            congratulation_date = None
            if (record.birthday):
                user_birth_date = record.birthday.value
                # use current and next years to check to cover cases when today is the end of the year
                for case in range(0, 1):
                    user_potential_congrat_date = user_birth_date.replace(
                        year=(now_date.year+case))
                    congratulation_date = AddressBook.check_potential_congrats_date(
                        user_potential_congrat_date, now_date)
                    if (congratulation_date):
                        break

                if congratulation_date:
                    res.append(
                        {"name": name, 'congratulation_date': congratulation_date.strftime(format)})

        return res

    def __str__(self) -> str:
        return '\n'.join(str(record) for record in self.data.values())
