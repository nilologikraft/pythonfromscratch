##############################################################################
# Python From Scratch
# Author: Nilo Ney Coutinho Menezes
# Editora Novatec (c) 2010-2025 - LogiKraft 2025
# Site: https://pythonfromscratch.com
# ISBN: 978-85-7522-949-1 (Paperback), 978-85-7522-950-7 (hardcover), 978-85-7522-951-4 (ebook)
#
# File: chapter 09/exercise-09-31.py.py
##############################################################################
import os.path

if os.path.isdir("z"):
    print("The directory z exists.")
elif os.path.isfile("z"):
    print("z exists, but it is a file and not a directory.")
else:
    print("The directory z does not exist.")
