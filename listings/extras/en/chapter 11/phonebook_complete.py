import sys
import sqlite3
import os.path
from functools import total_ordering
from collections import UserList

DATABASE = """
create table types(id integer primary key autoincrement,
                   description text);
create table names(id integer primary key autoincrement,
                   name text);
create table telephones(id integer primary key autoincrement,
                        id_name integer,
                        number text,
                        id_type integer);
insert into types(description) values ("Cell");
insert into types(description) values ("Landline");
insert into types(description) values ("Fax");
insert into types(description) values ("Home");
insert into types(description) values ("Work");
"""


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

    def __setitem__(self, position, elem):
        self.verify_type(elem)
        if elem not in self.data:
            super().__setitem__(position, elem)

    def verify_type(self, elem):
        if not isinstance(elem, self.elem_class):
            raise TypeError("Invalid type")

    def search(self, elem):
        self.verify_type(elem)
        try:
            return self.index(elem)
        except ValueError:
            return -1


class DBUniqueList(UniqueList):
    def __init__(self, elem_class):
        super().__init__(elem_class)
        self.deleted = []

    def remove(self, elem):
        if elem.id is not None:
            self.deleted.append(elem.id)
        super().remove(elem)

    def clear(self):
        self.deleted = []


@total_ordering
class Name:
    def __init__(self, name):
        self.name = name

    def __str__(self):
        return self.name

    def __repr__(self):
        return "<Class {3} in 0x{0:x} Name: {1} Key: {2}>".format(
            id(self), self.__name, self.__key, type(self).__name__
        )

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

    @property
    def key(self):
        return self.__key

    @staticmethod
    def CreateKey(name):
        return name.strip().lower()


class DBName(Name):
    def __init__(self, name, id_=None):
        super().__init__(name)
        self.id = id_


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


class DBPhoneType(PhoneType):
    def __init__(self, id_, type):
        super().__init__(type)
        self.id = id_


class Telephone:
    def __init__(self, number, type=None):
        self.number = number
        self.type = type

    def __str__(self):
        type_ = self.type or ""
        return f"{self.number} {type_}"

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


class DBTelephone(Telephone):
    def __init__(self, number, type=None, id_=None, id_name=None):
        super().__init__(number, type)
        self.id = id_
        self.id_name = id_name


class DBTelephones(DBUniqueList):
    def __init__(self):
        super().__init__(DBTelephone)


class DBPhoneTypes(UniqueList):
    def __init__(self):
        super().__init__(DBPhoneType)


class DBPhoneData:
    def __init__(self, name):
        self.name = name
        self.phones = DBTelephones()

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, value):
        if not isinstance(value, DBName):
            raise TypeError("name must be an instance of DBName")
        self.__name = value

    def search_phone(self, phone):
        position = self.phones.search(DBTelephone(phone))
        if position == -1:
            return None
        else:
            return self.phones[position]


class DBPhonebook:
    def __init__(self, database):
        self.phoneTypes = DBPhoneTypes()
        self.database = database
        is_new = not os.path.isfile(database)
        self.connection = sqlite3.connect(database)
        self.connection.row_factory = sqlite3.Row
        if is_new:
            self.create_database()
        self.load_types()

    def load_types(self):
        for type_ in self.connection.execute("select * from types"):
            id_ = type_["id"]
            description = type_["description"]
            self.phoneTypes.append(DBPhoneType(id_, description))

    def create_database(self):
        self.connection.executescript(DATABASE)

    def search_name(self, name):
        if not isinstance(name, DBName):
            raise TypeError("name must be of type DBName")
        found = self.connection.execute(
            """select count(*) from names where name = ?""",
            (name.name,),
        ).fetchone()
        if found[0] > 0:
            return self.load_by_name(name)
        else:
            return None

    def load_by_id(self, id):
        query = self.connection.execute("select * from names where id = ?", (id,))

        return self.load(query.fetchone())

    def load_by_name(self, name):
        query = self.connection.execute(
            "select * from names where name = ?", (name.name,)
        )
        return self.load(query.fetchone())

    def load(self, record):
        if record is None:
            return None
        new = DBPhoneData(DBName(record["name"], record["id"]))
        for phone in self.connection.execute(
            "select * from telephones where id_name = ?", (new.name.id,)
        ):
            phone_number = DBTelephone(
                phone["number"], None, phone["id"], phone["id_name"]
            )
            for type_ in self.phoneTypes:
                if type_.id == phone["id_type"]:
                    phone_number.type = type_
                    break
            new.phones.append(phone_number)
        return new

    def list(self):
        query = self.connection.execute("select * from names order by name")
        for record in query:
            yield self.load(record)

    def new_record(self, record):
        try:
            cur = self.connection.cursor()
            cur.execute("insert into names(name) values (?)", (str(record.name),))
            record.name.id = cur.lastrowid
            for phone in record.phones:
                cur.execute(
                    """insert into telephones(number,
                               id_type, id_name) values (?,?,?)""",
                    (phone.number, phone.type.id, record.name.id),
                )
                phone.id = cur.lastrowid
            self.connection.commit()
        except:
            self.connection.rollback()
            raise
        finally:
            cur.close()

    def update(self, record):
        try:
            cur = self.connection.cursor()
            cur.execute(
                "update names set name=? where id = ?",
                (str(record.name), record.name.id),
            )
            for phone in record.phones:
                if phone.id is None:
                    cur.execute(
                        """insert into telephones(number,
                                   id_type, id_name)
                                   values (?,?,?)""",
                        (phone.number, phone.type.id, record.name.id),
                    )
                    phone.id = cur.lastrowid
                else:
                    cur.execute(
                        """update telephones set number=?,
                                          id_type=?, id_name=?
                                          where id = ?""",
                        (
                            phone.number,
                            phone.type.id,
                            record.name.id,
                            phone.id,
                        ),
                    )
            for deleted in record.phones.deleted:
                cur.execute("delete from telephones where id = ?", (deleted,))
            self.connection.commit()
            record.phones.clear()
        except:
            self.connection.rollback()
            raise
        finally:
            cur.close()

    def delete(self, record):
        try:
            cur = self.connection.cursor()
            cur.execute("delete from telephones where id_name = ?", (record.name.id,))
            cur.execute("delete from names where id = ?", (record.name.id,))
            self.connection.commit()
        except:
            self.connection.rollback()
            raise
        finally:
            cur.close()


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
            option = validate_integer_range(
                "Choose an option: ", 0, len(self.options) - 1
            )
            if option == 0:
                break
            self.options[option][1]()


class PhonebookApp:

    @staticmethod
    def ask_name():
        return input("Name: ")

    @staticmethod
    def ask_phone():
        return input("Phone: ")

    @staticmethod
    def show_data(data):
        print(f"Name: {data.name}")
        for phone in data.phones:
            print(f"Phone: {phone}")
        print()

    @staticmethod
    def show_phone_data(data):
        print(f"Name: {data.name}")
        for i, phone in enumerate(data.phones):
            print(f"{i} - Phone: {phone}")
        print()

    def __init__(self, database):
        self.phonebook = DBPhonebook(database)
        self.menu = Menu()
        self.menu.add_option("New", self.new)
        self.menu.add_option("Edit", self.edit)
        self.menu.add_option("Delete", self.delete)
        self.menu.add_option("List", self.list)
        self.last_name = None

    def ask_phone_type(self, default=None):
        for i, type_ in enumerate(self.phonebook.phoneTypes):
            print(f" {i} - {type_} ", end=None)
        type_ = validate_integer_range(
            "Type: ", 0, len(self.phonebook.phoneTypes) - 1, default
        )
        return self.phonebook.phoneTypes[type_]

    def search(self, name):
        if isinstance(name, str):
            name = DBName(name)
        data = self.phonebook.search_name(name)
        return data

    def new(self):
        new_name = PhonebookApp.ask_name()
        if none_or_empty(new_name):
            return
        name = DBName(new_name)
        if self.search(name) is not None:
            print("Name already exists!")
            return
        record = DBPhoneData(name)
        self.menu_phones(record)
        self.phonebook.new_record(record)

    def delete(self):
        name = PhonebookApp.ask_name()
        if none_or_empty(name):
            return
        data = self.search(name)
        if data is not None:
            self.phonebook.delete(data)
        else:
            print("Name not found.")

    def edit(self):
        name = PhonebookApp.ask_name()
        if none_or_empty(name):
            return
        data = self.search(name)
        if data is not None:
            print("\nFound:\n")
            PhonebookApp.show_data(data)
            print("Press enter if you don't want to change the name")
            new_name = PhonebookApp.ask_name()
            if not none_or_empty(new_name):
                data.name.name = new_name
            self.menu_phones(data)
            self.phonebook.update(data)
        else:
            print("Name not found!")

    def menu_phones(self, data):
        while True:
            print("\nEditing phones\n")
            PhonebookApp.show_phone_data(data)
            if len(data.phones) > 0:
                print("\n[E] - edit\n[D] - delete\n", end="")
            print("[N] - new\n[X] - exit\n")
            operation = input("Choose an operation: ")
            operation = operation.lower()
            if operation not in ["e", "d", "n", "x"]:
                print("Invalid operation. Enter E, D, N, or X")
                continue
            if operation == "e" and len(data.phones) > 0:
                self.edit_phones(data)
            elif operation == "d" and len(data.phones) > 0:
                self.delete_phone(data)
            elif operation == "n":
                self.new_phone(data)
            elif operation == "x":
                break

    def new_phone(self, data):
        phone = PhonebookApp.ask_phone()
        if none_or_empty(phone):
            return
        if data.search_phone(phone) is not None:
            print("Phone already exists")
        type_ = self.ask_phone_type()
        data.phones.append(DBTelephone(phone, type_))

    def delete_phone(self, data):
        to_be_deleted = validate_integer_range_or_blank(
            "Enter the position of the number to delete, press enter to exit: ",
            0,
            len(data.phones) - 1,
        )
        if to_be_deleted is None:
            return
        data.phones.remove(data.phones[to_be_deleted])

    def edit_phones(self, data):
        to_be_edited = validate_integer_range_or_blank(
            "Enter the position of the number to edit, press enter to exit: ",
            0,
            len(data.phones) - 1,
        )
        if to_be_edited is None:
            return
        phone = data.phones[to_be_edited]
        print(f"Phone: {phone}")
        print("Press enter if you don't want to edit the number")
        new_phone = PhonebookApp.ask_phone()
        if not none_or_empty(new_phone):
            phone.number = new_phone
        print("Press enter if you don't want to edit the type")
        phone.type = self.ask_phone_type(self.phonebook.phoneTypes.search(phone.type))

    def list(self):
        print("\nPhonebook")
        print("-" * 60)
        for e in self.phonebook.list():
            PhonebookApp.show_data(e)
        print("-" * 60)

    def execute(self):
        self.menu.execute()


if __name__ == "__main__":
    if len(sys.argv) > 1:
        app = PhonebookApp(sys.argv[1])
        app.execute()
    else:
        print("Error: database name not provided")
        print("Usage phonebook.py database_name")
