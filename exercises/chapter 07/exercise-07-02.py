##############################################################################
# Python From Scratch
# Author: Nilo Ney Coutinho Menezes
# Editora Novatec (c) 2010-2025 - LogiKraft 2025
# Site: https://pythonfromscratch.com
# ISBN: 978-85-7522-949-1 (Paperback), 978-85-7522-950-7 (hardcover), 978-85-7522-951-4 (ebook)
#
# File: chapter 07/exercise-07-02.py.py
##############################################################################
first = input("Enter the first string: ")
second = input("Enter the second string: ")

third = ""

# For each letter in the first string
for letter in first:
    # If the letter is in the second string (common to both)
    # To avoid duplicates, it should not be in the third string
    if letter in second and letter not in third:
        third += letter

if third == "":
    print("No common characters found.")
else:
    print(f"Common characters: {third}")
