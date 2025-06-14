##############################################################################
# Python From Scratch
# Author: Nilo Ney Coutinho Menezes
# Editora Novatec (c) 2010-2025 - LogiKraft 2025
# Site: https://pythonfromscratch.com
# ISBN: 978-85-7522-949-1 (Paperback), 978-85-7522-950-7 (hardcover), 978-85-7522-951-4 (ebook)
#
# File: chapter 06/06.17 - Creating and printing the shopping list.py
##############################################################################
shopping = []
while True:
    product = input("Product: ")
    if product == "end":
        break
    quantity = int(input("Quantity: "))
    price = float(input("Price: "))
    shopping.append([product, quantity, price])
total = 0.0
for e in shopping:
    print(f"{e[0]:20s} x {e[1]:5d} {e[2]:5.2f} {e[1] * e[2]:6.2f}")
    total+= e[1] * e[2]
print(f"Total: {total:7.2f}")
