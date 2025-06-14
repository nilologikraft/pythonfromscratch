##############################################################################
# Python From Scratch
# Author: Nilo Ney Coutinho Menezes
# Editora Novatec (c) 2010-2025 - LogiKraft 2025
# Site: https://pythonfromscratch.com
# ISBN: 978-85-7522-949-1 (Paperback), 978-85-7522-950-7 (hardcover), 978-85-7522-951-4 (ebook)
#
# File: chapter 09/exercise-09-06.py.py
##############################################################################
WIDTH = 79
input_file = open("input.txt")
for line in input_file.readlines():
    if line[0] == ";":
        continue
    elif line[0] == ">":
        print(line[1:].rjust(WIDTH))
    elif line[0] == "*":
        print(line[1:].center(WIDTH))
    elif line[0] == "=":
        print("=" * 40)
    elif line[0] == ".":
        input("Press Enter to continue")
        print()
    else:
        print(line)
input_file.close()
