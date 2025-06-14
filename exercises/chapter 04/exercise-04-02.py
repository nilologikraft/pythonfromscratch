##############################################################################
# Python From Scratch
# Author: Nilo Ney Coutinho Menezes
# Editora Novatec (c) 2010-2025 - LogiKraft 2025
# Site: https://pythonfromscratch.com
# ISBN: 978-85-7522-949-1 (Paperback), 978-85-7522-950-7 (hardcover), 978-85-7522-951-4 (ebook)
#
# File: chapter 04/exercise-04-02.py.py
##############################################################################
speed = float(input("Enter your car speed:"))
if speed > 80:
    fine = (speed - 80) * 5
    print(f"You were fined R$ {fine:7.2f}!")
if speed <= 80:
    print("Your speed is ok, have a good trip!")
