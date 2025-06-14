##############################################################################
# Python From Scratch
# Author: Nilo Ney Coutinho Menezes
# Editora Novatec (c) 2010-2025 - LogiKraft 2025
# Site: https://pythonfromscratch.com
# ISBN: 978-85-7522-949-1 (Paperback), 978-85-7522-950-7 (hardcover), 978-85-7522-951-4 (ebook)
#
# File: chapter 10/exercise-10-01.py.py
##############################################################################
class Television:
    def __init__(self):
        self.powered = False
        self.channel = 2
        self.size = 20
        self.brand = "Ching-Ling"


tv = Television()
tv.size = 27
tv.brand = "DingDang"
living_room_tv = Television()
living_room_tv.size = 52
living_room_tv.brand = "XangLa"

print(f"tv size={tv.size} brand={tv.brand}")
print(f"living_room_tv size={living_room_tv.size} brand={living_room_tv.brand}")
