##############################################################################
# Python From Scratch
# Author: Nilo Ney Coutinho Menezes
# Editora Novatec (c) 2010-2025 - LogiKraft 2025
# Site: https://pythonfromscratch.com
# ISBN: 978-85-7522-949-1 (Paperback), 978-85-7522-950-7 (hardcover), 978-85-7522-951-4 (ebook)
#
# File: chapter 03/exercise-03-09.py.py
##############################################################################
days = int(input("Days:"))
hours = int(input("Hours:"))
minutes = int(input("Minutes:"))
seconds = int(input("Seconds:"))
# One minute has 60 seconds
# One hour has 3600 (60 * 60) seconds
# One day has 24 hours, so 24 * 3600 seconds
total_in_seconds = days * 24 * 3600 + hours * 3600 + minutes * 60 + seconds
print("Converted to seconds equals %10d seconds." % total_in_seconds)
