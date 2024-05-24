import pickle
from .AddressBook import AddressBook
from .Notes import Notes


def save_data(data, filename="addressbook.pkl"):
    with open(filename, "wb") as f:
        pickle.dump(data, f)


def load_data(filename="addressbook.pkl"):
    try:
        with open(filename, "rb") as f:
            return pickle.load(f)
    except FileNotFoundError:
        if filename == 'addressbook.pkl':
            return AddressBook()
        else:
            return Notes()
