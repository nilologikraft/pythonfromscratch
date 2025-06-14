##############################################################################
# Python From Scratch
# Author: Nilo Ney Coutinho Menezes
# Editora Novatec (c) 2010-2025 - LogiKraft 2025
# Site: https://pythonfromscratch.com
# ISBN: 978-85-7522-949-1 (Paperback), 978-85-7522-950-7 (hardcover), 978-85-7522-951-4 (ebook)
#
# File: chapter 08/08.27 - Without using partial.py
##############################################################################
import operator

def execute(operation, symbol, operand1, operand2):
    result = operation(float(operand1), float(operand2))
    print(f"{operand1} {symbol} {operand2} = {result}")

operand1 = input("Operator 1: ")
operand2 = input("Operator 2: ")
operation = input("Operation: ").strip()
if operation == "+":
    execute(operator.add, operation, operand1, operand2)
elif operation == "-":
    execute(operator.sub, operation, operand1, operand2)
elif operation == "*":
    execute(operator.mul, operation, operand1, operand2)
elif operation == "/":
    execute(operator.truediv, operation, operand1, operand2)
