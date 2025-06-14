##############################################################################
# Python From Scratch
# Author: Nilo Ney Coutinho Menezes
# Editora Novatec (c) 2010-2025 - LogiKraft 2025
# Site: https://pythonfromscratch.com
# ISBN: 978-85-7522-949-1 (Paperback), 978-85-7522-950-7 (hardcover), 978-85-7522-951-4 (ebook)
#
# File: chapter 09/exercise-09-32.py.py
##############################################################################
import sys
import os.path

if len(sys.argv) < 2:
    print("Enter the name of the file or directory to check as a parameter!")
    sys.exit(1)

name = sys.argv[1]
if os.path.isdir(name):
    print(f"The directory {name} exists.")
elif os.path.isfile(name):
    print(f"The file {name} exists.")
else:
    print(f"{name} does not exist.")
