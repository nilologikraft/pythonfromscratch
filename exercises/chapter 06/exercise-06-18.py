##############################################################################
# Python From Scratch
# Author: Nilo Ney Coutinho Menezes
# Editora Novatec (c) 2010-2025 - LogiKraft 2025
# Site: https://pythonfromscratch.com
# ISBN: 978-85-7522-949-1 (Paperback), 978-85-7522-950-7 (hardcover), 978-85-7522-951-4 (ebook)
#
# File: chapter 06/exercise-06-07.py.py
##############################################################################
expression = input("Enter the sequence of parentheses to validate:")
x = 0
stack = []
while x < len(expression):
    if expression[x] == "(":
        stack.append("(")
    if expression[x] == ")":
        if len(stack) > 0:
            top = stack.pop(-1)
        else:
            stack.append(")")  # Forces error message
            break
    x += 1
if len(stack) == 0:
    print("OK")
else:
    print("Error")
