##############################################################################
# Python From Scratch
# Author: Nilo Ney Coutinho Menezes
# Editora Novatec (c) 2010-2025 - LogiKraft 2025
# Site: https://pythonfromscratch.com
# ISBN: 978-85-7522-949-1 (Paperback), 978-85-7522-950-7 (hardcover), 978-85-7522-951-4 (ebook)
#
# File: chapter 06/exercise-06-02.py.py
##############################################################################
first = []
second = []
while True:
    e = int(input("Enter a value for the first list (0 to finish): "))
    if e == 0:
        break
    first.append(e)
while True:
    e = int(input("Enter a value for the second list (0 to finish): "))
    if e == 0:
        break
    second.append(e)
third = first[:]  # Copies elements from the first list
third.extend(second)
x = 0
while x < len(third):
    print(f"{x}: {third[x]}")
    x = x + 1
