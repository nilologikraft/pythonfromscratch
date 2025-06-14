##############################################################################
# Python From Scratch
# Author: Nilo Ney Coutinho Menezes
# Editora Novatec (c) 2010-2025 - LogiKraft 2025
# Site: https://pythonfromscratch.com
# ISBN: 978-85-7522-949-1 (Paperback), 978-85-7522-950-7 (hardcover), 978-85-7522-951-4 (ebook)
#
# File: chapter 09/exercise-09-14.py.py
##############################################################################
# Pay attention to encoding on Windows

import sys

if len(sys.argv) != 3:
    print("\nUsage: exercise-09-14.py input output\n\n\n")
    sys.exit(1)

input_file = sys.argv[1]
output_file = sys.argv[2]

file = open(input_file, "r", encoding="utf-8")
output = open(output_file, "w", encoding="utf-8")
blank = 0

for line in file:
    # Removes spaces on the right
    # Replace with strip if you also
    # want to remove spaces on the left
    line = line.rstrip()
    line = line.replace("  ", "")  # Removes repeated spaces
    if line == "":
        blank += 1  # Counts blank lines
    else:
        blank = 0  # If the line is not blank, resets the counter
    if blank < 2:  # Doesn't write from the second blank line
        output.write(line + "\n")

file.close()
output.close()
