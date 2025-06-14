##############################################################################
# Python From Scratch
# Author: Nilo Ney Coutinho Menezes
# Editora Novatec (c) 2010-2025 - LogiKraft 2025
# Site: https://pythonfromscratch.com
# ISBN: 978-85-7522-949-1 (Paperback), 978-85-7522-950-7 (hardcover), 978-85-7522-951-4 (ebook)
#
# File: chapter 08/exercise-08-05.py.py
##############################################################################
def search(list_to_search, value):
    if value in list_to_search:
        return list_to_search.index(value)
    return None


L = [10, 20, 25, 30]
print(search(L, 25))
print(search(L, 27))
