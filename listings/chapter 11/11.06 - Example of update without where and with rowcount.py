##############################################################################
# Python From Scratch
# Author: Nilo Ney Coutinho Menezes
# Editora Novatec (c) 2010-2025 - LogiKraft 2025
# Site: https://pythonfromscratch.com
# ISBN: 978-85-7522-949-1 (Paperback), 978-85-7522-950-7 (hardcover), 978-85-7522-951-4 (ebook)
#
# File: chapter 11/11.06 - Example of update without where and with rowcount.py
##############################################################################
import sqlite3
from contextlib import closing

with sqlite3.connect("phonebook.db") as connection:
    with closing(connection.cursor()) as cursor:
        cursor.execute("""update phonebook
                             set telephone = '12345-6789' """)
        print("Updated records: ", cursor.rowcount)
