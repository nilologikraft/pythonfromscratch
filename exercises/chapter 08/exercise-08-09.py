##############################################################################
# Python From Scratch
# Author: Nilo Ney Coutinho Menezes
# Editora Novatec (c) 2010-2025 - LogiKraft 2025
# Site: https://pythonfromscratch.com
# ISBN: 978-85-7522-949-1 (Paperback), 978-85-7522-950-7 (hardcover), 978-85-7522-951-4 (ebook)
#
# File: chapter 08/exercise-08-09.py.py
##############################################################################
# The program calculates the factorial of 4
# From the printed output messages and program tracing,
# we can conclude that the factorial of 4 is calculated with recursive calls
# in the line: fact = n * factorial(n-1)
#
# Since the factorial call precedes the "Factorial of" line print,
# we can visualize the sequence in stack form, where the calculation is done from outside
# to inside: Calculation of factorial of 4, 3, 2 and 1
# to then proceed to the next line, which prints the results:
# factorial of 1,2,3,4
