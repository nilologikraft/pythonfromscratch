##############################################################################
# Python From Scratch
# Author: Nilo Ney Coutinho Menezes
# Editora Novatec (c) 2010-2025 - LogiKraft 2025
# Site: https://pythonfromscratch.com
# ISBN: 978-85-7522-949-1 (Paperback), 978-85-7522-950-7 (hardcover), 978-85-7522-951-4 (ebook)
#
# File: chapter 06/exercise-06-09.py.py
##############################################################################
L = [15, 7, 27, 39]
p = int(input("Enter the value to search for (p): "))
v = int(input("Enter the other value to search for (v): "))
x = 0
foundP = False
foundV = False
first = 0
while x < len(L):
    if L[x] == p:
        foundP = True
        if not foundV:
            first = 1
    if L[x] == v:
        foundV = True
        if not foundP:
            first = 2
    x += 1
if foundP:
    print(f"p: {p} found")
else:
    print(f"p: {p} not found")
if foundV:
    print(f"v: {v} found")
else:
    print(f"v: {v} not found")
if first == 1:
    print("p was found before v")
elif first == 2:
    print("v was found before p")
