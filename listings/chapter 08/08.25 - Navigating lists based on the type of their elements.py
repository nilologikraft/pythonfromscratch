##############################################################################
# Python From Scratch
# Author: Nilo Ney Coutinho Menezes
# Editora Novatec (c) 2010-2025 - LogiKraft 2025
# Site: https://pythonfromscratch.com
# ISBN: 978-85-7522-949-1 (Paperback), 978-85-7522-950-7 (hardcover), 978-85-7522-951-4 (ebook)
#
# File: chapter 08/08.25 - Navigating lists based on the type of their elements.py
##############################################################################
L = ["a", ["b", "c", "d"], "e"]
for x in L:
    if type(x) is str:
        print(x)
    else:
        print("List:", end= "")
        for z in x:
            print(f" {z}", end= "")
        print()
