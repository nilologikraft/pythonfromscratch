##############################################################################
# Python From Scratch
# Author: Nilo Ney Coutinho Menezes
# Editora Novatec (c) 2010-2025 - LogiKraft 2025
# Site: https://pythonfromscratch.com
# ISBN: 978-85-7522-949-1 (Paperback), 978-85-7522-950-7 (hardcover), 978-85-7522-951-4 (ebook)
#
# File: chapter 03/exercise-03-10.py.py
##############################################################################
salary = float(input("Enter current salary:"))
raise_percentage = float(input("Enter raise percentage:"))
raise_amount = salary * raise_percentage / 100
new_salary = salary + raise_amount
print("A raise of %5.2f %% on a salary of $ %7.2f" % (raise_percentage, salary))
print("equals a raise of $ %7.2f" % raise_amount)
print("Resulting in a new salary of $ %7.2f" % new_salary)
