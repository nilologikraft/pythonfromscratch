##############################################################################
# Python From Scratch
# Author: Nilo Ney Coutinho Menezes
# Editora Novatec (c) 2010-2025 - LogiKraft 2025
# Site: https://pythonfromscratch.com
# ISBN: 978-85-7522-949-1 (Paperback), 978-85-7522-950-7 (hardcover), 978-85-7522-951-4 (ebook)
#
# File: chapter 06/exercise-06-20.b.py.py
##############################################################################
# Alternative solution, using the dictionary's get method

sentence = input("Enter a sentence to count the letters:")
d = {}
for letter in sentence:
    # If letter doesn't exist in dictionary, returns 0
    # if it exists, returns the previous value
    d[letter] = d.get(letter, 0) + 1
print(d)
