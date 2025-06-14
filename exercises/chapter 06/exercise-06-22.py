##############################################################################
# Python From Scratch
# Author: Nilo Ney Coutinho Menezes
# Editora Novatec (c) 2010-2025 - LogiKraft 2025
# Site: https://pythonfromscratch.com
# ISBN: 978-85-7522-949-1 (Paperback), 978-85-7522-950-7 (hardcover), 978-85-7522-951-4 (ebook)
#
# File: chapter 06/exercise-06-22.py.py
##############################################################################
BEFORE = [1, 2, 5, 6, 9]
AFTER = [1, 2, 8, 10]

before_set = set(BEFORE)
after_set = set(AFTER)

# Sets support the & operator to perform intersection, that is,
# A & B results in the set of elements present in both A and B
print("Before:", BEFORE)
print("After:", AFTER)
print("Elements that did not change: ", before_set & after_set)
print("New elements:", after_set - before_set)
print("Elements that were removed:", before_set - after_set)
