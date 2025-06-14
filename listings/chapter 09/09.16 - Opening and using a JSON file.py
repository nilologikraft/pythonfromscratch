##############################################################################
# Python From Scratch
# Author: Nilo Ney Coutinho Menezes
# Editora Novatec (c) 2010-2025 - LogiKraft 2025
# Site: https://pythonfromscratch.com
# ISBN: 978-85-7522-949-1 (Paperback), 978-85-7522-950-7 (hardcover), 978-85-7522-951-4 (ebook)
#
# File: chapter 09/09.16 - Opening and using a JSON file.py
##############################################################################
import json
from pathlib import Path
with Path("list.json").open(encoding="utf-8") as file:
    students = json.load(file)
for student in students:
    print("Name:", student["name"])
    print("Grades:", student["grades"])
    print("Average:", sum(student["grades"]) / len(student["grades"]))
    print()
