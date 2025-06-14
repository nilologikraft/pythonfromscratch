##############################################################################
# Python From Scratch
# Author: Nilo Ney Coutinho Menezes
# Editora Novatec (c) 2010-2025 - LogiKraft 2025
# Site: https://pythonfromscratch.com
# ISBN: 978-85-7522-949-1 (Paperback), 978-85-7522-950-7 (hardcover), 978-85-7522-951-4 (ebook)
#
# File: chapter 12/exercise-12-01.py.py
##############################################################################
input_string = "ABC431DEF901c431203FXEW9"
output = []
number = []

for character in input_string:
    if "a" <= character.lower() <= "z":
        if not number:
            output.append(number)
        number += character
    elif number:
        number = []

for found in output:
    print("".join(found))
