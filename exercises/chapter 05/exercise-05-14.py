##############################################################################
# Python From Scratch
# Author: Nilo Ney Coutinho Menezes
# Editora Novatec (c) 2010-2025 - LogiKraft 2025
# Site: https://pythonfromscratch.com
# ISBN: 978-85-7522-949-1 (Paperback), 978-85-7522-950-7 (hardcover), 978-85-7522-951-4 (ebook)
#
# File: chapter 05/exercise-05-14.py.py
##############################################################################
nsum = 0
quantity = 0
while True:
    n = int(input("Enter an integer: "))
    if n == 0:
        break
    nsum = nsum + n
    quantity = quantity + 1
print("Number of integers entered:", quantity)
print("Sum: ", nsum)
print(f"Average: {nsum/quantity:10.2f}")
