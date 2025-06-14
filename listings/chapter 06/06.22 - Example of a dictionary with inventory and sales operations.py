##############################################################################
# Python From Scratch
# Author: Nilo Ney Coutinho Menezes
# Editora Novatec (c) 2010-2025 - LogiKraft 2025
# Site: https://pythonfromscratch.com
# ISBN: 978-85-7522-949-1 (Paperback), 978-85-7522-950-7 (hardcover), 978-85-7522-951-4 (ebook)
#
# File: chapter 06/06.22 - Example of a dictionary with inventory and sales operations.py
##############################################################################
stock = {"tomato": [1000, 2.30],
         "lettuce": [500, 0.45],
         "potato": [2001, 1.20],
         "bean": [100, 1.50]}
sale = [["tomato", 5], ["potato", 10], ["lettuce", 5]]
total = 0
print("Sales:\n")
for operation in sale:
    product, quantity = operation
    price = stock[product][1]
    cost = price * quantity
    print(f"{product:12s}: {quantity:3d} x {price:6.2f} = {cost:6.2f}")
    stock[product][0] -= quantity
    total += cost
print(f" Total cost: {total:21.2f}\n")
print("Stock:\n")
for key, data in stock.items():
    print("Description: ", key)
    print("Quantity: ", data[0])
    print(f"Price: {data[1]:6.2f}\n")
