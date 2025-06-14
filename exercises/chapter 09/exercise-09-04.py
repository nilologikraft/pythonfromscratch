##############################################################################
# Python From Scratch
# Author: Nilo Ney Coutinho Menezes
# Editora Novatec (c) 2010-2025 - LogiKraft 2025
# Site: https://pythonfromscratch.com
# ISBN: 978-85-7522-949-1 (Paperback), 978-85-7522-950-7 (hardcover), 978-85-7522-951-4 (ebook)
#
# File: chapter 09/exercise-09-04.py.py
##############################################################################
import sys

# Check if parameters were passed
if len(sys.argv) != 4:  # Remember that the program name is the first in the list
    print("\nUsage: e09-04.py first second output\n\n")
else:
    first = open(sys.argv[1], "r")
    second = open(sys.argv[2], "r")
    output = open(sys.argv[3], "w")

    # Works similar to readlines
    for l1 in first:
        output.write(l1)
    for l2 in second:
        output.write(l2)

    first.close()
    second.close()
    output.close()
