##############################################################################
# Python From Scratch
# Author: Nilo Ney Coutinho Menezes
# Editora Novatec (c) 2010-2025 - LogiKraft 2025
# Site: https://pythonfromscratch.com
# ISBN: 978-85-7522-949-1 (Paperback), 978-85-7522-950-7 (hardcover), 978-85-7522-951-4 (ebook)
#
# File: chapter 04/04.03 - Income Tax Calculation.py
##############################################################################
salary = float(input("Enter the salary for tax calculation: "))
base = salary
tax = 0
if base > 3000:
    tax = tax + (base - 3000) * 0.35
    base = 3000
if base > 1000:
    tax = tax + (base - 1000) * 0.20
print(f"Salary: ${salary:6.2f} Tax payable: ${tax:6.2f}")
