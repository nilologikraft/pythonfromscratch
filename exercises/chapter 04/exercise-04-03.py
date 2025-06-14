##############################################################################
# Python From Scratch
# Author: Nilo Ney Coutinho Menezes
# Editora Novatec (c) 2010-2025 - LogiKraft 2025
# Site: https://pythonfromscratch.com
# ISBN: 978-85-7522-949-1 (Paperback), 978-85-7522-950-7 (hardcover), 978-85-7522-951-4 (ebook)
#
# File: chapter 04/exercise-04-03.py.py
##############################################################################
a = int(input("Enter the first value:"))
b = int(input("Enter the second value:"))
c = int(input("Enter the third value:"))
largest = a
if b > a and b > c:
    largest = b
if c > a and c >= b:
    largest = c
smallest = a
if b < c and b < a:
    smallest = b
if c <= b and c < a:
    smallest = c
print(f"The smallest number entered was {smallest}")
print(f"The largest number entered was {largest}")
