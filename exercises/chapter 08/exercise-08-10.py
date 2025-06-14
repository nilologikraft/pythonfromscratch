##############################################################################
# Python From Scratch
# Author: Nilo Ney Coutinho Menezes
# Editora Novatec (c) 2010-2025 - LogiKraft 2025
# Site: https://pythonfromscratch.com
# ISBN: 978-85-7522-949-1 (Paperback), 978-85-7522-950-7 (hardcover), 978-85-7522-951-4 (ebook)
#
# File: chapter 08/exercise-08-10.py.py
##############################################################################
def fibonacci(n):
    prev = 0
    next = 1
    while n > 0:
        prev, next = next, next + prev
        n -= 1
    return prev


for x in range(10):
    print(f"fibonacci({x}) = {fibonacci(x)}")
