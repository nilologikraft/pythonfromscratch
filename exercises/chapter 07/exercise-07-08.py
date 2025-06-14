##############################################################################
# Python From Scratch
# Author: Nilo Ney Coutinho Menezes
# Editora Novatec (c) 2010-2025 - LogiKraft 2025
# Site: https://pythonfromscratch.com
# ISBN: 978-85-7522-949-1 (Paperback), 978-85-7522-950-7 (hardcover), 978-85-7522-951-4 (ebook)
#
# File: chapter 07/exercise-07-08.py.py
##############################################################################
phrase = input("Enter a phrase: ")
words = phrase.split()
for word in words:
    print(word)
print("Number of words:", len(words))
