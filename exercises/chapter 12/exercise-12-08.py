##############################################################################
# Python From Scratch
# Author: Nilo Ney Coutinho Menezes
# Editora Novatec (c) 2010-2025 - LogiKraft 2025
# Site: https://pythonfromscratch.com
# ISBN: 978-85-7522-949-1 (Paperback), 978-85-7522-950-7 (hardcover), 978-85-7522-951-4 (ebook)
#
# File: chapter 12/exercise-12-08.py.py
##############################################################################
# Functions number, sequence and check pattern from listing 12.5
import re

CNPJ_RE = r"^\d{2}\.\d{3}\.\d{3}/\d{4}-\d{2}$"


# Checks if input is a valid CNPJ, that is:
# A sequence in the format 99.999.999/9999-99
def cnpj(input):
    return bool(re.match(CNPJ_RE, input))


inputs = [
    "12.345.678/9012-34",  # Yes
    "12.345.678-9012-34",  # No
    "12.345.678.9012-34",  # No
    "2.345.678/9012-34",  # No
    "12.345.678/9012-4",  # No
    "99.999.999/9999-99",  # Yes
]

for input in inputs:
    print(f"{input}: is it a CNPJ? {'Yes' if cnpj(input) else 'No'}")
