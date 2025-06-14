##############################################################################
# Python From Scratch
# Author: Nilo Ney Coutinho Menezes
# Editora Novatec (c) 2010-2025 - LogiKraft 2025
# Site: https://pythonfromscratch.com
# ISBN: 978-85-7522-949-1 (Paperback), 978-85-7522-950-7 (hardcover), 978-85-7522-951-4 (ebook)
#
# File: chapter 05/exercise-05-21.py.py
##############################################################################
while True:
    value = int(input("Enter the amount to pay:"))
    if value == 0:
        break
    bills = 0
    current = 50
    to_pay = value
    while True:
        if current <= to_pay:
            to_pay -= current
            bills += 1
        else:
            print(f"{bills} bill(s) of R${current}")
            if to_pay == 0:
                break
            if current == 50:
                current = 20
            elif current == 20:
                current = 10
            elif current == 10:
                current = 5
            elif current == 5:
                current = 1
            bills = 0
