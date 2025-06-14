##############################################################################
# Python From Scratch
# Author: Nilo Ney Coutinho Menezes
# Editora Novatec (c) 2010-2025 - LogiKraft 2025
# Site: https://pythonfromscratch.com
# ISBN: 978-85-7522-949-1 (Paperback), 978-85-7522-950-7 (hardcover), 978-85-7522-951-4 (ebook)
#
# File: chapter 06/exercise-06-14.py.py
##############################################################################
available_seats = [10, 2, 1, 3, 0]
sold = [0] * len(available_seats)
while True:
    room = int(input("Room (0 to exit): "))
    if room == 0:
        print("End")
        break
    if room > len(available_seats) or room < 1:
        print("Invalid room")
    elif available_seats[room - 1] == 0:
        print("Sorry, room is full!")
    else:
        seats = int(
            input(
                f"How many seats do you want ({available_seats[room - 1]} available):"
            )
        )
        if seats > available_seats[room - 1]:
            print("That number of seats is not available.")
        elif seats < 0:
            print("Invalid number")
        else:
            available_seats[room - 1] -= seats
            sold[room - 1] += seats
            print(f"{seats} seats sold")
print("\nRoom utilization")
for room, available in enumerate(available_seats):
    print(f"Room {room + 1} – {available} seat(s) available")
print("\nSales by room")
total_sold = 0
for room, sales in enumerate(sold):
    print(f"Room {room + 1} – {sales} ticket(s) sold")
    total_sold += sales
print(f"Total tickets sold: {total_sold}")
