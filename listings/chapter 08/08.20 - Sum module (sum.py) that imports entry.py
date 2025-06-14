##############################################################################
# Python From Scratch
# Author: Nilo Ney Coutinho Menezes
# Editora Novatec (c) 2010-2025 - LogiKraft 2025
# Site: https://pythonfromscratch.com
# ISBN: 978-85-7522-949-1 (Paperback), 978-85-7522-950-7 (hardcover), 978-85-7522-951-4 (ebook)
#
# File: chapter 08/08.20 - Sum module (sum.py) that imports entry.py
##############################################################################
import entry
L = []
for x in range(10):
    L.append(entry.integer_validation("Enter a number:", 0, 20))
print(f"Sum: {sum(L)}")
