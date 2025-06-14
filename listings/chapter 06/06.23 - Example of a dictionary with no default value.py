##############################################################################
# Python From Scratch
# Author: Nilo Ney Coutinho Menezes
# Editora Novatec (c) 2010-2025 - LogiKraft 2025
# Site: https://pythonfromscratch.com
# ISBN: 978-85-7522-949-1 (Paperback), 978-85-7522-950-7 (hardcover), 978-85-7522-951-4 (ebook)
#
# File: chapter 06/06.23 - Example of a dictionary with no default value.py
##############################################################################
d = {}
for letter in "abracadabra":
    if letter in d:
        d[letter] = d[letter] + 1
    else:
        d[letter] = 1
print(d)
