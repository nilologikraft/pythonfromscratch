##############################################################################
# Python From Scratch
# Author: Nilo Ney Coutinho Menezes
# Editora Novatec (c) 2010-2025 - LogiKraft 2025
# Site: https://pythonfromscratch.com
# ISBN: 978-85-7522-949-1 (Paperback), 978-85-7522-950-7 (hardcover), 978-85-7522-951-4 (ebook)
#
# File: chapter 12/exercise-12-07.py.py
##############################################################################
# Checks if input is a valid CPF, that is:
# A sequence in the format 999.999.999-99
# This function does not validate the check digit
import re

CPF_RE = r"^\d{3}\.\d{3}\.\d{3}-\d{2}$"


def cpf(input):
    return bool(re.match(CPF_RE, input))


inputs = [
    "123.456.789-01",  # Yes
    "123456.789-01",  # No
    "123.456.78901",  # No
    "23.456.789-01",  # No
    "123.456.78-01",  # No
    "999.999.999-99",  # Yes
]

for input in inputs:
    print(f"{input}: is it a CPF? {'Yes' if cpf(input) else 'No'}")
