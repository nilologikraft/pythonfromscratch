##############################################################################
# Python From Scratch
# Author: Nilo Ney Coutinho Menezes
# Editora Novatec (c) 2010-2025 - LogiKraft 2025
# Site: https://pythonfromscratch.com
# ISBN: 978-85-7522-949-1 (Paperback), 978-85-7522-950-7 (hardcover), 978-85-7522-951-4 (ebook)
#
# File: chapter 09/09.05 - Processing a file.py
##############################################################################
WIDTH = 79
with open("input.txt") as entries:
    for line in entries.readlines():
        if line[0] == ";":
            continue
        elif line[0] == ">":
            print(line[1:].rjust(WIDTH))
        elif line[0] == "<":
            print(line[1:].ljust(WIDTH))
        elif line[0] == "*":
            print(line[1:].center(WIDTH))
        else:
            print(line)
