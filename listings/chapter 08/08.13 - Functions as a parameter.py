##############################################################################
# Python From Scratch
# Author: Nilo Ney Coutinho Menezes
# Editora Novatec (c) 2010-2025 - LogiKraft 2025
# Site: https://pythonfromscratch.com
# ISBN: 978-85-7522-949-1 (Paperback), 978-85-7522-950-7 (hardcover), 978-85-7522-951-4 (ebook)
#
# File: chapter 08/08.13 - Functions as a parameter.py
##############################################################################
def addition(a, b):
    return a + b
def subtraction(a, b):
    return a - b
def print_result(a, b, foper):
    print(foper(a, b))
print_result(5, 4, addition)
9
print_result(10, 2, subtraction)
8
