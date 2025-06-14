##############################################################################
# Python From Scratch
# Author: Nilo Ney Coutinho Menezes
# Editora Novatec (c) 2010-2025 - LogiKraft 2025
# Site: https://pythonfromscratch.com
# ISBN: 978-85-7522-949-1 (Paperback), 978-85-7522-950-7 (hardcover), 978-85-7522-951-4 (ebook)
#
# File: chapter 09/09.17 - Creating a price table in JSON format.py
##############################################################################
import json
from pathlib import Path
price_table = {}
print("Price list creator")
print("Enter a blank product name to finish")
while product := input("Product name:"):
    price = input("Price:")
    price_table[product] = price
with Path("prices.json").open("w", encoding="utf-8") as file:
    json.dump(price_table, file)
