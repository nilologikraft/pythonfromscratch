##############################################################################
# Python From Scratch
# Author: Nilo Ney Coutinho Menezes
# Editora Novatec (c) 2010-2025 - LogiKraft 2025
# Site: https://pythonfromscratch.com
# ISBN: 978-85-7522-949-1 (Paperback), 978-85-7522-950-7 (hardcover), 978-85-7522-951-4 (ebook)
#
# File: chapter 08/exercise-08-12.py.py
##############################################################################
def search_string(s, list_to_search):
    return s in list_to_search


L = ["AB", "CD", "EF", "FG"]

print(search_string("AB", L))
print(search_string("CD", L))
print(search_string("EF", L))
print(search_string("FG", L))
print(search_string("XYZ", L))
