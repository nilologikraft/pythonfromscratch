##############################################################################
# Python From Scratch
# Author: Nilo Ney Coutinho Menezes
# Editora Novatec (c) 2010-2025 - LogiKraft 2025
# Site: https://pythonfromscratch.com
# ISBN: 978-85-7522-949-1 (Paperback), 978-85-7522-950-7 (hardcover), 978-85-7522-951-4 (ebook)
#
# File: chapter 05/exercise-05-19.py.py
##############################################################################
# Note: some values will not be calculated correctly
# due to rounding issues and the representation of 0.01
# in floating point. An alternative is to multiply all values
# by 100 and perform all calculations with integers.

value = float(input("Enter the amount to pay:"))
bills = 0
current = 100
to_pay = value
while True:
    if current <= to_pay:
        to_pay -= current
        bills += 1
    else:
        if current >= 1:
            print(f"{bills} bill(s) of ${current}")
        else:
            print(f"{bills} coin(s) of ${current:5.2f}")
        if to_pay < 0.01:
            break
        elif current == 100:
            current = 50
        elif current == 50:
            current = 20
        elif current == 20:
            current = 10
        elif current == 10:
            current = 5
        elif current == 5:
            current = 1
        elif current == 1:
            current = 0.50
        elif current == 0.50:
            current = 0.10
        elif current == 0.10:
            current = 0.05
        elif current == 0.05:
            current = 0.02
        elif current == 0.02:
            current = 0.01
        bills = 0
