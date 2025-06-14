##############################################################################
# Python From Scratch
# Author: Nilo Ney Coutinho Menezes
# Editora Novatec (c) 2010-2025 - LogiKraft 2025
# Site: https://pythonfromscratch.com
# ISBN: 978-85-7522-949-1 (Paperback), 978-85-7522-950-7 (hardcover), 978-85-7522-951-4 (ebook)
#
# File: chapter 07/exercise-07-01.py.py
##############################################################################
first = input("Enter the first string: ")
second = input("Enter the second string: ")

position = first.find(second)

if position == -1:
    print(f"'{second}' not found in '{first}'")
else:
    print(f"{second} found at position {position} in {first}")
