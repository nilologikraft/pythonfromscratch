##############################################################################
# Python From Scratch
# Author: Nilo Ney Coutinho Menezes
# Editora Novatec (c) 2010-2025 - LogiKraft 2025
# Site: https://pythonfromscratch.com
# ISBN: 978-85-7522-949-1 (Paperback), 978-85-7522-950-7 (hardcover), 978-85-7522-951-4 (ebook)
#
# File: chapter 12/12.05 - Using a list of functions to apply.py
##############################################################################
from functools import partial
sentence = "Buy it for $50.72. Call (92) 5431-2201 before 10/12/2033."
def number(entry, qmin, qmax):
    num = 0
    for character in entry:
        if character.isnumeric():
            num += 1
        else:
            break
    if qmin <= num <= qmax:
        return num, 0, num - 1
    else:
        return -1, -1, -1
def sequence(entry, pattern):
    position, position_max = 0, len(pattern)
    for character in entry:
        if character == pattern[position]:
            position += 1  # Same characters, test the next character
        else:
            break  # Exited the sequence
        if position == position_max:  # Found the entire sequence
            return 1, 0, position - 1
    return -1, -1, -1
def pattern_check(entry, patterns):
    position = 0
    for pattern in patterns:
        found, _, end = pattern(entry[position:])
        if found > 0:
            position += end + 1
        else:
            return -1, -1, -1
    return 1, 0, position - 1
def ldc(entry):
    found, _, end = pattern_check(
        entry,
        [
            partial(sequence, pattern="("),
            partial(number, qmin=2, qmax=3),
            partial(sequence, pattern=")"),
        ],
    )
    return (1, 0, end) if found > 0 else (-1, -1, -1)
for position in range(len(sentence)):
    found, start, end = ldc(sentence[position:])
    if found > 0:
        print(f"LDC found in positions: {position+start} to {position+end}")
        print(sentence[position + start: position + end + 1])
