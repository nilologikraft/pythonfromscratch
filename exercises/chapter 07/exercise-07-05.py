##############################################################################
# Python From Scratch
# Author: Nilo Ney Coutinho Menezes
# Editora Novatec (c) 2010-2025 - LogiKraft 2025
# Site: https://pythonfromscratch.com
# ISBN: 978-85-7522-949-1 (Paperback), 978-85-7522-950-7 (hardcover), 978-85-7522-951-4 (ebook)
#
# File: chapter 07/exercise-07-05.py.py
##############################################################################
first = input("Enter the first string: ")
second = input("Enter the second string: ")

third = ""

for letter in first:
    if letter not in second:
        third += letter

if third == "":
    print("All characters were removed.")
else:
    print(f"The characters {second} were removed from {first}, resulting in: {third}")
