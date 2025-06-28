##############################################################################
# Python From Scratch
# Author: Nilo Ney Coutinho Menezes
# Editora Novatec (c) 2010-2025 - LogiKraft 2025
# Site: https://pythonfromscratch.com
# ISBN: 978-85-7522-949-1 (Paperback), 978-85-7522-950-7 (hardcover), 978-85-7522-951-4 (ebook)
#
# File: chapter 06/exercise-06-05.py.py
##############################################################################
last = 10
queue = list(range(1, last + 1))
while True:
    print(f"\nThere are {len(queue)} customers in the queue")
    print("Current queue:", queue)
    print("Enter F to add a customer to the end of the queue,")
    print("or A to serve a customer. X to exit.")
    operation = input("Operation (F, A or X):")
    x = 0
    exit = False
    while x < len(operation):
        if operation[x] == "A":
            if len(queue) > 0:
                served = queue.pop(0)
                print(f"Customer {served} served")
            else:
                print("Empty queue! No one to serve.")
        elif operation[x] == "F":
            last += 1  # Increments the new customer's ticket
            queue.append(last)
        elif operation[x] == "X":
            exit = True
            break
        else:
            print(
                f"Invalid operation: {operation[x]} at position {x}! Enter only F, A or X!"
            )
        x += 1
    if exit:
        break
