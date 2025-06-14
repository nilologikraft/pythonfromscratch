##############################################################################
# Python From Scratch
# Author: Nilo Ney Coutinho Menezes
# Editora Novatec (c) 2010-2025 - LogiKraft 2025
# Site: https://pythonfromscratch.com
# ISBN: 978-85-7522-949-1 (Paperback), 978-85-7522-950-7 (hardcover), 978-85-7522-951-4 (ebook)
#
# File: chapter 08/exercise-08-11.py.py
##############################################################################
def validate_string(s, min_length, max_length):
    length = len(s)
    return min_length <= length <= max_length


print(validate_string("", 1, 5))
print(validate_string("ABC", 2, 5))
print(validate_string("ABCEFG", 3, 5))
print(validate_string("ABCEFG", 1, 10))
