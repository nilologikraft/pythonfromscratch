##############################################################################
# Python From Scratch
# Author: Nilo Ney Coutinho Menezes
# Editora Novatec (c) 2010-2025 - LogiKraft 2025
# Site: https://pythonfromscratch.com
# ISBN: 978-85-7522-949-1 (Paperback), 978-85-7522-950-7 (hardcover), 978-85-7522-951-4 (ebook)
#
# File: chapter 07/exercise-07-03.py.py
##############################################################################
first = input("Enter the first string: ")
second = input("Enter the second string: ")

third = ""

# For each letter in the first string
for letter in first:
    # Check if the letter does not appear in the second string
    # and also if it's not already listed in the third
    if letter not in second and letter not in third:
        third += letter

# For each letter in the second string
for letter in second:
    # Besides not being in the first string,
    # check if it's not already in the third (avoid repetitions)
    if letter not in first and letter not in third:
        third += letter

if third == "":
    print("No uncommon characters found.")
else:
    print(f"Uncommon characters: {third}")
