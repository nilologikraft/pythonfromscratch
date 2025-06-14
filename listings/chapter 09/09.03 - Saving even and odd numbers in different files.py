##############################################################################
# Python From Scratch
# Author: Nilo Ney Coutinho Menezes
# Editora Novatec (c) 2010-2025 - LogiKraft 2025
# Site: https://pythonfromscratch.com
# ISBN: 978-85-7522-949-1 (Paperback), 978-85-7522-950-7 (hardcover), 978-85-7522-951-4 (ebook)
#
# File: chapter 09/09.03 - Saving even and odd numbers in different files.py
##############################################################################
with open("odds.txt ", "w") as odds:
    with open("evens.txt ", "w") as evens:
        for n in range(0, 1000):
            if n % 2 == 0:
                evens.write(f"{n}\n")
            else:
                odds.write(f"{n}\n")
