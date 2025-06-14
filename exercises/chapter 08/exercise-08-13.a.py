##############################################################################
# Python From Scratch
# Author: Nilo Ney Coutinho Menezes
# Editora Novatec (c) 2010-2025 - LogiKraft 2025
# Site: https://pythonfromscratch.com
# ISBN: 978-85-7522-949-1 (Paperback), 978-85-7522-950-7 (hardcover), 978-85-7522-951-4 (ebook)
#
# File: chapter 08/exercise-08-13.a.py.py
##############################################################################
def validate_input(message, valid_options):
    options = valid_options.lower()
    while True:
        choice = input(message)
        if choice.lower() in options:
            break
        print("Error: invalid option. Please try again.\n")
    return choice


# Example: print(validate_input("Choose an option:", "abcde"))
#
# Extra question: what happens if the user types more than one option?
# For example, ab.
