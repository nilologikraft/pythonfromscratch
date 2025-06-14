##############################################################################
# Python From Scratch
# Author: Nilo Ney Coutinho Menezes
# Editora Novatec (c) 2010-2025 - LogiKraft 2025
# Site: https://pythonfromscratch.com
# ISBN: 978-85-7522-949-1 (Paperback), 978-85-7522-950-7 (hardcover), 978-85-7522-951-4 (ebook)
#
# File: chapter 09/exercise-09-18.py.py
##############################################################################
# If # appears in the name or phone number of an address book entry,
# an error will occur when reading the file.
# This error occurs because the number of expected fields in the line will be different
# from 2 (name and phone).
# The program has no way of knowing whether the character is part of one field or another.
# One solution to this problem is to replace the # within a field before saving it.
# This way, the field separator in the file won't be confused with the content.
# During reading, the replacement must be reversed to obtain the same content.
