##############################################################################
# Python From Scratch
# Author: Nilo Ney Coutinho Menezes
# Editora Novatec (c) 2010-2025 - LogiKraft 2025
# Site: https://pythonfromscratch.com
# ISBN: 978-85-7522-949-1 (Paperback), 978-85-7522-950-7 (hardcover), 978-85-7522-951-4 (ebook)
#
# File: chapter 06/exercise-06-03.py.py
##############################################################################
first = []
second = []
while True:
    element = int(input("Enter a value for the first list (0 to finish):"))
    if element == 0:
        break
    first.append(element)
while True:
    element = int(input("Enter a value for the second list (0 to finish):"))
    if element == 0:
        break
    second.append(element)
third = []
# Here we will create another list with elements from the first
# and second lists. There are several ways to solve this exercise.
# In this solution, we will search for values to insert into the third
# list. If they don't exist, we'll add them to the third. Otherwise,
# we won't copy them, thus avoiding duplicates.
two_lists = first[:]
two_lists.extend(second)
x = 0
while x < len(two_lists):
    y = 0
    while y < len(third):
        if two_lists[x] == third[y]:
            break
        y += 1
    if y == len(third):
        third.append(two_lists[x])
    x += 1
x = 0
while x < len(third):
    print(f"{x}: {third[x]}")
    x += 1
