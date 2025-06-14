##############################################################################
# Python From Scratch
# Author: Nilo Ney Coutinho Menezes
# Editora Novatec (c) 2010-2025 - LogiKraft 2025
# Site: https://pythonfromscratch.com
# ISBN: 978-85-7522-949-1 (Paperback), 978-85-7522-950-7 (hardcover), 978-85-7522-951-4 (ebook)
#
# File: chapter 12/exercise-12-03.py.py
##############################################################################
# Functions number, sequence and check pattern from listing 12.5
from functools import partial


def number(input_string, min_qty, max_qty):
    num = 0
    for character in input_string:
        if character.isnumeric():
            num += 1
        else:
            break
    if min_qty <= num <= max_qty:
        return num, 0, num - 1
    else:
        return -1, -1, -1


def sequence(input_string, pattern):
    position, max_position = 0, len(pattern)
    for character in input_string:
        if character == pattern[position]:
            position += 1  # Same characters, test next character
        else:
            break  # Out of sequence
        if position == max_position:  # Found entire sequence
            return 1, 0, position - 1
    return -1, -1, -1


def check_pattern(input_string, patterns):
    position = 0
    for pattern in patterns:
        found, _, end = pattern(input_string[position:])
        if found > 0:
            position += end + 1
        else:
            return -1, -1, -1
    return 1, 0, position - 1


two_numbers = partial(number, min_qty=2, max_qty=2)
slash = partial(sequence, pattern="/")
pattern = [two_numbers, slash, two_numbers, slash, two_numbers]

# Here's a small list of inputs to facilitate visualization
inputs = [
    "12/03/24",  # Pattern found
    "12/3/2024",  # Pattern not found
    "Twelfth of March 12/03",  # Pattern not found
    "12-03-24 12/03/2024 abc 21/30/24",  # Pattern found
    "12/03/24 12/03/624 abc 21/30/24",  # Pattern found twice
]
for input_string in inputs:
    print("Input:", input_string)
    found = False
    position = 0
    while position < len(input_string):
        found, start, end = check_pattern(input_string[position:], pattern)
        if found > 0:
            print(f"Date positions: {position+start} to {position+end} ", end="")
            print("Date:", input_string[position + start : position + end + 1])
            found = True
            position += end + 1
        else:
            position += 1
    if not found:
        print("No date found in input")
    print()
