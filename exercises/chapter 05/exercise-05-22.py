##############################################################################
# Python From Scratch
# Author: Nilo Ney Coutinho Menezes
# Editora Novatec (c) 2010-2025 - LogiKraft 2025
# Site: https://pythonfromscratch.com
# ISBN: 978-85-7522-949-1 (Paperback), 978-85-7522-950-7 (hardcover), 978-85-7522-951-4 (ebook)
#
# File: chapter 05/exercise-05-22.py.py
##############################################################################
while True:
    print(
        """

Menu
----
1 - Addition
2 - Subtraction
3 - Division
4 - Multiplication
5 - Exit

"""
    )
    option = int(input("Choose an option:"))
    if option == 5:
        break
    elif option >= 1 and option < 5:
        n = int(input("Multiplication table of:"))
        x = 1
        while x <= 10:
            if option == 1:
                print(f"{n} + {x} = {n + x}")
            elif option == 2:
                print(f"{n} - {x} = {n - x}")
            elif option == 3:
                print(f"{n} / {x} = {n / x:5.4f}")
            elif option == 4:
                print(f"{n} x {x} = {n * x}")
            x = x + 1
    else:
        print("Invalid option!")
