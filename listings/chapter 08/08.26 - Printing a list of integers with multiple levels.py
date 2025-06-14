##############################################################################
# Python From Scratch
# Author: Nilo Ney Coutinho Menezes
# Editora Novatec (c) 2010-2025 - LogiKraft 2025
# Site: https://pythonfromscratch.com
# ISBN: 978-85-7522-949-1 (Paperback), 978-85-7522-950-7 (hardcover), 978-85-7522-951-4 (ebook)
#
# File: chapter 08/08.26 - Printing a list of integers with multiple levels.py
##############################################################################
def print_lists(list_to_print, level=0):
    for x in list_to_print:
        if type(x) is int:
            print(f"{x:{level * 2}}")
        else:
            print_lists(x, level + 1)
