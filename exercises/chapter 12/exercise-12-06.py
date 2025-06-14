##############################################################################
# Python From Scratch
# Author: Nilo Ney Coutinho Menezes
# Editora Novatec (c) 2010-2025 - LogiKraft 2025
# Site: https://pythonfromscratch.com
# ISBN: 978-85-7522-949-1 (Paperback), 978-85-7522-950-7 (hardcover), 978-85-7522-951-4 (ebook)
#
# File: chapter 12/exercise-12-06.py.py
##############################################################################
# Functions number, sequence and check pattern from listing 12.5
from functools import partial


def number(input, min_qty, max_qty):
    num = 0
    for character in input:
        if character.isnumeric():
            num += 1
        else:
            break
    if min_qty <= num <= max_qty:
        return num, 0, num - 1
    else:
        return -1, -1, -1


def sequence(input, pattern):
    position, max_position = 0, len(pattern)
    for character in input:
        if character == pattern[position]:
            position += 1  # Same characters, test next character
        else:
            break  # Out of sequence
        if position == max_position:  # Found entire sequence
            return 1, 0, position - 1
    return -1, -1, -1


def check_pattern(input, patterns):
    position = 0
    for pattern in patterns:
        found, _, end = pattern(input[position:])
        if found > 0:
            position += end + 1
        else:
            return -1, -1, -1
    return 1, 0, position - 1


def cell_number(input):
    pattern = [
        partial(sequence, pattern="("),
        partial(number, min_qty=2, max_qty=3),
        partial(sequence, pattern=")"),
        partial(number, min_qty=5, max_qty=5),
        partial(sequence, pattern="-"),
        partial(number, min_qty=4, max_qty=4),
    ]
    found, _, _ = check_pattern(input, pattern)
    return found > 0


inputs = [
    "(92)99999-9999",  # Yes
    "(11)99999-999",  # No
    "(2)99999-9999",  # No
    "(12)9999999999",  # No
    "(312)9999999999",  # No
    "(312)99999-9999",  # Yes
]

for input in inputs:
    print(f"{input}: is it a cell number? {'Yes' if cell_number(input) else 'No'}")
