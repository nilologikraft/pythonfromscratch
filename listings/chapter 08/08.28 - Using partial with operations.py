##############################################################################
# Python From Scratch
# Author: Nilo Ney Coutinho Menezes
# Editora Novatec (c) 2010-2025 - LogiKraft 2025
# Site: https://pythonfromscratch.com
# ISBN: 978-85-7522-949-1 (Paperback), 978-85-7522-950-7 (hardcover), 978-85-7522-951-4 (ebook)
#
# File: chapter 08/08.28 - Using partial with operations.py
##############################################################################
import operator
from functools import partial
def execute(operation, symbol, operand1, operand2):
    result = operation(float(operand1), float(operand2))
    print(f"{operand1} {symbol} {operand2} = {result}")
operations = {
    "+": partial(execute, operator.add, "+"),
    "-": partial(execute, operator.sub, "-"),
    "*": partial(execute, operator.mul, "×"),
    "/": partial(execute, operator.truediv, "÷")}
operand1 = input("Operator 1: ")
operand2 = input("Operator 2: ")
operation = input("Operation: ").strip()
if operation in operations:
    operations[operation](operand1, operand2)
else:
    print("Invalid operation!")
