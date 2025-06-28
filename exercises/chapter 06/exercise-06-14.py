##############################################################################
# Python From Scratch
# Author: Nilo Ney Coutinho Menezes
# Editora Novatec (c) 2010-2025 - LogiKraft 2025
# Site: https://pythonfromscratch.com
# ISBN: 978-85-7522-949-1 (Paperback), 978-85-7522-950-7 (hardcover), 978-85-7522-951-4 (ebook)
#
# File: chapter 06/exercise-06-18.py.py
##############################################################################
L = [1, 2, 3, 4, 5]
end = 5
while end > 1:
    swapped = False
    x = 0
    while x < (end - 1):
        if L[x] < L[x + 1]:  # Only the verification condition was changed
            swapped = True
            temp = L[x]
            L[x] = L[x + 1]
            L[x + 1] = temp
        x += 1
    if not swapped:
        break
    end -= 1
for e in L:
    print(e)
