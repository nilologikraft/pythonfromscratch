##############################################################################
# Python From Scratch
# Author: Nilo Ney Coutinho Menezes
# Editora Novatec (c) 2010-2025 - LogiKraft 2025
# Site: https://pythonfromscratch.com
# ISBN: 978-85-7522-949-1 (Paperback), 978-85-7522-950-7 (hardcover), 978-85-7522-951-4 (ebook)
#
# File: chapter 06/06.09 - Verification of the highest value.py
##############################################################################
L = [1, 7, 2, 4]
maximum = L[0]
for e in L:
    if e > maximum:
        maximum = e
print(maximum)
