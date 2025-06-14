##############################################################################
# Python From Scratch
# Author: Nilo Ney Coutinho Menezes
# Editora Novatec (c) 2010-2025 - LogiKraft 2025
# Site: https://pythonfromscratch.com
# ISBN: 978-85-7522-949-1 (Paperback), 978-85-7522-950-7 (hardcover), 978-85-7522-951-4 (ebook)
#
# File: chapter 03/exercise-03-15.py.py
##############################################################################
cigarettes_per_day = int(input("Number of cigarettes per day:"))
years_smoking = float(input("Number of years smoking:"))
reduction_in_minutes = years_smoking * 365 * cigarettes_per_day * 10
# One day has 24 x 60 minutes
reduction_in_days = reduction_in_minutes / (24 * 60)
print("Life time reduction %8.2f days." % reduction_in_days)
