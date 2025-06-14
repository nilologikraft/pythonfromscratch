##############################################################################
# Python From Scratch
# Author: Nilo Ney Coutinho Menezes
# Editora Novatec (c) 2010-2025 - LogiKraft 2025
# Site: https://pythonfromscratch.com
# ISBN: 978-85-7522-949-1 (Paperback), 978-85-7522-950-7 (hardcover), 978-85-7522-951-4 (ebook)
#
# File: chapter 04/exercise-04-11.py.py
##############################################################################
value = float(input("Enter the house value: "))
salary = float(input("Enter the salary: "))
years = int(input("How many years to pay: "))
months = years * 12
installment = value / months
if installment > salary * 0.3:
    print("Unfortunately you cannot get the loan")
else:
    print(f"Installment value: R$ {installment:7.2f} Loan OK")
