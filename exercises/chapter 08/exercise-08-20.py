##############################################################################
# Python From Scratch
# Author: Nilo Ney Coutinho Menezes
# Editora Novatec (c) 2010-2025 - LogiKraft 2025
# Site: https://pythonfromscratch.com
# ISBN: 978-85-7522-949-1 (Paperback), 978-85-7522-950-7 (hardcover), 978-85-7522-951-4 (ebook)
#
# File: chapter 08/exercise-08-20.py.py
##############################################################################
def factorial_generator(n):
    value = 1
    for element in range(1, n + 1):
        value *= element
        yield value


# Usage example:
# Generate factorials from 1 to 5
for n, factorial in enumerate(factorial_generator(5), 1):
    print(f"{n}! = {factorial}")
