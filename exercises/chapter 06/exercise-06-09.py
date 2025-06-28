##############################################################################
# Python From Scratch
# Author: Nilo Ney Coutinho Menezes
# Editora Novatec (c) 2010-2025 - LogiKraft 2025
# Site: https://pythonfromscratch.com
# ISBN: 978-85-7522-949-1 (Paperback), 978-85-7522-950-7 (hardcover), 978-85-7522-951-4 (ebook)
#
# File: chapter 06/exercise-06-13.py.py
##############################################################################
T = [-10, -8, 0, 1, 2, 5, -2, -4]
minimum = T[
    0
]  # The choice of the first element is arbitrary, could be any valid element
maximum = T[0]
sum = 0
for e in T:
    if e < minimum:
        minimum = e
    if e > maximum:
        maximum = e
    sum = sum + e
print(f"Maximum temperature: {maximum} °C")
print(f"Minimum temperature: {minimum} °C")
print(f"Average temperature: {sum / len(T)} °C")
