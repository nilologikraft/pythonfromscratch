##############################################################################
# Python From Scratch
# Author: Nilo Ney Coutinho Menezes
# Editora Novatec (c) 2010-2025 - LogiKraft 2025
# Site: https://pythonfromscratch.com
# ISBN: 978-85-7522-949-1 (Paperback), 978-85-7522-950-7 (hardcover), 978-85-7522-951-4 (ebook)
#
# File: chapter 05/exercise-05-27.a.py.py
##############################################################################
# To solve this problem, we can use strings, as presented in section 3.4 of the book
# Note that we are reading the number without converting it to int or float,
# this way the value of s will be a string
number = input("Enter the number to verify, without spaces:")
from_left = 0
from_right = len(number) - 1  # position of the last character in the string
while from_right > from_left and number[from_left] == number[from_right]:
    from_right = from_right - 1
    from_left = from_left + 1
if number[from_left] == number[from_right]:
    print(f"{number} is a palindrome")
else:
    print(f"{number} is not a palindrome")
