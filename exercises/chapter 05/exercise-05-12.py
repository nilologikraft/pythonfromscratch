##############################################################################
# Python From Scratch
# Author: Nilo Ney Coutinho Menezes
# Editora Novatec (c) 2010-2025 - LogiKraft 2025
# Site: https://pythonfromscratch.com
# ISBN: 978-85-7522-949-1 (Paperback), 978-85-7522-950-7 (hardcover), 978-85-7522-951-4 (ebook)
#
# File: chapter 05/exercise-05-12.py.py
##############################################################################
deposit = float(input("Initial deposit: "))
rate = float(input("Interest rate (Ex.: 3 for 3%): "))
monthly_investment = float(input("Monthly deposit: "))
month = 1
balance = deposit
while month <= 24:
    balance = balance + (balance * (rate / 100)) + monthly_investment
    print(f"Balance for month {month} is ${balance:5.2f}.")
    month = month + 1
print(f"The gain obtained with interest was ${balance-deposit:8.2f}.")
