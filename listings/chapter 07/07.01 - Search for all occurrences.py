##############################################################################
# Python From Scratch
# Author: Nilo Ney Coutinho Menezes
# Editora Novatec (c) 2010-2025 - LogiKraft 2025
# Site: https://pythonfromscratch.com
# ISBN: 978-85-7522-949-1 (Paperback), 978-85-7522-950-7 (hardcover), 978-85-7522-951-4 (ebook)
#
# File: chapter 07/07.01 - Search for all occurrences.py
##############################################################################
s = "one tiger, two tigers, three tigers"
p = 0
while(p > -1):
    p = s.find("tiger", p)
    if p >= 0:
        print(f"Position: {p}")
        p += 1
