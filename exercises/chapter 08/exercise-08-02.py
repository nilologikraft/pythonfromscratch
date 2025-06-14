##############################################################################
# Python From Scratch
# Author: Nilo Ney Coutinho Menezes
# Editora Novatec (c) 2010-2025 - LogiKraft 2025
# Site: https://pythonfromscratch.com
# ISBN: 978-85-7522-949-1 (Paperback), 978-85-7522-950-7 (hardcover), 978-85-7522-951-4 (ebook)
#
# File: chapter 08/exercise-08-02.py.py
##############################################################################
def multiple(a, b):
    return a % b == 0


print(f"multiple(8,4) == True  -> obtained: {multiple(8,4)}")
print(f"multiple(7,3) == False -> obtained: {multiple(7,3)}")
print(f"multiple(5,5) == True  -> obtained: {multiple(5,5)}")
