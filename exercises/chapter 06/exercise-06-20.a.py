##############################################################################
# Python From Scratch
# Author: Nilo Ney Coutinho Menezes
# Editora Novatec (c) 2010-2025 - LogiKraft 2025
# Site: https://pythonfromscratch.com
# ISBN: 978-85-7522-949-1 (Paperback), 978-85-7522-950-7 (hardcover), 978-85-7522-951-4 (ebook)
#
# File: chapter 06/exercise-06-20.a.py.py
##############################################################################
sentence = input("Enter a sentence to count the letters:")
letter_counter = {}
for letter in sentence:
    if letter in letter_counter:
        letter_counter[letter] = letter_counter[letter] + 1
    else:
        letter_counter[letter] = 1
print(letter_counter)
