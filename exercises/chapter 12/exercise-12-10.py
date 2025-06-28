##############################################################################
# Python From Scratch
# Author: Nilo Ney Coutinho Menezes
# Editora Novatec (c) 2010-2025 - LogiKraft 2025
# Site: https://pythonfromscratch.com
# ISBN: 978-85-7522-949-1 (Paperback), 978-85-7522-950-7 (hardcover), 978-85-7522-951-4 (ebook)
#
# File: chapter 12/exercise-12-10.py.py
##############################################################################
import re

DOLLARS_RE = r"^(([rR]\$)?(((\d{1,3}\.)?(\d{3}\.)*?\d{3})|(\d{1,3}))(,\d{2})?)$"
# ^ - From the start of the string
# ( - Group of the right part of the expression, before the comma
#  ([rR]\$)? - Optionally can have $
#  ( - Group of the integer part
#   ((\d{1,3}\.)?(\d{3}\.)*?\d{3}) - Group of the integer part with dots separating thousands
#   Required to ensure that parts between dots have 3 digits, except the first one
#   | - or
#   (\d{1,3}) - Group of the integer part without dots
#  ) - Group of the right part
# (,\d{2})? - Optionally can have the decimal part
# )$ - Until the end of the string


def clean_spaces(input):
    return input.replace(" ", "")


def dollars(input):
    # It's easier to clean spaces before validation,
    # since the regular expression is already quite complex
    # Remember: you don't need to use regex for everything!
    input = clean_spaces(input)
    return bool(re.match(DOLLARS_RE, input))


inputs = [
    "$ 1.234,56",  # Yes
    "$ 1.234,56",  # Yes
    "$1.234,56",  # Yes
    "$12.123.234,56",  # Yes
    "1.234,56",  # Yes
    "$1.234,56",  # Yes
    "$234,56",  # Yes
    "$234,56",  # Yes
    "234,56",  # Yes
    "$234",  # Yes
    "$234",  # Yes
    "$2",  # Yes
    "$23",  # Yes
    "234",  # Yes
    "34",  # Yes
    "4",  # Yes
    "$234,4",  # No - Cents must have 2 digits
    "$234,4",  # No - Cents must have 2 digits
    "$1234,4",  # No - Missing . to separate thousands
    "$1234,4",  # No - Missing . to separate thousands
    "$1234.12,4",  # No - Incorrect use of thousands separator (.)
    "$1.24,56",  # No - Irregular, only two numbers after the .
]


for input in inputs:
    print(f"{input}: {dollars(input)}")
