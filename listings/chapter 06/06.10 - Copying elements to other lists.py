##############################################################################
# Python From Scratch
# Author: Nilo Ney Coutinho Menezes
# Editora Novatec (c) 2010-2025 - LogiKraft 2025
# Site: https://pythonfromscratch.com
# ISBN: 978-85-7522-949-1 (Paperback), 978-85-7522-950-7 (hardcover), 978-85-7522-951-4 (ebook)
#
# File: chapter 06/06.10 - Copying elements to other lists.py
##############################################################################
values = [9, 8, 7, 12, 0, 13, 21]
evens = []
odds = []
for e in values:
    if e % 2 == 0:
        evens.append(e)
    else:
        odds.append(e)
print("Evens: ", evens)
print("Odds: ", odds)
