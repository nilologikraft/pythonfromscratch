##############################################################################
# Python From Scratch
# Author: Nilo Ney Coutinho Menezes
# Editora Novatec (c) 2010-2025 - LogiKraft 2025
# Site: https://pythonfromscratch.com
# ISBN: 978-85-7522-949-1 (Paperback), 978-85-7522-950-7 (hardcover), 978-85-7522-951-4 (ebook)
#
# File: chapter 07/exercise-07-07.py.py
##############################################################################
vowels = "aeiou"
phrase = input("Enter a phrase: ")
lowercase_phrase = phrase.lower()
for vowel in vowels:
    vowel_count = lowercase_phrase.count(vowel)
    if vowel_count > 0:
        print(f"{vowel} appears {vowel_count} time(s)")
