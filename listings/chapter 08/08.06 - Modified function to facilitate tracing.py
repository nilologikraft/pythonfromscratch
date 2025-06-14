##############################################################################
# Python From Scratch
# Author: Nilo Ney Coutinho Menezes
# Editora Novatec (c) 2010-2025 - LogiKraft 2025
# Site: https://pythonfromscratch.com
# ISBN: 978-85-7522-949-1 (Paperback), 978-85-7522-950-7 (hardcover), 978-85-7522-951-4 (ebook)
#
# File: chapter 08/08.06 - Modified function to facilitate tracing.py
##############################################################################
def factorial(n):
    print(f"Calculating the factorial of {n}")
    if n == 0 or n == 1:
        print(f"Factorial of {n} = 1")
        return 1
    else:
        fat = n * factorial(n - 1)
        print(f" factorial of {n} = {fat}")
    return fat
factorial(4)
