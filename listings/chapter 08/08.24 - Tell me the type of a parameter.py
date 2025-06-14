##############################################################################
# Python From Scratch
# Author: Nilo Ney Coutinho Menezes
# Editora Novatec (c) 2010-2025 - LogiKraft 2025
# Site: https://pythonfromscratch.com
# ISBN: 978-85-7522-949-1 (Paperback), 978-85-7522-950-7 (hardcover), 978-85-7522-951-4 (ebook)
#
# File: chapter 08/08.24 - Tell me the type of a parameter.py
##############################################################################
import types
def says_the_type(a):
    if isinstance(a, str):
        return "String"
    elif isinstance(a, list):
        return "List"
    elif isinstance(a, dict):
        return "Dictionary"
    elif isinstance(a, int):
        return "Integer number"
    elif isinstance(a, float):
        return "Float number"
    elif isinstance(a, types.functionType):
        return "Function"
    elif isinstance(a, types.BuiltinFunctionType):
        return "Internal function"
    else:
        return str(type(a))
print(says_the_type(10))
print(says_the_type(10.5))
print(says_the_type("Hello"))
print(says_the_type([1, 2, 3]))
print(says_the_type({"a": 1, "b": 50}))
print(says_the_type(print))
print(says_the_type(None))
