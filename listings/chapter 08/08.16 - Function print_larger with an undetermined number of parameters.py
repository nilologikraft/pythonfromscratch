##############################################################################
# Python From Scratch
# Author: Nilo Ney Coutinho Menezes
# Editora Novatec (c) 2010-2025 - LogiKraft 2025
# Site: https://pythonfromscratch.com
# ISBN: 978-85-7522-949-1 (Paperback), 978-85-7522-950-7 (hardcover), 978-85-7522-951-4 (ebook)
#
# File: chapter 08/08.16 - Function print_larger with an undetermined number of parameters.py
##############################################################################
def print_larger(message, *numbers):
    larger = None
    for e in numbers:
        if larger is None or larger < e:
            larger = e
    print(message, larger)
print_larger("Larger:", 5, 4, 3, 1)
Larger: 5
print_larger("Max:", *[1, 7, 9])
Max: 9
print_larger("Max:")
Max: None
