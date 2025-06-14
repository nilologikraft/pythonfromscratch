##############################################################################
# Python From Scratch
# Author: Nilo Ney Coutinho Menezes
# Editora Novatec (c) 2010-2025 - LogiKraft 2025
# Site: https://pythonfromscratch.com
# ISBN: 978-85-7522-949-1 (Paperback), 978-85-7522-950-7 (hardcover), 978-85-7522-951-4 (ebook)
#
# File: chapter 06/06.02 - Calculation of the average with entered grades.py
##############################################################################
grades = [0, 0, 0, 0, 0]
sum = 0
x = 0
while x < 5:
    grades[x] = float(input(f"Grade {x}:"))
    sum += grades[x]
    x += 1
x = 0
while x < 5:
    print(f"Grade {x}: {grades[x]:6.2f}")
    x += 1
print(f"Average: {sum / x:5.2f}")
