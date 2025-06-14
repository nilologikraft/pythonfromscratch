##############################################################################
# Python From Scratch
# Author: Nilo Ney Coutinho Menezes
# Editora Novatec (c) 2010-2025 - LogiKraft 2025
# Site: https://pythonfromscratch.com
# ISBN: 978-85-7522-949-1 (Paperback), 978-85-7522-950-7 (hardcover), 978-85-7522-951-4 (ebook)
#
# File: chapter 08/08.08 - Recursive Fibonacci function with prints.py
##############################################################################
def fibonacci(n):
    print(f"Calculating Fibonacci {n}")
    if n <= 1:
        print(f"  Fibonacci of {n} = {n}")
        return n
    else:
        print(f"  Fibonacci de {n} = fibonacci {n-1} + fibonacci {n-2} = ...")
        result = fibonacci(n - 1) + fibonacci(n - 2)
        print(f"  Fibonacci of {n} = fibonacci {n-1} + fibonacci {n-2} = {result}")
        return result
fibonacci(5)
