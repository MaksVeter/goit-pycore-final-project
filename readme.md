
# Contact and Note Management Console Bot

  

## Загальний опис

  

Цей проект реалізує консольного бота на Python, який дозволяє керувати контактами та нотатками. Ви можете додавати, редагувати, видаляти контакти (з телефонами, адресою, електронною поштою) а також створювати, редагувати, видаляти, шукати текстові нотатки.

  

## Інструкція з використання

  

### Вимоги

  

- Python 3.6 або новіша версія

-  `colorama` бібліотека

  

### Встановлення та запуск

  

1. Клонуйте репозиторій:

```bash

git clone https://github.com/MaksVeter/goit-pycore-final-project

```

  

2. Перейдіть у директорію проекту:

```bash

cd goit-pycore-final-project

```

  

3. Встановіть необхідні бібліотеки:

```bash

pip install -r requirements.txt

```
4. Запустіть бота:

```bash

python src/main.py

```

### Використання

 1. Список доступних команд 

```bash

List of commands
1. hello  say hello to the assistant
2. add [contact_name] [phone_number]  adds contact name and phone number to memory
3. change [contact_name] [old_phone_number] [new_phone_number]  edits the contacts phone number
4. phone [contact_name]  displays the contacts phone number
5. all  show contacts phone book
6. close  or  exit  exit from the assistant
7. add-birthday [contact_name] [day_of_birthday]  add birthday of contact name
8. show-birthday [contact_name]  display day of birth
9. birthdays  show birthdays that will happen in the next week
10. add_email [contact_name] [email_number]  adds email of contact name
11. change_email [contact_name] [old_email_number] [new_email_number]  edits the contacts email
12. email [contact_name]  displays the contacts emails
13. note-add  add text note
14. note-show  show all notes
15. help  help page

```

2. Приклад взаємодії

Додаємо і переглянемо контакти:
```bash 
Enter a command: add Антон 1234567890
Contact added.
Enter a command: add_phone Антон 2345678901
Contact updated. Phone added.
Enter a command: add-email Антон email@domain.com
Contact updated. Email added.
Enter a command: add-birthday Антон 29.05.2024
Contact updated. Birthday added.
Enter a command: add-address Антон Україна, Київ, пр-кт Берестейський
Contact updated. Address added.
Enter a command: all 
Contact name: Антон, phones: 1234567890; 2345678901, birthday: 29.05.2024, address: Україна, Київ, пр-кт Берестейський, emails: email@domain.com
Enter a command: search Антон
Contact name: Антон, phones: 1234567890; 2345678901, birthday: 29.05.2024, address: Україна, Київ, пр-кт Берестейський, emails: email@domain.com
```
  

## Команда і ролі

  

- **Scrum Master: @valeriia1421**: Регулює термін виконання проєкту. Здійснює щоденний Stand Up для планування роботи команди. Слідкує за наявністю завдань у всіх учасників команди та термінами їх реалізації.

- **Team Lead @MaksVeter**: Стежить за технічною реалізацією проєкту, відповідає за якість коду, пише код ревью та завдання щодо проекту для учасників команди. Є власником репозиторію за командним проєктом.

- **Developer @PavloRohozhyn**: Займається технічною реалізацією функцій проєкту.

- **Developer @sazhukov**: Займається технічною реалізацією функцій проєкту.

  

## Контакти

  

Для будь-яких запитань або пропозицій, будь ласка, звертайтесь до команди проекту.