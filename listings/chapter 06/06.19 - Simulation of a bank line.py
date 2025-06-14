##############################################################################
# Python From Scratch
# Author: Nilo Ney Coutinho Menezes
# Editora Novatec (c) 2010-2025 - LogiKraft 2025
# Site: https://pythonfromscratch.com
# ISBN: 978-85-7522-949-1 (Paperback), 978-85-7522-950-7 (hardcover), 978-85-7522-951-4 (ebook)
#
# File: chapter 06/06.19 - Simulation of a bank line.py
##############################################################################
last = 10  # Initial number of clients
line = list(range (1, last + 1))
while True:
    print(f"\nThere are {len(line)} customers in the line")
    print(f"Current line: {line}")
    print("Type A to add a customer to the end of the line,")
    print("or S to perform the service. X to exit.")
    operation = input("Operation (A, S, or X):")
    if operation == "A":
        last += 1 # Increase the new customer's ticket
        line.append(last)
    elif operation == "S":
        if len(queue) > 0:
            attended = line.pop(0)
            print(f"Customer {attended} served")
        else:
            print("Empty line! Nobody to serve.")
    elif operation == "X":
        break
    else:
        print("Invalid operation! Type A, S, or X!")
