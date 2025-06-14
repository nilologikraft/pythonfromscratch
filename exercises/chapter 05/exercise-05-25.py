##############################################################################
# Python From Scratch
# Author: Nilo Ney Coutinho Menezes
# Editora Novatec (c) 2010-2025 - LogiKraft 2025
# Site: https://pythonfromscratch.com
# ISBN: 978-85-7522-949-1 (Paperback), 978-85-7522-950-7 (hardcover), 978-85-7522-951-4 (ebook)
#
# File: chapter 05/exercise-05-25.py.py
##############################################################################
# The abs function is used to calculate the absolute value of a number,
# that is, its value without sign.
# Examples: abs(1) returns 1 and abs(-1) returns 1

n = float(input("Enter a number to find its square root: "))
b = 2
while abs(n - (b * b)) > 0.00001:
    p = (b + (n / b)) / 2
    b = p
print(f"The square root of {n} is approximately {p:8.4f}")
