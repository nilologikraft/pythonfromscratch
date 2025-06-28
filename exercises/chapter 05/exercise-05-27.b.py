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
maximum_exponent_of_10 = 0
while 10**maximum_exponent_of_10 < n:
    maximum_exponent_of_10 += 1
# Positions relative to the right and left of n
from_right = maximum_exponent_of_10
from_left = 0
# Here we copy n to number_from_left and number_from_right
number_from_left = number_from_right = n
# and make digit_from_right = digit_from_left (for special cases)
digit_from_right = digit_from_left = 0
while from_right > from_left:
    digit_from_right = int(
        number_from_right / (10 ** (from_right - 1))
    )  # Rightmost digit
    digit_from_left = number_from_left % 10  # Leftmost digit
    if digit_from_right != digit_from_left:  # If they are different, we exit
        break
    from_left = from_left + 1  # Move to the next digit on the left
    from_right = from_right - 1  # Move to the next digit on the right
    number_from_right = number_from_right - (
        digit_from_right * (10**from_right)
    )  # Adjust ni to remove the previous digit
    number_from_left = int(number_from_left / 10)  # Adjust nf to remove the last digit

if digit_from_right == digit_from_left:
    print(f"{n} is a palindrome")
else:
    print(f"{n} is not a palindrome")
