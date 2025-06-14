##############################################################################
# Python From Scratch
# Author: Nilo Ney Coutinho Menezes
# Editora Novatec (c) 2010-2025 - LogiKraft 2025
# Site: https://pythonfromscratch.com
# ISBN: 978-85-7522-949-1 (Paperback), 978-85-7522-950-7 (hardcover), 978-85-7522-951-4 (ebook)
#
# File: chapter 05/exercise-05-23.py.py
##############################################################################
n = int(input("Enter a number:"))
if n < 0:
    print("Invalid number. Please enter only positive values")
if n == 0 or n == 1:
    print(f"{n} is a special case.")
else:
    if n == 2:
        print("2 is prime")
    elif n % 2 == 0:
        print(f"{n} is not prime, as 2 is the only even prime number.")
    else:
        x = 3
        while x < n:
            if n % x == 0:
                break
            x = x + 2
        if x == n:
            print(f"{n} is prime")
        else:
            print(f"{n} is not prime, as it is divisible by {x}")
