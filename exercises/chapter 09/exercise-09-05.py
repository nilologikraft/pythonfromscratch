##############################################################################
# Python From Scratch
# Author: Nilo Ney Coutinho Menezes
# Editora Novatec (c) 2010-2025 - LogiKraft 2025
# Site: https://pythonfromscratch.com
# ISBN: 978-85-7522-949-1 (Paperback), 978-85-7522-950-7 (hardcover), 978-85-7522-951-4 (ebook)
#
# File: chapter 09/exercise-09-05.py.py
##############################################################################
even = open("even.txt", "r")
output = open("even_reversed.txt", "w")

L = even.readlines()
L.reverse()
for line in L:
    output.write(line)

even.close()
output.close()

# Note that we read all lines before doing the reversal
# This approach doesn't work with large files
# Alternative using with:
#
##with open("even.txt","r") as even, open("even_reversed.txt","w") as output:
##    L = even.readlines()
##    L.reverse()
##    for line in L:
##        output.write(line)
