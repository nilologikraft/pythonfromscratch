##############################################################################
# Python From Scratch
# Author: Nilo Ney Coutinho Menezes
# Editora Novatec (c) 2010-2025 - LogiKraft 2025
# Site: https://pythonfromscratch.com
# ISBN: 978-85-7522-949-1 (Paperback), 978-85-7522-950-7 (hardcover), 978-85-7522-951-4 (ebook)
#
# File: chapter 06/06.08 - Stack of dishes.py
##############################################################################
plate = 5
stack = list(range(1, plate + 1))
while True:
    print(f"\nThere are {len(stack)} plates in the stack")
    print(f"Current stack: {stack}")
    print("Type E to stack a new plate,")
    print("or D to unstack. S to leave.")
    operation = input("Operation (E, D, or S):")
    if operation == "D":
        if len(stack) > 0:
            washed = stack.pop(-1)
            print(f"Plates {washed} washed")
        else:
            print("Empty stack! Nothing to wash.")
    elif operation == "E":
        plate += 1 # New plate
        stack.append(plate)
    elif operation == "S":
        break
    else:
        print("Invalid operation! Just type E, D, or S!")
