##############################################################################
# Python From Scratch
# Author: Nilo Ney Coutinho Menezes
# Editora Novatec (c) 2010-2025 - LogiKraft 2025
# Site: https://pythonfromscratch.com
# ISBN: 978-85-7522-949-1 (Paperback), 978-85-7522-950-7 (hardcover), 978-85-7522-951-4 (ebook)
#
# File: chapter 09/exercise-09-02.py.py
##############################################################################
import sys

# Check if parameters were passed
if len(sys.argv) != 4:  # Remember that the program name is the first in the list
    print("\nUsage: e09-02.py filename start end\n\n")
else:
    name = sys.argv[1]
    start = int(sys.argv[2])
    end = int(sys.argv[3])
    file = open(name, "r")
    for line in file.readlines()[start - 1 : end]:
        # Since the line ends with ENTER,
        # we remove the last character before printing
        print(line[:-1])
    file.close()

# Don't forget to read about encodings
# Depending on the file type and your operating system,
# it may not print correctly on screen.
