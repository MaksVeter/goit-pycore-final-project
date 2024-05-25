
  

# Contact and Note Management Console Bot

  

  

## Загальний опис

  

  

Цей проект реалізує консольного бота на Python, який дозволяє керувати контактами та нотатками. Ви можете додавати, редагувати, видаляти контакти (з телефонами, адресою, електронною поштою) а також створювати, редагувати, видаляти, шукати текстові нотатки. Стан контактів та нотаток зберігається між запусками бота у поточній директорії.

  

  

## Інструкція з використання

  

  

### Вимоги

  

  

- Python 3.6 або новіша версія

  

-  `colorama` бібліотека

  

  
### Встановлення та запуск як пакет
1. Клонуйте репозиторій:

```bash
git clone  https://github.com/MaksVeter/goit-pycore-final-project
```

2. Перейдіть у директорію проекту:

```bash
cd goit-pycore-final-project
```

3. Ініціюйте та активуйте Venv
```bash
python3 -m venv .venv
# активація в залежності від ОС
source .venv/bin/activate # для Mac
.\.venv\Scripts\activate.bat # для Windows CMD
.\.venv\Scripts\Activate.ps1 # для Windows PowerShell
```

4. Встановіть пакет

```bash
pip install -e .
```

5. Бот буде доступний за командою

```bash
contactsbot
```



### Встановлення та запуск як модуль

1. Клонуйте репозиторій:

```bash
git clone  https://github.com/MaksVeter/goit-pycore-final-project
```

2. Перейдіть у директорію проекту:

```bash
cd goit-pycore-final-project
```

3. Встановіть необхідні бібліотеки:

```bash
pip install  -r  requirements.txt
```

4. Запустіть бота:

```bash
python3 src/main.py
```

  

### Використання

  

1. Список доступних команд

  

```bash
List of commands
1.  hello  say hello to the assistant
2.  add [contact_name] [phone_number]  adds contact name and phone number to memory
3.  change [contact_name] [old_phone_number] [new_phone_number]  edits the contact's phone number
4.  phone [contact_name]  displays the contact(\')s phone number
5.  all  show contacts phone book
6.  search [search_term]  search contacts by name
7.  delete [contact_name]  delete contact by name
8.  close  or  exit  exit from the assistant
9.  add-birthday [contact_name] [day_of_birthday]  add birthday of contact name
10. show-birthday [contact_name]  display day of birth
11. birthdays  show birthdays that will happen in the next week
12. add-email [contact_name] [email]  adds email of contact name
13. change-email [contact_name] [old_email] [new_email]  edits the contact's email
14. email [contact_name]  displays the contact's emails
15. add-address [contact_name] [address]  adds address of contact name
16. change-address [contact_name] [new_address]  edits the contact's address
17. note-add  add text note
18. note-show  show all notes
19. note-change [note_id]  change note by ID
20. note-delete [note_id]  delete note by ID
21. note-delete-all  delete note by ID
22. note-search [search_term]  search in all notes
23. help  help page
```

  

2. Приклад взаємодії

  

Додаємо і переглянемо контакти:

```bash

Enter a  command:  add  Антон  1234567890

Contact added.

Enter a  command:  add_phone  Антон  2345678901

Contact updated.  Phone  added.

Enter a  command:  add-email  Антон  email@domain.com

Contact updated.  Email  added.

Enter a  command:  add-birthday  Антон  29.05.2024

Contact updated.  Birthday  added.

Enter a  command:  add-address  Антон  Україна,  Київ,  пр-кт  Берестейський

Contact updated.  Address  added.

Enter a  command:  all

Contact name: Антон, 
 phones:      1234567890; 2345678901, 
 birthday:    29.05.2024, 
 address:     Україна, Київ, пр-кт Берестейський, 
 emails:      email@domain.com; email2@domain.com

Enter a  command:  search  Антон

Contact name: Антон, 
 phones:      1234567890; 2345678901, 
 birthday:    29.05.2024, 
 address:     Україна, Київ, пр-кт Берестейський, 
 emails:      email@domain.com; email2@domain.com

```

  

## Команда і ролі

  

  

-  **Scrum Master: @valeriia1421**: Регулює термін виконання проєкту. Здійснює щоденний Stand Up для планування роботи команди. Слідкує за наявністю завдань у всіх учасників команди та термінами їх реалізації.

  

-  **Team Lead @MaksVeter**: Стежить за технічною реалізацією проєкту, відповідає за якість коду, пише код ревью та завдання щодо проекту для учасників команди. Є власником репозиторію за командним проєктом.

  

-  **Developer @PavloRohozhyn**: Займається технічною реалізацією функцій проєкту.

  

-  **Developer @sazhukov**: Займається технічною реалізацією функцій проєкту.

  

  

## Контакти

  

  

Для будь-яких запитань або пропозицій, будь ласка, звертайтесь до команди проекту.