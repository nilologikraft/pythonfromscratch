##############################################################################
# Python From Scratch
# Author: Nilo Ney Coutinho Menezes
# Editora Novatec (c) 2010-2025 - LogiKraft 2025
# Site: https://pythonfromscratch.com
# ISBN: 978-85-7522-949-1 (Paperback), 978-85-7522-950-7 (hardcover), 978-85-7522-951-4 (ebook)
#
# File: chapter 09/exercise-09-23.py.py
##############################################################################
address_book = []

# Variable to mark a change in the address book
changed = False


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
    for p, e in enumerate(address_book):
        if e[0].lower() == mname:
            return p
    return None


def new():
    global address_book, changed
    name = ask_name()
    phone = ask_phone()
    address_book.append([name, phone])
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


def modify():
    global changed
    p = search(ask_name())
    if p is not None:
        name = address_book[p][0]
        phone = address_book[p][1]
        print("Found:")
        show_data(name, phone)
        name = ask_name()
        phone = ask_phone()
        if confirm("modification") == "Y":
            address_book[p] = [name, phone]
            changed = True
    else:
        print("Name not found.")


def list():
    print("\nAddress Book\n\n------")
    # We use the enumerate function to get the position in the address book
    for position, e in enumerate(address_book):
        # Print the position without line break
        print(f"Position: {position} ", end="")
        show_data(e[0], e[1])
    print("------\n")


def read_last_saved_book():
    last = last_book()
    if last is not None:
        read_file(last)


def last_book():
    try:
        file = open("last book.dat", "r", encoding="utf-8")
        last = file.readline()[:-1]
        file.close()
    except FileNotFoundError:
        return None
    return last


def update_last(name):
    file = open("last book.dat", "w", encoding="utf-8")
    file.write(f"{name}\n")
    file.close()


def read_file(filename):
    global address_book, changed
    file = open(filename, "r", encoding="utf-8")
    address_book = []
    for l in file.readlines():
        name, phone = l.strip().split("#")
        address_book.append([name, phone])
    file.close()
    changed = False


def read():
    global changed
    if changed:
        print(
            "You haven't saved the list since the last change. Do you want to save it now?"
        )
        if confirm("save") == "Y":
            save()
    print("Read\n---")
    filename = ask_filename()
    read_file(filename)
    update_last(filename)


def sort():
    global changed
    # You can sort the list as shown in the book
    # using the bubble sort method
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
        if confirm("save") == "N":
            return
    print("Save\n------")
    filename = ask_filename()
    file = open(filename, "w", encoding="utf-8")
    for e in address_book:
        file.write(f"{e[0]}#{e[1]}\n")
    file.close()
    update_last(filename)
    changed = False


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
   1 - New
   2 - Modify
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


read_last_saved_book()

while True:
    option = menu()
    if option == 0:
        break
    elif option == 1:
        new()
    elif option == 2:
        modify()
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
