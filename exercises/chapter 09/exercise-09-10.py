##############################################################################
# Python From Scratch
# Author: Nilo Ney Coutinho Menezes
# Editora Novatec (c) 2010-2025 - LogiKraft 2025
# Site: https://pythonfromscratch.com
# ISBN: 978-85-7522-949-1 (Paperback), 978-85-7522-950-7 (hardcover), 978-85-7522-951-4 (ebook)
#
# File: chapter 09/exercise-09-10.py.py
##############################################################################
import sys

if len(sys.argv) < 2:
    print("\nUsage: exercise-09-10.py file1 [file2 file3 fileN]\n\n\n")
    sys.exit(1)

output = open("single_output.txt", "w", encoding="utf-8")
for name in sys.argv[1:]:
    file = open(name, "r", encoding="utf-8")
    for line in file:
        output.write(line)
    file.close()
output.close()
