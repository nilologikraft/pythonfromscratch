##############################################################################
# Python From Scratch
# Author: Nilo Ney Coutinho Menezes
# Editora Novatec (c) 2010-2025 - LogiKraft 2025
# Site: https://pythonfromscratch.com
# ISBN: 978-85-7522-949-1 (Paperback), 978-85-7522-950-7 (hardcover), 978-85-7522-951-4 (ebook)
#
# File: chapter 06/exercise-06-01.py.py
##############################################################################
grades = [0, 0, 0, 0, 0, 0, 0]  # Or [0] * 7
sum = 0
x = 0
while x < 7:
    grades[x] = float(input(f"Grade {x}:"))
    sum += grades[x]
    x += 1
x = 0
while x < 7:
    print(f"Grade {x}: {grades[x]:6.2f}")
    x += 1
print(f"Average: {sum/x:5.2f}")
