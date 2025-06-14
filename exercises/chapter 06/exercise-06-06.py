##############################################################################
# Python From Scratch
# Author: Nilo Ney Coutinho Menezes
# Editora Novatec (c) 2010-2025 - LogiKraft 2025
# Site: https://pythonfromscratch.com
# ISBN: 978-85-7522-949-1 (Paperback), 978-85-7522-950-7 (hardcover), 978-85-7522-951-4 (ebook)
#
# File: chapter 06/exercise-06-06.py.py
##############################################################################
last = 0
queue1 = []
queue2 = []
while True:
    print(
        f"\nThere are {len(queue1)} customers in queue 1 and {len(queue2)} in queue 2."
    )
    print("Current queue 1:", queue1)
    print("Current queue 2:", queue2)
    print("Enter F to add a customer to the end of queue 1 (or G for queue 2),")
    print("or A to serve queue 1 (or B for queue 2)")
    print("S to exit.")
    operation = input("Operation (F, G, A, B or S):")
    x = 0
    exit = False
    while x < len(operation):
        # Here we'll use queue as a reference to queue 1
        # or queue 2, depending on the operation.
        if operation[x] == "A" or operation[x] == "F":
            queue = queue1
        else:
            queue = queue2
        if operation[x] == "A" or operation[x] == "B":
            if len(queue) > 0:
                served = queue.pop(0)
                print(f"Customer {served} served")
            else:
                print("Empty queue! No one to serve.")
        elif operation[x] == "F" or operation[x] == "G":
            last += 1  # Increments the new customer's ticket
            queue.append(last)
        elif operation[x] == "S":
            exit = True
            break
        else:
            print(
                f"Invalid operation: {operation[x]} at position {x}! Enter only F, G, A, B or S!"
            )
        x = x + 1
    if exit:
        break
