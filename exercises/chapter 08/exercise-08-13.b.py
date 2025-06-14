##############################################################################
# Python From Scratch
# Author: Nilo Ney Coutinho Menezes
# Editora Novatec (c) 2010-2025 - LogiKraft 2025
# Site: https://pythonfromscratch.com
# ISBN: 978-85-7522-949-1 (Paperback), 978-85-7522-950-7 (hardcover), 978-85-7522-951-4 (ebook)
#
# File: chapter 08/exercise-08-13.b.py.py
##############################################################################
def validate_options(valid_options):
    valid_options = valid_options.lower()
    while True:
        option = input("Enter an option:").lower()
        if option in valid_options:
            return option
        print("Invalid option, please choose again.")
