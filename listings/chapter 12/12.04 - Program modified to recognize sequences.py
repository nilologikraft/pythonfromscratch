##############################################################################
# Python From Scratch
# Author: Nilo Ney Coutinho Menezes
# Editora Novatec (c) 2010-2025 - LogiKraft 2025
# Site: https://pythonfromscratch.com
# ISBN: 978-85-7522-949-1 (Paperback), 978-85-7522-950-7 (hardcover), 978-85-7522-951-4 (ebook)
#
# File: chapter 12/12.04 - Program modified to recognize sequences.py
##############################################################################
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
    position, maximum_position = 0, len(pattern)
    for character in entry:
        if character == pattern[position]:
            position += 1  # test the next character
        else:
            break  # Exited the sequence
        if position == maximum_position:  # Found the entire sequence
            return 1, 0, position - 1
    return -1, -1, -1
def ldc(entry):
    found, _, _ = sequence(entry[0], "(")
    if found > 0:
        found, _, n_end = number(entry[1:], 2, 3)
        if found > 0:
            found, _, _ = sequence(entry[n_end + 2], ")")
            if found > 0:
                return 1, 0, found + 2
    return -1, -1, -1
for position in range(len(sequence)):
    found, start, end = ldc(sequence[position:])
    if found > 0:
        print(f"LDC found in positions: {position+start} to {position+end}")
        print(sequence[position + start: position + end + 1])
