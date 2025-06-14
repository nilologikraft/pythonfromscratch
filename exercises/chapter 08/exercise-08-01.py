##############################################################################
# Python From Scratch
# Author: Nilo Ney Coutinho Menezes
# Editora Novatec (c) 2010-2025 - LogiKraft 2025
# Site: https://pythonfromscratch.com
# ISBN: 978-85-7522-949-1 (Paperback), 978-85-7522-950-7 (hardcover), 978-85-7522-951-4 (ebook)
#
# File: chapter 08/exercise-08-01.py.py
##############################################################################
def maximum(a, b):
    if a > b:
        return a
    else:
        return b


print(f"maximum(5,6) == 6 -> obtained: {maximum(5,6)}")
print(f"maximum(2,1) == 2 -> obtained: {maximum(2,1)}")
print(f"maximum(7,7) == 7 -> obtained: {maximum(7,7)}")
