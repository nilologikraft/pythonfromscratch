##############################################################################
# Python From Scratch
# Author: Nilo Ney Coutinho Menezes
# Editora Novatec (c) 2010-2025 - LogiKraft 2025
# Site: https://pythonfromscratch.com
# ISBN: 978-85-7522-949-1 (Paperback), 978-85-7522-950-7 (hardcover), 978-85-7522-951-4 (ebook)
#
# File: chapter 09/exercise-09-28.py.py
##############################################################################
# As the file format becomes increasingly complex,
# we'll use Python's pickle module to save and read the address book.
#
# Extra challenge:
# Modify the program to display a phone management submenu.
# This submenu would be displayed when adding and changing phones.
# Operations: add new phone, delete phone, change phone
import pickle

address_book = []

# Variable to mark a change in the address book
changed = False

phone_types = ["mobile", "landline", "home", "work", "fax"]


def ask_name(default=""):
    name = input("Name: ")
    if name == "":
        name = default
    return name


def ask_phone(default=""):
    phone = input("Phone: ")
    if phone == "":
        phone = default
    return phone


def ask_phone_type(default=""):
    while True:
        type = input("Phone type [%s]: " % ",".join(phone_types)).lower()
        if type == "":
            type = default
        for t in phone_types:
            if t.startswith(type):
                return t  # Returns the full name
        else:
            print("Invalid phone type!")


def ask_email(default=""):
    email = input("Email: ")
    if email == "":
        email = default
    return email


def ask_birthday(default=""):
    birthday = input("Birthday: ")
    if birthday == "":
        birthday = default
    return birthday


def show_data(name, phones, email, birthday):
    print(f"Name: {name.capitalize()}")
    print("Phone(s):")
    for phone in phones:
        print(f"\tNumber: {phone[0]:15s} Type: {phone[1].capitalize()}")
    print(f"Email: {email}\nBirthday: {birthday}\n")


def ask_filename():
    return input("File name: ")


def search(name):
    mname = name.lower()
    for p, e in enumerate(address_book):
        if e[0].lower() == mname:
            return p
    return None


def new():
    global address_book, changed
    name = ask_name()
    if search(name) is not None:
        print("Name already exists!")
        return
    phones = []
    while True:
        number = ask_phone()
        type = ask_phone_type()
        phones.append([number, type])
        if confirm("that you want to register another phone") == "N":
            break
    email = ask_email()
    birthday = ask_birthday()
    address_book.append([name, phones, email, birthday])
    changed = True


def confirm(operation):
    while True:
        option = input(f"Confirm {operation} (Y/N)? ").upper()
        if option in "YN":
            return option
        else:
            print("Invalid response. Choose Y or N.")


def delete():
    global address_book, changed
    name = ask_name()
    p = search(name)
    if p is not None:
        if confirm("deletion") == "Y":
            del address_book[p]
            changed = True
    else:
        print("Name not found.")


def change():
    global changed
    p = search(ask_name())
    if p is not None:
        name, phones, email, birthday = address_book[p]
        print("Found:")
        show_data(name, phones, email, birthday)
        name = ask_name(name)  # If nothing is entered, keeps the value
        for phone in phones:
            number, type = phone
            phone[0] = ask_phone(number)
            phone[1] = ask_phone_type(type)
        email = ask_email(email)
        birthday = ask_birthday(birthday)
        if confirm("change") == "Y":
            address_book[p] = [name, phones, email, birthday]
            changed = True
    else:
        print("Name not found.")


def list():
    print("\nAddress Book\n\n------")
    # We use the enumerate function to get the position in the address book
    for position, e in enumerate(address_book):
        # Print the position
        print(f"\nPosition: {position}")
        show_data(e[0], e[1], e[2], e[3])
    print("------\n")


def read_last_saved_address_book():
    last = last_address_book()
    if last is not None:
        read_file(last)


def last_address_book():
    try:
        file = open("last address book pickle.dat", "r", encoding="utf-8")
        last = file.readline()[:-1]
        file.close()
    except FileNotFoundError:
        return None
    return last


def update_last(name):
    file = open("last address book pickle.dat", "w", encoding="utf-8")
    file.write(f"{name}\n")
    file.close()


def read_file(filename):
    global address_book, changed
    file = open(filename, "rb")
    address_book = pickle.load(file)
    file.close()
    changed = False


def read():
    global changed
    if changed:
        print(
            "You haven't saved the list since the last change. Do you want to save it now?"
        )
        if confirm("saving") == "Y":
            save()
    print("Read\n---")
    filename = ask_filename()
    read_file(filename)
    update_last(filename)


def sort():
    global changed
    # You can sort the list as shown in the book
    # with the bubble sort method
    # Or combine Python's sort method with lambdas to
    # define the list key
    # address_book.sort(key=lambda e: return e[0])
    end = len(address_book)
    while end > 1:
        i = 0
        swapped = False
        while i < (end - 1):
            if address_book[i] > address_book[i + 1]:
                # Option: address_book[i], address_book[i+1] = address_book[i+1], address_book[i]
                temp = address_book[i + 1]
                address_book[i + 1] = address_book[i]
                address_book[i] = temp
                swapped = True
            i += 1
        if not swapped:
            break
    changed = True


def save():
    global changed
    if not changed:
        print("You haven't changed the list. Do you want to save it anyway?")
        if confirm("saving") == "N":
            return
    print("Save\n------")
    filename = ask_filename()

    file = open(filename, "wb")
    pickle.dump(address_book, file)
    file.close()
    update_last(filename)
    changed = False


def validate_integer_range(question, start, end):
    while True:
        try:
            value = int(input(question))
            if start <= value <= end:
                return value
        except ValueError:
            print(f"Invalid value, please enter between {start} and {end}")


def menu():
    print(
        """
   1 - New
   2 - Change
   3 - Delete
   4 - List
   5 - Save
   6 - Read
   7 - Sort by name

   0 - Exit
"""
    )
    print(f"\nNames in address book: {len(address_book)} Changed: {changed}\n")
    return validate_integer_range("Choose an option: ", 0, 7)


read_last_saved_address_book()

while True:
    option = menu()
    if option == 0:
        break
    elif option == 1:
        new()
    elif option == 2:
        change()
    elif option == 3:
        delete()
    elif option == 4:
        list()
    elif option == 5:
        save()
    elif option == 6:
        read()
    elif option == 7:
        sort()
