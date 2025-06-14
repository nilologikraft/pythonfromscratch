##############################################################################
# Python From Scratch
# Author: Nilo Ney Coutinho Menezes
# Editora Novatec (c) 2010-2025 - LogiKraft 2025
# Site: https://pythonfromscratch.com
# ISBN: 978-85-7522-949-1 (Paperback), 978-85-7522-950-7 (hardcover), 978-85-7522-951-4 (ebook)
#
# File: chapter 09/exercise-09-39.py.py
##############################################################################
import json

contacts = []


def ask_name():
    return input("Name: ")


def ask_phone():
    return input("Phone: ")


def show_data(name, phone):
    print(f"Name: {name} Phone: {phone}")


def ask_filename():
    return input("File name: ")


def search(name):
    mname = name.lower()
    for p, e in enumerate(contacts):
        if e[0].lower() == mname:
            return p
    return None


def new():
    name = ask_name()
    phone = ask_phone()
    contacts.append([name, phone])


def delete():
    name = ask_name()
    p = search(name)
    if p is not None:
        del contacts[p]
    else:
        print("Name not found.")


def modify():
    p = search(ask_name())
    if p is not None:
        name = contacts[p][0]
        phone = contacts[p][1]
        print("Found:")
        show_data(name, phone)
        name = ask_name()
        phone = ask_phone()
        contacts[p] = [name, phone]
    else:
        print("Name not found.")


def list_all():
    print("\nContacts\n\n------")
    for e in contacts:
        show_data(e[0], e[1])
    print("------\n")


def read():
    global contacts
    filename = ask_filename()
    try:
        with open(filename, "r", encoding="utf-8") as file:
            contacts = json.load(file)
    except FileNotFoundError:
        print("File not found")
    except json.JSONDecodeError:
        print("Error reading JSON file")


def save():
    filename = ask_filename()
    with open(filename, "w", encoding="utf-8") as file:
        json.dump(contacts, file, ensure_ascii=False, indent=2)


def validate_integer_range(prompt, start, end):
    while True:
        try:
            value = int(input(prompt))
            if start <= value <= end:
                return value
        except ValueError:
            print(f"Invalid value, please enter a number between {start} and {end}")


def menu():
    print(
        """
  1 – New
  2 – Modify
  3 – Delete
  4 – List
  5 – Save
  6 – Read

  0 – Exit
"""
    )
    return validate_integer_range("Choose an option: ", 0, 6)


while option := menu():
    if option == 0:
        break
    elif option == 1:
        new()
    elif option == 2:
        modify()
    elif option == 3:
        delete()
    elif option == 4:
        list_all()
    elif option == 5:
        save()
    elif option == 6:
        read()
