##############################################################################
# Python From Scratch
# Author: Nilo Ney Coutinho Menezes
# Editora Novatec (c) 2010-2025 - LogiKraft 2025
# Site: https://pythonfromscratch.com
# ISBN: 978-85-7522-949-1 (Paperback), 978-85-7522-950-7 (hardcover), 978-85-7522-951-4 (ebook)
#
# File: chapter 05/exercise-05-08.py.py
##############################################################################
first = int(input("First number: "))
second = int(input("Second number: "))
x = 1
result = 0
while x <= second:
    result = result + first
    x = x + 1
print(f"{first} x {second} = {result}")
