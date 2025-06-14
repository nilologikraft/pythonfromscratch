##############################################################################
# Python From Scratch
# Author: Nilo Ney Coutinho Menezes
# Editora Novatec (c) 2010-2025 - LogiKraft 2025
# Site: https://pythonfromscratch.com
# ISBN: 978-85-7522-949-1 (Paperback), 978-85-7522-950-7 (hardcover), 978-85-7522-951-4 (ebook)
#
# File: chapter 04/exercise-04-12.py.py
##############################################################################
consumption = int(input("Consumption in kWh: "))
type = input("Installation type (R, C or I): ")
if type == "R":
    if consumption <= 500:
        price = 0.40
    else:
        price = 0.65
elif type == "I":
    if consumption <= 5000:
        price = 0.55
    else:
        price = 0.60
elif type == "C":
    if consumption <= 1000:
        price = 0.55
    else:
        price = 0.60
else:
    price = 0
    print("Error! Unknown installation type!")
cost = consumption * price
print(f"Amount to pay: R$ {cost:7.2f}")
