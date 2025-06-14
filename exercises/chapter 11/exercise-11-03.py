##############################################################################
# Python From Scratch
# Author: Nilo Ney Coutinho Menezes
# Editora Novatec (c) 2010-2025 - LogiKraft 2025
# Site: https://pythonfromscratch.com
# ISBN: 978-85-7522-949-1 (Paperback), 978-85-7522-950-7 (hardcover), 978-85-7522-951-4 (ebook)
#
# File: chapter 11/exercise-11-03.py.py
##############################################################################
import sqlite3
from contextlib import closing

with sqlite3.connect("prices.db") as connection:
    with closing(connection.cursor()) as cursor:
        while True:
            name = input("Product name to search [blank to exit]: ")
            if not name:
                break
            cursor.execute("""select * from prices where name = ?""", (name,))
            found = 0
            for result in cursor.fetchall():
                print("Name: {0:30s} Price: {1:6.2f}".format(*result))
                found += 1
            if found == 0:
                print("Not found.")
            else:
                print("{} product(s) found.".format(found))
