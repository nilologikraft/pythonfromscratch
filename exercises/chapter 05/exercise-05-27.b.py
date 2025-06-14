##############################################################################
# Python From Scratch
# Author: Nilo Ney Coutinho Menezes
# Editora Novatec (c) 2010-2025 - LogiKraft 2025
# Site: https://pythonfromscratch.com
# ISBN: 978-85-7522-949-1 (Paperback), 978-85-7522-950-7 (hardcover), 978-85-7522-951-4 (ebook)
#
# File: chapter 05/exercise-05-27.b.py.py
##############################################################################
# Exercise 5.27
# Alternative solution, using only integers
n = int(input("Enter the number to verify:"))
# Since n is an integer, we'll calculate its
# number of digits by finding the first
# power of 10 greater than n.
# Example: 341 - first power of 10 greater: 1000 = 10 ^ 4
# We'll use 4 and not 3 to allow handling numbers
# with a single digit. The adjustment is made in the formulas below
q = 0
while 10**q < n:
    q = q + 1
i = q
f = 0
nf = ni = n  # Here we copy n to ni and nf
pi = pf = 0  # and make pi = pf (for special cases)
while i > f:
    pi = int(ni / (10 ** (i - 1)))  # Rightmost digit
    pf = nf % 10  # Leftmost digit
    if pi != pf:  # If they are different, we exit
        break
    f = f + 1  # Move to the next digit on the left
    i = i - 1  # Move to the next digit on the right
    ni = ni - (pi * (10**i))  # Adjust ni to remove the previous digit
    nf = int(nf / 10)  # Adjust nf to remove the last digit

if pi == pf:
    print(f"{n} is a palindrome")
else:
    print(f"{n} is not a palindrome")
