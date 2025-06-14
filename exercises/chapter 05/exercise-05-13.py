##############################################################################
# Python From Scratch
# Author: Nilo Ney Coutinho Menezes
# Editora Novatec (c) 2010-2025 - LogiKraft 2025
# Site: https://pythonfromscratch.com
# ISBN: 978-85-7522-949-1 (Paperback), 978-85-7522-950-7 (hardcover), 978-85-7522-951-4 (ebook)
#
# File: chapter 05/exercise-05-13.py.py
##############################################################################
debt = float(input("Debt: "))
rate = float(input("Interest (Ex.: 3 for 3%): "))
payment = float(input("Monthly payment: "))
month = 1
if debt * (rate / 100) > payment:
    print(
        "Your debt will never be paid off, as the interest is higher than the monthly payment."
    )
else:
    balance = debt
    interest_paid = 0
    while balance > payment:
        interest = balance * rate / 100
        balance = balance + interest - payment
        interest_paid = interest_paid + interest
        print(f"Debt balance in month {month} is R${balance:6.2f}.")
        month = month + 1
    print(f"To pay off a debt of R${debt:8.2f}, at {rate:5.2f}% interest,")
    print(
        f"you will need {month - 1} months, paying a total of R${interest_paid:8.2f} in interest."
    )
    print(
        f"In the last month, you would have a remaining balance of R${balance:8.2f} to pay."
    )
