##############################################################################
# Python From Scratch
# Author: Nilo Ney Coutinho Menezes
# Editora Novatec (c) 2010-2025 - LogiKraft 2025
# Site: https://pythonfromscratch.com
# ISBN: 978-85-7522-949-1 (Paperback), 978-85-7522-950-7 (hardcover), 978-85-7522-951-4 (ebook)
#
# File: chapter 03/exercise-03-11.py.py
##############################################################################
price = float(input("Enter the price of the item:"))
discount = float(input("Enter the discount percentage:"))
discount_amount = price * discount / 100
to_pay = price - discount_amount
print("A discount of %5.2f %% on an item of $ %7.2f" % (discount, price))
print("equals $ %7.2f." % discount_amount)
print("The amount to pay is $ %7.2f" % to_pay)
