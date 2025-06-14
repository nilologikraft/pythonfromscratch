##############################################################################
# Python From Scratch
# Author: Nilo Ney Coutinho Menezes
# Editora Novatec (c) 2010-2025 - LogiKraft 2025
# Site: https://pythonfromscratch.com
# ISBN: 978-85-7522-949-1 (Paperback), 978-85-7522-950-7 (hardcover), 978-85-7522-951-4 (ebook)
#
# File: chapter 09/exercise-09-11.py.py
##############################################################################
import sys

if len(sys.argv) != 2:
    print("\nUsage: exercise-09-11.py file1\n\n\n")
    sys.exit(1)

name = sys.argv[1]
counter = {}

file = open(name, "r", encoding="utf-8")
for line in file:
    line = line.strip().lower()
    words = line.split()
    for word in words:
        if word in counter:
            counter[word] += 1
        else:
            counter[word] = 1
file.close()

for key in counter:
    print(f"{key} = {counter[key]}")
