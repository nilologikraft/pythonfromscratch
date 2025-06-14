import sys
import pickle
from functools import total_ordering
from collections import UserList


def none_or_empty(text):
    return text is None or not text.strip()


def validate_integer_range(question, start, end, default=None):
    while True:
        try:
            entry = input(question)
            if none_or_empty(entry) and default is not None:
                entry = default
            value = int(entry)
            if start <= value <= end:
                return value
        except ValueError:
            print(f"Invalid value, please enter between {start} and {end}")


def validate_integer_range_or_blank(question, start, end):
    while True:
        try:
            entry = input(question)
            if none_or_empty(entry):
                return None
            value = int(entry)
            if start <= value <= end:
                return value
        except ValueError:
            print(f"Invalid value, please enter between {start} and {end}")


class UniqueList(UserList):
    def __init__(self, elem_class, enumerable=None):
        super().__init__(enumerable)
        self.elem_class = elem_class

    def append(self, elem):
        self.verify_type(elem)
        if elem not in self.data:
            super().append(elem)

    def __setitem__(self, posição, elem):
        self.verify_type(elem)
        if elem not in self.data:
            super().__setitem__(posição, elem)

    def verify_type(self, elem):
        if not isinstance(elem, self.elem_class):
            raise TypeError("Invalid Type")

    def search(self, elem):
        self.verify_type(elem)
        try:
            return self.index(elem)
        except ValueError:
            return -1


@total_ordering
class Name:
    def __init__(self, name):
        self.name = name

    def __str__(self):
        return self.name

    def __repr__(self):
        return f"<Class {type(self).__name__} in 0x{id(self):x} Name: {self.__name} Key: {self.__key}>"

    def __eq__(self, other):
        return self.name == other.name

    def __lt__(self, other):
        return self.name < other.name

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, value):
        if none_or_empty(value):
            raise ValueError("Name cannot be None or empty")
        self.__name = value
        self.__key = Name.CreateKey(value)

    @staticmethod
    def CreateKey(name):
        return name.strip().lower()


@total_ordering
class PhoneType:
    def __init__(self, type):
        self.type = type

    def __str__(self):
        return f"({self.type})"

    def __eq__(self, other):
        if other is None:
            return False
        return self.type == other.type

    def __lt__(self, other):
        return self.type < other.type


class Telephone:
    def __init__(self, number, type=None):
        self.number = number
        self.type = type

    def __str__(self):
        type = self.type or ""
        return f"{self.number} {type}"

    def __eq__(self, other):
        return self.number == other.number and (
            (self.type == other.type) or (self.type is None or other.type is None)
        )

    @property
    def number(self):
        return self.__number

    @number.setter
    def number(self, value):
        if none_or_empty(value):
            raise ValueError("Number cannot be None or empty")
        self.__number = value


class Telephones(UniqueList):
    def __init__(self):
        super().__init__(Telephone)


class PhoneTypes(UniqueList):
    def __init__(self):
        super().__init__(PhoneType)


class PhoneData:
    def __init__(self, name):
        self.name = name
        self.telephones = Telephones()

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, value):
        if type(value) != Name:
            raise TypeError("name must be an instance of Name class")
        self.__name = value

    def search_phone(self, phone):
        position = self.telephones.search(Telephone(phone))
        if position == -1:
            return None
        else:
            return self.telephones[position]


class Phonebook(UniqueList):
    def __init__(self):
        super().__init__(PhoneData)
        self.telephone_types = PhoneTypes()

    def add_type(self, type):
        self.telephone_types.append(PhoneType(type))

    def search_name(self, name):
        if isinstance(name, str):
            name = Name(name)
        for data in self:
            if data.name == name:
                return data
        else:
            return None

    def sort(self):
        super().sort(key=lambda data: str(data.name))


class Menu:
    def __init__(self):
        self.options = [["Exit", None]]

    def add_option(self, name, function):
        self.options.append([name, function])

    def show(self):
        print("====")
        print("Menu")
        print("====\n")
        for i, option in enumerate(self.options):
            print(f"[{i}] - {option[0]}")
        print()

    def execute(self):
        while True:
            self.show()
            choice = validate_integer_range(
                "Choose an option: ", 0, len(self.options) - 1
            )
            if choice == 0:
                break
            self.options[choice][1]()


class PhonebookApp:
    @staticmethod
    def ask_name():
        return input("Name: ")

    @staticmethod
    def ask_telephone():
        return input("Phone: ")

    @staticmethod
    def show_data(data):
        print(f"Name: {data.name}")
        for phone in data.telephones:
            print(f"Phone: {phone}")
        print()

    @staticmethod
    def show_phone_data(data):
        print(f"Name: {data.name}")
        for i, phone in enumerate(data.telephones):
            print(f"{i} - Phone: {phone}")
        print()

    @staticmethod
    def ask_filename():
        return input("File name: ")

    def __init__(self):
        self.phonebook = Phonebook()
        self.phonebook.add_type("Cell")
        self.phonebook.add_type("Home")
        self.phonebook.add_type("Work")
        self.phonebook.add_type("Fax")
        self.menu = Menu()
        self.menu.add_option("New", self.new)
        self.menu.add_option("Edit", self.edit)
        self.menu.add_option("Delete", self.delete)
        self.menu.add_option("List", self.list)
        self.menu.add_option("Save", self.save)
        self.menu.add_option("Load", self.load)
        self.menu.add_option("Sort", self.sort)
        self.last_name = None

    def ask_telephone_type(self, default=None):
        for i, type in enumerate(self.phonebook.telephone_types):
            print(f" {i} - {type} ", end=None)
        t = validate_integer_range(
            "Type: ", 0, len(self.phonebook.telephone_types) - 1, default
        )
        return self.phonebook.telephone_types[t]

    def search(self, name):
        data = self.phonebook.search_name(name)
        return data

    def new(self):
        new = PhonebookApp.ask_name()
        if none_or_empty(new):
            return
        name = Name(new)
        if self.search(name) is not None:
            print("Name already exists!")
            return
        record = PhoneData(name)
        self.phone_menu(record)
        self.phonebook.append(record)

    def delete(self):
        if len(self.phonebook) == 0:
            print("Empty phonebook, nothing to delete")
        name = PhonebookApp.ask_name()
        if none_or_empty(name):
            return
        p = self.search(name)
        if p is not None:
            self.phonebook.remove(p)
            print(f"Deleted. The phonebook now has only: {len(self.phonebook)} records")
        else:
            print("Name not found.")

    def edit(self):
        if len(self.phonebook) == 0:
            print("Empty phonebook, nothing to edit")
        name = PhonebookApp.ask_name()
        p = self.search(name)
        if none_or_empty(name):
            return
        if p is not None:
            print("\nFound:\n")
            PhonebookApp.show_data(p)
            print("Enter to keep the same name")
            name = PhonebookApp.ask_name()
            if not none_or_empty(name):
                p.name = Name(name)
            self.phone_menu(p)
        else:
            print("Name not found!")

    def phone_menu(self, data):
        while True:
            print("\nEditing phones\n")
            PhonebookApp.show_phone_data(data)
            if len(data.telephones) > 0:
                print("\n[E] - edit\n[D] - delete\n", end="")
            print("[N] - new\n[X] - exit\n")
            operation = input("Choose an operation: ")
            operation = operation.lower()
            if operation not in ["e", "d", "n", "x"]:
                print("Invalid operation. Enter E, D, N or X")
                continue
            if operation == "e" and len(data.telephones) > 0:
                self.edit_phones(data)
            elif operation == "d" and len(data.telephones) > 0:
                self.delete_phone(data)
            elif operation == "n":
                self.new_phone(data)
            elif operation == "x":
                break

    def new_phone(self, data):
        phone = PhonebookApp.ask_telephone()
        if none_or_empty(phone):
            return
        if data.search_phone(phone) is not None:
            print("Phone already exists")
        type = self.ask_telephone_type()
        data.telephones.append(Telephone(phone, type))

    def delete_phone(self, data):
        t = validate_integer_range_or_blank(
            "Enter the position of the number to delete, enter to exit: ",
            0,
            len(data.telephones) - 1,
        )
        if t is None:
            return
        data.telephones.remove(data.telephones[t])

    def edit_phones(self, data):
        t = validate_integer_range_or_blank(
            "Enter the position of the number to edit, enter to exit: ",
            0,
            len(data.telephones) - 1,
        )
        if t is None:
            return
        phone = data.telephones[t]
        print(f"Phone: {phone}")
        print("Enter to keep the same number")
        telephone_number = PhonebookApp.ask_telephone()
        if not none_or_empty(telephone_number):
            phone.number = telephone_number
        print("Enter to keep the same type")
        phone.type = self.ask_telephone_type(
            self.phonebook.telephone_types.search(phone.type)
        )

    def list(self):
        print("\nPhonebook")
        print("-" * 60)
        for e in self.phonebook:
            PhonebookApp.show_data(e)
        print("-" * 60)

    def load(self, filename=None):
        if filename is None:
            filename = PhonebookApp.ask_filename()
        if none_or_empty(filename):
            return
        with open(filename, "rb") as file:
            self.phonebook = pickle.load(file)
        self.last_name = filename

    def sort(self):
        self.phonebook.sort()
        print("\nPhonebook sorted\n")

    def save(self):
        if self.last_name is not None:
            print(f"Last used name was '{self.last_name}'")
            print("Enter to use the same name")
        filename = PhonebookApp.ask_filename()
        if none_or_empty(filename):
            if self.last_name is not None:
                filename = self.last_name
            else:
                return
        with open(filename, "wb") as file:
            pickle.dump(self.phonebook, file)

    def execute(self):
        self.menu.execute()


if __name__ == "__main__":
    app = PhonebookApp()
    if len(sys.argv) > 1:
        app.load(sys.argv[1])
    app.execute()
