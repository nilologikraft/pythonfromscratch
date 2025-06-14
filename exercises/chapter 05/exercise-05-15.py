##############################################################################
# Python From Scratch
# Author: Nilo Ney Coutinho Menezes
# Editora Novatec (c) 2010-2025 - LogiKraft 2025
# Site: https://pythonfromscratch.com
# ISBN: 978-85-7522-949-1 (Paperback), 978-85-7522-950-7 (hardcover), 978-85-7522-951-4 (ebook)
#
# File: chapter 05/exercise-05-15.py.py
##############################################################################
to_pay = 0
while True:
    code = int(input("Product code (0 to exit): "))
    price = 0
    if code == 0:
        break
    elif code == 1:
        price = 0.50
    elif code == 2:
        price = 1.00
    elif code == 3:
        price = 4.00
    elif code == 5:
        price = 7.00
    elif code == 9:
        price = 8.00
    else:
        print("Invalid code!")
    if price != 0:
        quantity = int(input("Quantity: "))
        to_pay = to_pay + (price * quantity)
print(f"Total to pay R${to_pay:8.2f}")
