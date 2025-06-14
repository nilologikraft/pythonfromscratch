##############################################################################
# Python From Scratch
# Author: Nilo Ney Coutinho Menezes
# Editora Novatec (c) 2010-2025 - LogiKraft 2025
# Site: https://pythonfromscratch.com
# ISBN: 978-85-7522-949-1 (Paperback), 978-85-7522-950-7 (hardcover), 978-85-7522-951-4 (ebook)
#
# File: chapter 08/exercise-08-22.py.py
##############################################################################
import math
import operator
from functools import partial


def execute_unary(operation, symbol, operand1):
    result = operation(float(operand1))
    print(f"{symbol} {operand1} = {result}")


def execute(operation, symbol, operand1, operand2):
    result = operation(float(operand1), float(operand2))
    print(f"{operand1} {symbol} {operand2} = {result}")


operations = {
    "+": partial(execute, operator.add, "+"),
    "-": partial(execute, operator.sub, "-"),
    "*": partial(execute, operator.mul, "×"),
    "/": partial(execute, operator.truediv, "÷"),
    "sqrt": partial(execute_unary, math.sqrt, "square root of "),
    "power": partial(execute, operator.pow, "power"),
}
operand1 = input("Operand 1: ")
operation = input("Operation: ").strip().lower()
if operation in operations:
    if operation == "sqrt":  # Square root has only one operand
        operations[operation](operand1)
    else:
        operand2 = input("Operand 2: ")
        operations[operation](operand1, operand2)
else:
    print("Invalid operation!")
