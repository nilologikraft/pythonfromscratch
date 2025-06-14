##############################################################################
# Python From Scratch
# Author: Nilo Ney Coutinho Menezes
# Editora Novatec (c) 2010-2025 - LogiKraft 2025
# Site: https://pythonfromscratch.com
# ISBN: 978-85-7522-949-1 (Paperback), 978-85-7522-950-7 (hardcover), 978-85-7522-951-4 (ebook)
#
# File: chapter 06/06.11 - Controlling the occupancy of movie theaters.py
##############################################################################
vacant_places = [10, 2, 1, 3, 0]
while True:
    room = int(input("Room (0 to exit): "))
    if room == 0:
        print("End")
        break
    if room > len(vacant_places) or room < 1:
        print("Invalid room")
    elif vacant_places [room - 1] == 0:
        print("Sorry, there are no more seats available!")
    else:
        places = int(input(f"How many places do you want ({vacant_places [room - 1]} vacant):"))
        if  places > vacant_places[room - 1]:
            print("This number of seats is not available.")
        elif places < 0:
            print("Invalid number")
        else:
            vacant_places[room - 1] -= places
            print(f"{places} places sold")
print("Room occupancy")
for room, vacant in enumerate(vacant_places):
    print(f"Room {room + 1} - {vacant} empty place (s)")
