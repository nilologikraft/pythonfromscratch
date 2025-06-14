##############################################################################
# Python From Scratch
# Author: Nilo Ney Coutinho Menezes
# Editora Novatec (c) 2010-2025 - LogiKraft 2025
# Site: https://pythonfromscratch.com
# ISBN: 978-85-7522-949-1 (Paperback), 978-85-7522-950-7 (hardcover), 978-85-7522-951-4 (ebook)
#
# File: chapter 08/08.14 - Configuring functions with functions.py
##############################################################################
def print_list(L, fprint, fcondition):
    for e in L:
        if fcondition(e):
            fprint(e)
def print_element(e):
    print(f"Value: {e}")
def is_even(x):
    return x % 2 == 0
def is_odd(x):
    return not is_even(x)
L = [1, 7, 9, 2, 11, 0]
print_list(L, print_element, is_even)
Value: 2
Value: 0
print_list(L, print_element, is_odd)
Value: 1
Value: 7
Value: 9
Value: 11
