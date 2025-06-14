##############################################################################
# Python From Scratch
# Author: Nilo Ney Coutinho Menezes
# Editora Novatec (c) 2010-2025 - LogiKraft 2025
# Site: https://pythonfromscratch.com
# ISBN: 978-85-7522-949-1 (Paperback), 978-85-7522-950-7 (hardcover), 978-85-7522-951-4 (ebook)
#
# File: chapter 11/11.05 - Query using parameters.py
##############################################################################
import sqlite3
from contextlib import closing
name = input("Name to select: ")
with sqlite3.connect("phonebook.db") as connection:
    with closing(connection.cursor()) as cursor:
        cursor.execute('select * from phonebook where name = ?', (name,))
        x = 0
        while True:
            result = cursor.fetchone()
            if result is None:
                if x == 0:
                    print("Nothing found.")
                break
            print(f"Name: {result[0]}\nPhone: {result[1]}")
            x += 1
