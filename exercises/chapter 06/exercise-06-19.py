##############################################################################
# Python From Scratch
# Author: Nilo Ney Coutinho Menezes
# Editora Novatec (c) 2010-2025 - LogiKraft 2025
# Site: https://pythonfromscratch.com
# ISBN: 978-85-7522-949-1 (Paperback), 978-85-7522-950-7 (hardcover), 978-85-7522-951-4 (ebook)
#
# File: chapter 06/exercise-06-19.py.py
##############################################################################
inventory = {
    "tomato": [1000, 2.30],
    "lettuce": [500, 0.45],
    "potato": [2001, 1.20],
    "beans": [100, 1.50],
}
total = 0
print("Sales:\n")
while True:
    product = input("Product name (end to exit):")
    if product == "end":
        break
    if product in inventory:
        quantity = int(input("Quantity:"))
        if quantity <= inventory[product][0]:
            price = inventory[product][1]
            cost = price * quantity
            print(f"{product:12s}: {quantity:3d} x {price:6.2f} = {cost:6.2f}")
            inventory[product][0] -= quantity
            total += cost
        else:
            print("Requested quantity not available")
    else:
        print("Invalid product name")
print(f" Total cost: {total:21.2f}\n")
print("Inventory:\n")
for key, data in inventory.items():
    print("Description: ", key)
    print("Quantity: ", data[0])
    print(f"Price: {data[1]:6.2f}\n")
