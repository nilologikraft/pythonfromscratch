##############################################################################
# Python From Scratch
# Author: Nilo Ney Coutinho Menezes
# Editora Novatec (c) 2010-2025 - LogiKraft 2025
# Site: https://pythonfromscratch.com
# ISBN: 978-85-7522-949-1 (Paperback), 978-85-7522-950-7 (hardcover), 978-85-7522-951-4 (ebook)
#
# File: chapter 06/06.03 - Presenting numbers.py
##############################################################################
numbers = [0, 0, 0, 0, 0]
x = 0
while x < 5:
    numbers[x] = int(input(f"Number {x + 1}:"))
    x += 1
while True:
    chosen = int(input("What position do you want to print (0 to exit): "))
    if chosen == 0:
        break
    print(f"You chose number: {numbers [chosen - 1]}")
