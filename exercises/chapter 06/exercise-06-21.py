##############################################################################
# Python From Scratch
# Author: Nilo Ney Coutinho Menezes
# Editora Novatec (c) 2010-2025 - LogiKraft 2025
# Site: https://pythonfromscratch.com
# ISBN: 978-85-7522-949-1 (Paperback), 978-85-7522-950-7 (hardcover), 978-85-7522-951-4 (ebook)
#
# File: chapter 06/exercise-06-21.py.py
##############################################################################
L1 = [1, 2, 6, 8]
L2 = [3, 6, 8, 9]

print(f"List 1: {L1}")
print(f"List 2: {L2}")

set_1 = set(L1)
set_2 = set(L2)

# Sets support the & operator to perform intersection, that is,
# A & B results in the set of elements present in both A and B
print("Values common to both lists:", set_1 & set_2)
print("Values that only exist in the first:", set_1 - set_2)
print("Values that only exist in the second:", set_2 - set_1)

# Sets support the ^ operator that performs symmetric difference.
# A ^ B results in elements of A not present in B combined
# with elements of B not present in A
# A ^ B = A - B | B - A
print("Elements not repeated in both lists:", set_1 ^ set_2)

# Repeated:
print("First list, without elements repeated in the second:", set_1 - set_2)
