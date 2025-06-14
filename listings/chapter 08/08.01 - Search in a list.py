##############################################################################
# Python From Scratch
# Author: Nilo Ney Coutinho Menezes
# Editora Novatec (c) 2010-2025 - LogiKraft 2025
# Site: https://pythonfromscratch.com
# ISBN: 978-85-7522-949-1 (Paperback), 978-85-7522-950-7 (hardcover), 978-85-7522-951-4 (ebook)
#
# File: chapter 08/08.01 - Search in a list.py
##############################################################################
def search(where, value):
    for x, e in enumerate(where):
        if e == value:
            return x
    return None
L = [10, 20, 25, 30]
print(search(L, 25))
print(search(L, 27))
