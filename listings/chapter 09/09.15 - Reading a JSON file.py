##############################################################################
# Python From Scratch
# Author: Nilo Ney Coutinho Menezes
# Editora Novatec (c) 2010-2025 - LogiKraft 2025
# Site: https://pythonfromscratch.com
# ISBN: 978-85-7522-949-1 (Paperback), 978-85-7522-950-7 (hardcover), 978-85-7522-951-4 (ebook)
#
# File: chapter 09/09.15 - Reading a JSON file.py
##############################################################################
import json
from pathlib import Path
with Path("data.json").open() as file:
    data = json.load(file)
print(data["name"])
print(data["values"])
