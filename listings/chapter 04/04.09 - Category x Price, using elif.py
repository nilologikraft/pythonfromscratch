##############################################################################
# Python From Scratch
# Author: Nilo Ney Coutinho Menezes
# Editora Novatec (c) 2010-2025 - LogiKraft 2025
# Site: https://pythonfromscratch.com
# ISBN: 978-85-7522-949-1 (Paperback), 978-85-7522-950-7 (hardcover), 978-85-7522-951-4 (ebook)
#
# File: chapter 04/04.09 - Category x Price, using elif.py
##############################################################################
category = int(input("Enter the product category:"))
if category == 1:
    price = 10
elif category == 2:
    price = 18
elif category == 3:
    price = 23
elif category == 4:
    price = 26
elif category == 5:
    price = 31
else:
    print("Invalid category, enter a value between 1 and 5!")
    price = 0
print(f"Product price is: ${price:6.2f}")
