##############################################################################
# Python From Scratch
# Author: Nilo Ney Coutinho Menezes
# Editora Novatec (c) 2010-2025 - LogiKraft 2025
# Site: https://pythonfromscratch.com
# ISBN: 978-85-7522-949-1 (Paperback), 978-85-7522-950-7 (hardcover), 978-85-7522-951-4 (ebook)
#
# File: chapter 06/exercise-06-11.py.py
##############################################################################
L = []
while True:
    n = int(input("Enter a number (0 to exit):"))
    if n == 0:
        break
    L.append(n)
for e in L:
    print(e)
# The first while loop couldn't be converted to a for loop because
# the number of repetitions is unknown at the start.
