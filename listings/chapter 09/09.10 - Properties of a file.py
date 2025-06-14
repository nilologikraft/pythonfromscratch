##############################################################################
# Python From Scratch
# Author: Nilo Ney Coutinho Menezes
# Editora Novatec (c) 2010-2025 - LogiKraft 2025
# Site: https://pythonfromscratch.com
# ISBN: 978-85-7522-949-1 (Paperback), 978-85-7522-950-7 (hardcover), 978-85-7522-951-4 (ebook)
#
# File: chapter 09/09.10 - Properties of a file.py
##############################################################################
import os
import os.path
import time
import sys
name = sys.argv[1]
print(f"Name : {name}")
print(f"Size: {os.path.getsize(name)}")
print(f"Created: {time.ctime(os.path.getctime(name))}")
print(f"Modified: {time.ctime(os.path.getmtime(name))}")
print(f"Accessed: {time.ctime(os.path.getatime(name))}")
