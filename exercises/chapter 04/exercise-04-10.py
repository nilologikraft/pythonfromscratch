##############################################################################
# Python From Scratch
# Author: Nilo Ney Coutinho Menezes
# Editora Novatec (c) 2010-2025 - LogiKraft 2025
# Site: https://pythonfromscratch.com
# ISBN: 978-85-7522-949-1 (Paperback), 978-85-7522-950-7 (hardcover), 978-85-7522-951-4 (ebook)
#
# File: chapter 04/exercise-04-10.py.py
##############################################################################
a = float(input("First number:"))
b = float(input("Second number:"))
operation = input("Enter the operation to perform (+, -, * or /):")
if operation == "+":
    result = a + b
elif operation == "-":
    result = a - b
elif operation == "*":
    result = a * b
elif operation == "/":
    result = a / b
else:
    print("Invalid operation!")
    result = 0
print("Result: ", result)
