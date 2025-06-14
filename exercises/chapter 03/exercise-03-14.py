##############################################################################
# Python From Scratch
# Author: Nilo Ney Coutinho Menezes
# Editora Novatec (c) 2010-2025 - LogiKraft 2025
# Site: https://pythonfromscratch.com
# ISBN: 978-85-7522-949-1 (Paperback), 978-85-7522-950-7 (hardcover), 978-85-7522-951-4 (ebook)
#
# File: chapter 03/exercise-03-14.py.py
##############################################################################
km = int(input("Enter the number of kilometers driven:"))
days = int(input("Enter how many days you kept the car:"))
price_per_day = 60
price_per_km = 0.15
total_to_pay = km * price_per_km + days * price_per_day
print("Total to pay: $ %7.2f" % total_to_pay)
