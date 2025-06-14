##############################################################################
# Python From Scratch
# Author: Nilo Ney Coutinho Menezes
# Editora Novatec (c) 2010-2025 - LogiKraft 2025
# Site: https://pythonfromscratch.com
# ISBN: 978-85-7522-949-1 (Paperback), 978-85-7522-950-7 (hardcover), 978-85-7522-951-4 (ebook)
#
# File: chapter 08/08.15 - my_sum function with an undetermined number of parameters.py
##############################################################################
def my_sum(*args):
    s = 0
    for x in args:
        s += x
    return s
my_sum(1, 2)
3
my_sum(2)
2
my_sum(5, 6, 7, 8)
26
my_sum(9, 10, 20, 30, 40)
109
my_sum()
0
