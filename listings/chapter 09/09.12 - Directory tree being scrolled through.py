##############################################################################
# Python From Scratch
# Author: Nilo Ney Coutinho Menezes
# Editora Novatec (c) 2010-2025 - LogiKraft 2025
# Site: https://pythonfromscratch.com
# ISBN: 978-85-7522-949-1 (Paperback), 978-85-7522-950-7 (hardcover), 978-85-7522-951-4 (ebook)
#
# File: chapter 09/09.12 - Directory tree being scrolled through.py
##############################################################################
import os
import sys
for root, directories, files in os.walk(sys.argv[1]):
    print("\nPath:", root)
    for d in directories:
        print(f"  {d}/")
    for f in files:
        print(f"  {f}")
    print(f"{len(directories)} directory(s), {len(files)} file(s)")
