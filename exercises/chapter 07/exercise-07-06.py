##############################################################################
# Python From Scratch
# Author: Nilo Ney Coutinho Menezes
# Editora Novatec (c) 2010-2025 - LogiKraft 2025
# Site: https://pythonfromscratch.com
# ISBN: 978-85-7522-949-1 (Paperback), 978-85-7522-950-7 (hardcover), 978-85-7522-951-4 (ebook)
#
# File: chapter 07/exercise-07-06.py.py
##############################################################################
first = input("Enter the first string: ")
second = input("Enter the second string: ")
third = input("Enter the third string: ")

if len(second) == len(third):
    result = ""
    for letter in first:
        position = second.find(letter)
        if position != -1:
            result += third[position]
        else:
            result += letter

    if result == "":
        print("All characters were removed.")
    else:
        print(
            f"The characters {second} were replaced by "
            f"{third} in {first}, resulting in: {result}"
        )
else:
    print("ERROR: The second and third strings must have the same length.")
