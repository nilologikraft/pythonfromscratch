##############################################################################
# Python From Scratch
# Author: Nilo Ney Coutinho Menezes
# Editora Novatec (c) 2010-2025 - LogiKraft 2025
# Site: https://pythonfromscratch.com
# ISBN: 978-85-7522-949-1 (Paperback), 978-85-7522-950-7 (hardcover), 978-85-7522-951-4 (ebook)
#
# File: chapter 06/06.21 - Obtaining the price with a dictionary.py
##############################################################################
table = {"Lettuce": 0.45,
         "Potato": 1.20,
         "Tomato": 2.30,
         "Beans": 1.50}
while True:
    product = input("Enter product's name, end to exit:")
    if product == "end":
        break
    if product in table:
        print(f"Price {table[product]:5.2f}")
    else:
        print("Product not found!")
