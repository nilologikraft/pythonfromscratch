##############################################################################
# Python From Scratch
# Author: Nilo Ney Coutinho Menezes
# Editora Novatec (c) 2010-2025 - LogiKraft 2025
# Site: https://pythonfromscratch.com
# ISBN: 978-85-7522-949-1 (Paperback), 978-85-7522-950-7 (hardcover), 978-85-7522-951-4 (ebook)
#
# File: chapter 04/exercise-04-04.py.py
##############################################################################
salary = float(input("Enter your salary: "))
raise_percentage = 0.15
if salary > 1250:
    raise_percentage = 0.10
raise_amount = salary * raise_percentage
print(f"Your raise will be: ${raise_amount:7.2f}")
