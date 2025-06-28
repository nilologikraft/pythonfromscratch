##############################################################################
# Python From Scratch
# Author: Nilo Ney Coutinho Menezes
# Editora Novatec (c) 2010-2025 - LogiKraft 2025
# Site: https://pythonfromscratch.com
# ISBN: 978-85-7522-949-1 (Paperback), 978-85-7522-950-7 (hardcover), 978-85-7522-951-4 (ebook)
#
# File: chapter 02/exercise-02-02.py.py
##############################################################################
# The result of the expression:
# 10 % 3 * 10 ** 2 + 1 - 10 * 4 / 2
# is 81.0
#
# Performing the calculation with the priorities from page 52,
# executing only one operation per line,
# we have the following calculation order:
# 0 --> 10 % 3 * 10 ** 2 + 1 - 10 * 4 / 2
# 1 --> 10 % 3 * 100     + 1 - 10 * 4 / 2
# 2 --> 1      * 100     + 1 - 10 * 4 / 2
# 3 -->          100     + 1 - 10 * 4 / 2
# 4 -->          100     + 1 - 40     / 2
# 5 -->          100     + 1 - 20
# 6 -->          101         - 20
# 7 -->                        81
#
# If you're curious to know why the result
# is 81.0 and not 81, read section 3.2, page 67.
# The division operation always results in a floating point number.
