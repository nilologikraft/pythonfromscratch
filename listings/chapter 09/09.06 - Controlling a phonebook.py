##############################################################################
# Python From Scratch
# Author: Nilo Ney Coutinho Menezes
# Editora Novatec (c) 2010-2025 - LogiKraft 2025
# Site: https://pythonfromscratch.com
# ISBN: 978-85-7522-949-1 (Paperback), 978-85-7522-950-7 (hardcover), 978-85-7522-951-4 (ebook)
#
# File: chapter 09/09.06 - Controlling a phonebook.py
##############################################################################
phonebook = []
def ask_name():
    return input("Name: ")
def ask_telephone():
    return input("Phone: ")
def show_data(name, phone):
    print(f"Name: {name} Phone: {phone}")
def ask_filename():
    return input("File name: ")
def search(name):
    name = name.lower()
    for p, e in enumerate(phonebook):
        if e[0].lower() == name:
            return p
    return None
def new():
    name = ask_name()
    telephone = ask_telephone()
    phonebook.append([name, phone])
def delete():
    name = ask_name()
    p = search(name)
    if p is not None:
        del phonebook[p]
    else:
        print("Name not found.")
def update():
    p = search(ask_name())
    if p is not None:
        name = phonebook[p][0]
        phone = phonebook[p][1]
        print("Found:")
        show_data(name, phone)
        name = ask_name()
        telephone = ask_telephone()
        phonebook[p] = [name, phone]
    else:
        print("Name not found.")
def list_all():
    print("\nPhonebook\n\n------")
    for e in phonebook:
        show_data(e[0], e[1])
    print("------\n")
def load():
    global phonebook
    filename = ask_filename()
    with open(filename, "r", encoding="utf-8") as file:
        phonebook = []
        for line in file.readlines():
            name, phone = line.strip().split("#")
            phonebook.append([name, phone])
def save():
    filename = ask_filename()
    with open(filename, "w", encoding="utf-8") as file:
        for e in phonebook:
            file.write(f"{e[0]}#{e[1]}\n")
def validate_integer_range(question, start, end):
    while True:
        try:
            value = int(input(question))
            if start <= value <= end:
                return value
        except ValueError:
            print(f"Invalid value, please type between {start} and {end}")
def menu():
    print("""
  1 - New
  2 - Update
  3 - Delete
  4 - List
  5 - Save
  6 - Load

  0 - Exit
""")
    return validate_integer_range("Choose an option: ", 0, 6)
while option := menu():
    if option == 0:
        break
    elif option == 1:
        new()
    elif option == 2:
        update()
    elif option == 3:
        delete()
    elif option == 4:
        list_all()
    elif option == 5:
        save()
    elif option == 6:
        load()
