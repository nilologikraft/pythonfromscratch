##############################################################################
# Python From Scratch
# Author: Nilo Ney Coutinho Menezes
# Editora Novatec (c) 2010-2025 - LogiKraft 2025
# Site: https://pythonfromscratch.com
# ISBN: 978-85-7522-949-1 (Paperback), 978-85-7522-950-7 (hardcover), 978-85-7522-951-4 (ebook)
#
# File: chapter 08/exercise-08-18.py.py
##############################################################################
def print_lists(values, level=0, character=" ", increment=2):
    for x in values:
        if isinstance(x, int):
            print(f"{character * (level * increment)}{x}")
        else:
            print_lists(x, level + 1, character, increment)


# Usage example:
# print_lists([1, 2, 3, [4, 5, 6, [7, 8, 9]], 10], character="*", increment=4)
