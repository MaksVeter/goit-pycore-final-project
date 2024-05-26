"""state manager with pickle methods"""
import pickle
from .AddressBook import AddressBook
from .Notes import Notes


def save_data(data, filename="addressbook.pkl"):
    """save data to pickle file"""
    with open(filename, "wb") as f:
        pickle.dump(data, f)


def load_data(filename="addressbook.pkl"):
    """load data from pickle file"""
    try:
        with open(filename, "rb") as f:
            return pickle.load(f)
    except FileNotFoundError:
        if filename == 'addressbook.pkl':
            return AddressBook()
        return Notes()
