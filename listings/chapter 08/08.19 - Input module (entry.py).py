##############################################################################
# Python From Scratch
# Author: Nilo Ney Coutinho Menezes
# Editora Novatec (c) 2010-2025 - LogiKraft 2025
# Site: https://pythonfromscratch.com
# ISBN: 978-85-7522-949-1 (Paperback), 978-85-7522-950-7 (hardcover), 978-85-7522-951-4 (ebook)
#
# File: chapter 08/08.19 - Input module (entry.py).py
##############################################################################
def integer_validation(message, minimum, maximum):
    while True:
        try:
            v = int(input(message))
            if v >= minimum and v <= maximum:
                return v
            else:
                print(f"Enter a value between {minimum} and {maximum}")
        except ValueError:
            print("You must enter an integer")
