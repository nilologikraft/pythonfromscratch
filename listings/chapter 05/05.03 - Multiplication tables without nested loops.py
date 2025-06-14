##############################################################################
# Python From Scratch
# Author: Nilo Ney Coutinho Menezes
# Editora Novatec (c) 2010-2025 - LogiKraft 2025
# Site: https://pythonfromscratch.com
# ISBN: 978-85-7522-949-1 (Paperback), 978-85-7522-950-7 (hardcover), 978-85-7522-951-4 (ebook)
#
# File: chapter 05/05.03 - multiplication tables without nested loops.py
##############################################################################
table = 1
number = 1
while table <= 10:
    print(f"{table} x {number} = {table * number}")
    number += 1
    if number == 11:
        number = 1
        table += 1
