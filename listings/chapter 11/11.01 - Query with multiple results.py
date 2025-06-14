##############################################################################
# Python From Scratch
# Author: Nilo Ney Coutinho Menezes
# Editora Novatec (c) 2010-2025 - LogiKraft 2025
# Site: https://pythonfromscratch.com
# ISBN: 978-85-7522-949-1 (Paperback), 978-85-7522-950-7 (hardcover), 978-85-7522-951-4 (ebook)
#
# File: chapter 11/11.01 - Query with multiple results.py
##############################################################################
import sqlite3
connection = sqlite3.connect("phonebook.db")
cursor = connection.cursor()
cursor.execute("select * from phonebook")
result = cursor.fetchall()
for record in result:
    print(f"Name: {record[0]}\nPhone: {record[1]}")
cursor.close()
connection.close()
