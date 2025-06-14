##############################################################################
# Python From Scratch
# Author: Nilo Ney Coutinho Menezes
# Editora Novatec (c) 2010-2025 - LogiKraft 2025
# Site: https://pythonfromscratch.com
# ISBN: 978-85-7522-949-1 (Paperback), 978-85-7522-950-7 (hardcover), 978-85-7522-951-4 (ebook)
#
# File: chapter 11/11.04 - Query with selection filter.py
##############################################################################
import sqlite3
from contextlib import closing

with sqlite3.connect("phonebook.db") as connection:
    with closing(connection.cursor()) as cursor:
        cursor.execute("select * from phonebook where name = 'Nilo'")
        while True:
            result = cursor.fetchone()
            if result is None:
                break
        print(f"Name: {result[0]}\nPhone: {result[1]}")
