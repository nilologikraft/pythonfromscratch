##############################################################################
# Python From Scratch
# Author: Nilo Ney Coutinho Menezes
# Editora Novatec (c) 2010-2025 - LogiKraft 2025
# Site: https://pythonfromscratch.com
# ISBN: 978-85-7522-949-1 (Paperback), 978-85-7522-950-7 (hardcover), 978-85-7522-951-4 (ebook)
#
# File: chapter 09/exercise-09-03.py.py
##############################################################################
# Assume that even and odd files contain only integers
# Assume that values in each file are sorted
# Values don't need to be sequential
# Tolerates blank lines
# Even and odd files can have different number of lines


def read_number(file):
    while True:
        number = file.readline()
        # Check if something was read
        if number == "":
            return None
        # Ignore blank lines
        if number.strip() != "":
            return int(number)


def write_number(file, n):
    file.write(f"{n}\n")


even = open("evens.txt", "r")
odd = open("odds.txt", "r")
even_odd = open("even_odd.txt", "w")
even_num = read_number(even)
odd_num = read_number(odd)
while True:
    if even_num is None and odd_num is None:  # End if both are None
        break
    if even_num is not None and (odd_num is None or even_num <= odd_num):
        write_number(even_odd, even_num)
        even_num = read_number(even)
    if odd_num is not None and (even_num is None or odd_num <= even_num):
        write_number(even_odd, odd_num)
        odd_num = read_number(odd)

even_odd.close()
even.close()
odd.close()
