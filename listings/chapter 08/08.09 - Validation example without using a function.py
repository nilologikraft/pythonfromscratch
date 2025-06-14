##############################################################################
# Python From Scratch
# Author: Nilo Ney Coutinho Menezes
# Editora Novatec (c) 2010-2025 - LogiKraft 2025
# Site: https://pythonfromscratch.com
# ISBN: 978-85-7522-949-1 (Paperback), 978-85-7522-950-7 (hardcover), 978-85-7522-951-4 (ebook)
#
# File: chapter 08/08.09 - Validation example without using a function.py
##############################################################################
while True:
    v = int(input("Enter a value between 0 and 5:"))
    if v < 0 or v > 5:
        print("Invalid value.")
    else:
        break
