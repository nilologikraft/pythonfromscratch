##############################################################################
# Python From Scratch
# Author: Nilo Ney Coutinho Menezes
# Editora Novatec (c) 2010-2025 - LogiKraft 2025
# Site: https://pythonfromscratch.com
# ISBN: 978-85-7522-949-1 (Paperback), 978-85-7522-950-7 (hardcover), 978-85-7522-951-4 (ebook)
#
# File: chapter 08/08.10 - Integer validation using function.py
##############################################################################
def range_int_input(question, minimum, maximum):
    while True:
        v = int(input(question))
        if v < minimum or v > maximum:
            print(f"Invalid value. Please enter a value between {minimum} and {maximum}")
        else:
            return v
