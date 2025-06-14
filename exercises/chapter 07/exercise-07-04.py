##############################################################################
# Python From Scratch
# Author: Nilo Ney Coutinho Menezes
# Editora Novatec (c) 2010-2025 - LogiKraft 2025
# Site: https://pythonfromscratch.com
# ISBN: 978-85-7522-949-1 (Paperback), 978-85-7522-950-7 (hardcover), 978-85-7522-951-4 (ebook)
#
# File: chapter 07/exercise-07-04.py.py
##############################################################################
sequence = input("Enter the string: ")

counter = {}

for letter in sequence:
    counter[letter] = counter.get(letter, 0) + 1

for key, value in counter.items():
    print(f"{key}: {value}x")
