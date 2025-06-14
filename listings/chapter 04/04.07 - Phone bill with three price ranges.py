##############################################################################
# Python From Scratch
# Author: Nilo Ney Coutinho Menezes
# Editora Novatec (c) 2010-2025 - LogiKraft 2025
# Site: https://pythonfromscratch.com
# ISBN: 978-85-7522-949-1 (Paperback), 978-85-7522-950-7 (hardcover), 978-85-7522-951-4 (ebook)
#
# File: chapter 04/04.07 - Phone bill with three price ranges.py
##############################################################################
minutes = int(input("How many minutes did you use this month:"))
if minutes < 200:
    price = 0.20
else:
    if minutes < 400:
        price = 0.18
    else:
        price = 0.15
print(f"You will pay this month: ${minutes * price:6.2f}")
