##############################################################################
# Python From Scratch
# Author: Nilo Ney Coutinho Menezes
# Editora Novatec (c) 2010-2025 - LogiKraft 2025
# Site: https://pythonfromscratch.com
# ISBN: 978-85-7522-949-1 (Paperback), 978-85-7522-950-7 (hardcover), 978-85-7522-951-4 (ebook)
#
# File: chapter 12/exercise-12-05.py.py
##############################################################################
# Functions sequence and check pattern from listing 12.5
from functools import partial


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


def sequences(input, pattern, min_qty=1, max_qty=1):
    position = 0
    end = -1
    found_count = 0
    while position < len(input):
        found, _, iend = sequence(input[position:], pattern)
        if found > 0:
            found_count += 1
            position += iend + 1
            end = position - 1
        else:
            break
    # If pattern is optional, returns found 1, but start and end -1
    # so that check_pattern continues searching
    if min_qty == 0 and found_count == 0:
        return 1, -1, -1
    # Checks if number of findings is between min_qty and max_qty
    elif min_qty <= found_count <= max_qty:
        return found_count, 0, end
    else:
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


inputs = [
    "(((---)))",  # Pattern found
    "(((--)))",  # Pattern not found
    "(----)",  # Pattern not found
    "----",  # Pattern not found
    "((--))",  # Pattern not found
    "<(((--)))>",  # Pattern found
    "<<(((--)))>>",  # Pattern found
    "<<(((---)))>>",  # Pattern found
    "<<((--))>> <(((---)))> (((---))) ((((----))))",  # Pattern found twice
]
# The pattern is a sequence of characters that can be optional
# < zero or up to two times
# ( three or up to four times
# - two or up to three times
# ) three or up to four times
# > zero or up to two times
# You can create other patterns to test the sequences function
pattern = [
    partial(sequences, pattern="<", min_qty=0, max_qty=2),
    partial(sequences, pattern="(", min_qty=3, max_qty=4),
    partial(sequences, pattern="-", min_qty=2, max_qty=3),
    partial(sequences, pattern=")", min_qty=3, max_qty=4),
    partial(sequences, pattern=">", min_qty=0, max_qty=2),
]

for input in inputs:
    print("Input:", input)
    found = False
    position = 0
    while position < len(input):
        found, start, end = check_pattern(input[position:], pattern)
        if found > 0:
            print(f"Pattern at positions: {position+start} to {position+end} ", end="")
            print("Pattern:", input[position + start : position + end + 1])
            found = True
            position += end + 1
        else:
            position += 1
    if not found:
        print("No pattern found in input")
    print()
