##############################################################################
# Python From Scratch
# Author: Nilo Ney Coutinho Menezes
# Editora Novatec (c) 2010-2025 - LogiKraft 2025
# Site: https://pythonfromscratch.com
# ISBN: 978-85-7522-949-1 (Paperback), 978-85-7522-950-7 (hardcover), 978-85-7522-951-4 (ebook)
#
# File: chapter 12/exercise-12-02.py.py
##############################################################################
input_string = "ABC431DEF901c431203FXEW9"


def check_pattern(input_string, patterns):
    position = 0
    for pattern in patterns:
        found, _, end = pattern(input_string[position:])
        if found > 0:
            position += end + 1
        else:
            return -1, -1, -1
    return 1, 0, position - 1


def numbers(input_string):
    found = 0
    end = -1
    for i, character in enumerate(input_string):
        if "0" <= character <= "9":
            found += 1
            end = i
        else:
            break
    return found, 0, end


position = 0
while position < len(input_string):
    found, start, end = check_pattern(input_string[position:], [numbers])
    if found > 0:
        print(input_string[position : position + end + 1])
        position += end + 1
    else:
        position += 1
