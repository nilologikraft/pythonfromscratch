##############################################################################
# Python From Scratch
# Author: Nilo Ney Coutinho Menezes
# Editora Novatec (c) 2010-2025 - LogiKraft 2025
# Site: https://pythonfromscratch.com
# ISBN: 978-85-7522-949-1 (Paperback), 978-85-7522-950-7 (hardcover), 978-85-7522-951-4 (ebook)
#
# File: chapter 08/exercise-08-21.py.py
##############################################################################
def myrange(start, end=None, step=1):
    if end is None:
        start, end = 0, start

    current = start
    while current <= end:  # Note the <= to include the last value
        yield current
        current += step


# Test cases
print(list(myrange(1)))  # [0, 1]
print(list(myrange(1, 10)))  # [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(list(myrange(0, 10, 2)))  # [0, 2, 4, 6, 8, 10]
