##############################################################################
# Python From Scratch
# Author: Nilo Ney Coutinho Menezes
# Editora Novatec (c) 2010-2025 - LogiKraft 2025
# Site: https://pythonfromscratch.com
# ISBN: 978-85-7522-949-1 (Paperback), 978-85-7522-950-7 (hardcover), 978-85-7522-951-4 (ebook)
#
# File: chapter 12/exercise-12-04.py.py
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


# Bonus, how to recognize an optional pattern.
# Not part of the exercise, but interesting.
def optional(input_string, patterns):
    found, start, end = check_pattern(input_string, patterns)
    if found > 0:
        return found, start, end
    else:
        return 1, -1, -1


three_numbers = partial(number, min_qty=1, max_qty=3)
cents = partial(number, min_qty=1, max_qty=2)
dollar_sign = partial(sequence, pattern="$")
comma = partial(sequence, pattern=",")

# Only the values mentioned in the exercise
pattern = [dollar_sign, three_numbers, comma, cents]
# Using the optional function to accept values without cents (bonus)
# pattern = [dollar_sign, three_numbers, partial(optional, patterns=[comma, cents])]

# Here's a small list of inputs to facilitate visualization
inputs = [
    "123,45",  # Pattern found
    "$123,450",  # Pattern not found
    "$123,45",  # Pattern not found
    "$12,34",  # Pattern found
    "$123,45 $12,34 $1,23 $1,0",  # Pattern found four times
    "$123 $12 $1 $1,0",  # Pattern found four times (if bonus - optional enabled), once otherwise
]
for input_string in inputs:
    print("Input:", input_string)
    found = False
    position = 0
    while position < len(input_string):
        found, start, end = check_pattern(input_string[position:], pattern)
        if found > 0:
            print(f"Dollars at positions: {position+start} to {position+end} ", end="")
            print("Dollars:", input_string[position + start : position + end + 1])
            found = True
            position += end + 1
        else:
            position += 1
    if not found:
        print("No dollar values found in input")
    print()
