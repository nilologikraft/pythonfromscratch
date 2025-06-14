##############################################################################
# Python From Scratch
# Author: Nilo Ney Coutinho Menezes
# Editora Novatec (c) 2010-2025 - LogiKraft 2025
# Site: https://pythonfromscratch.com
# ISBN: 978-85-7522-949-1 (Paperback), 978-85-7522-950-7 (hardcover), 978-85-7522-951-4 (ebook)
#
# File: chapter 12/exercise-12-09.py.py
##############################################################################
# Functions number, sequence and check pattern from listing 12.5
# Function cpf from exercise 12.07
# Function cnpj from exercise 12.08
import re

CPF_RE = r"^\d{3}\.\d{3}\.\d{3}-\d{2}$"
CNPJ_RE = r"^\d{2}\.\d{3}\.\d{3}/\d{4}-\d{2}$"


def cpf(input):
    return bool(re.match(CPF_RE, input))


# Checks if input is a valid CNPJ, that is:
# A sequence in the format 99.999.999/9999-99
def cnpj(input):
    return bool(re.match(CNPJ_RE, input))


inputs = [
    "12.345.678/9012-34",  # Valid CNPJ
    "12.345.678-9012-34",  # Invalid
    "99.999.999/9999-99",  # Valid CNPJ
    "123.456.789-01",  # Valid CPF
    "23.456.789-01",  # Invalid
    "999.456.789-01",  # Valid CPF
]

for input in inputs:
    print(
        f"{input}:\nis it a CNPJ? {'Yes' if cnpj(input) else 'No'}\nis it a CPF? {'Yes' if cpf(input) else 'No'}\n"
    )
