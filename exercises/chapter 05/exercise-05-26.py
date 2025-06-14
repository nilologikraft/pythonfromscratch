##############################################################################
# Python From Scratch
# Author: Nilo Ney Coutinho Menezes
# Editora Novatec (c) 2010-2025 - LogiKraft 2025
# Site: https://pythonfromscratch.com
# ISBN: 978-85-7522-949-1 (Paperback), 978-85-7522-950-7 (hardcover), 978-85-7522-951-4 (ebook)
#
# File: chapter 05/exercise-05-26.py.py
##############################################################################
# Note: this exercise is very similar to exercise 5.08
dividend = int(input("Dividend: "))
divisor = int(input("Divisor: "))
quotient = 0
x = dividend
while x >= divisor:
    x = x - divisor
    quotient = quotient + 1
remainder = x
print(f"The remainder of {dividend} / {divisor} is {remainder}")
