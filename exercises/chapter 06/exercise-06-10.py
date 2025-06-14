##############################################################################
# Python From Scratch
# Author: Nilo Ney Coutinho Menezes
# Editora Novatec (c) 2010-2025 - LogiKraft 2025
# Site: https://pythonfromscratch.com
# ISBN: 978-85-7522-949-1 (Paperback), 978-85-7522-950-7 (hardcover), 978-85-7522-951-4 (ebook)
#
# File: chapter 06/exercise-06-10.py.py
##############################################################################
L = [15, 7, 27, 39]
p = int(input("Enter the value to search for (p):"))
v = int(input("Enter the other value to search for (v):"))
x = 0
foundP = -1  # Here -1 indicates we haven't found the value yet
foundV = -1
first = 0
while x < len(L):
    if L[x] == p:
        foundP = x
    if L[x] == v:
        foundV = x
    x += 1
if foundP != -1:
    print(f"p: {p} found at position {foundP}")
else:
    print(f"p: {p} not found")
if foundV != -1:
    print(f"v: {v} found at position {foundV}")
else:
    print(f"v: {v} not found")
# Check if both were found
if foundP != -1 and foundV != -1:
    # since foundP and foundV store the positions where they were found
    if foundP <= foundV:
        print("p was found before v")
    else:
        print("v was found before p")
