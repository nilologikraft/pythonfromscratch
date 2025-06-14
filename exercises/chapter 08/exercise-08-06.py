##############################################################################
# Python From Scratch
# Author: Nilo Ney Coutinho Menezes
# Editora Novatec (c) 2010-2025 - LogiKraft 2025
# Site: https://pythonfromscratch.com
# ISBN: 978-85-7522-949-1 (Paperback), 978-85-7522-950-7 (hardcover), 978-85-7522-951-4 (ebook)
#
# File: chapter 08/exercise-08-06.py.py
##############################################################################
def sum(values):
    total = 0
    for e in values:
        total += e
    return total


L = [1, 7, 2, 9, 15]
print(sum(L))
print(sum([7, 9, 12, 3, 100, 20, 4]))
