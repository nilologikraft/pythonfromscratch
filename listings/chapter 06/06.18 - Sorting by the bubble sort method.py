##############################################################################
# Python From Scratch
# Author: Nilo Ney Coutinho Menezes
# Editora Novatec (c) 2010-2025 - LogiKraft 2025
# Site: https://pythonfromscratch.com
# ISBN: 978-85-7522-949-1 (Paperback), 978-85-7522-950-7 (hardcover), 978-85-7522-951-4 (ebook)
#
# File: chapter 06/06.18 - Sorting by the bubble sort method.py
##############################################################################
L = [7, 4, 3, 12, 8]
end = len(L)
while end > 1:
    changed = False
    x = 0
    while x < (end - 1):
        if L[x] > L[x + 1]:
            changed = True
            temp = L[x]
            L[x] = L[x + 1]
            L[x + 1] = temp
        x += 1
    if not changed:
        break
    end -= 1
for e in L:
    print(e)
