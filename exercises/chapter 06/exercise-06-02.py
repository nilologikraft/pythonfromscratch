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
    element = int(input("Enter a value for the first list (0 to finish): "))
    if element == 0:
        break
    first.append(element)
while True:
    element = int(input("Enter a value for the second list (0 to finish): "))
    if element == 0:
        break
    second.append(element)
# Copies elements from the first list to the third list
third = first[:]
# Extends the third list with the elements of the second list
third.extend(second)
x = 0
while x < len(third):
    print(f"{x}: {third[x]}")
    x += 1
