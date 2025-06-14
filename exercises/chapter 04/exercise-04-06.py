##############################################################################
# Python From Scratch
# Author: Nilo Ney Coutinho Menezes
# Editora Novatec (c) 2010-2025 - LogiKraft 2025
# Site: https://pythonfromscratch.com
# ISBN: 978-85-7522-949-1 (Paperback), 978-85-7522-950-7 (hardcover), 978-85-7522-951-4 (ebook)
#
# File: chapter 04/exercise-04-06.py.py
##############################################################################
distance = float(input("Enter the distance to travel: "))
if distance <= 200:
    fare = 0.5 * distance
else:
    fare = 0.45 * distance
print(f"Ticket price: R$ {fare:7.2f}")
