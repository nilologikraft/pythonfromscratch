##############################################################################
# Python From Scratch
# Author: Nilo Ney Coutinho Menezes
# Editora Novatec (c) 2010-2025 - LogiKraft 2025
# Site: https://pythonfromscratch.com
# ISBN: 978-85-7522-949-1 (Paperback), 978-85-7522-950-7 (hardcover), 978-85-7522-951-4 (ebook)
#
# File: chapter 08/exercise-08-14.py.py
##############################################################################
import random

n = random.randint(1, 10)
attempts = 0
while attempts < 3:
    x = int(input("Choose a number between 1 and 10: "))
    if x == n:
        print("You got it right!")
        break
    else:
        print("You got it wrong.")
    attempts += 1
