##############################################################################
# Python From Scratch
# Author: Nilo Ney Coutinho Menezes
# Editora Novatec (c) 2010-2025 - LogiKraft 2025
# Site: https://pythonfromscratch.com
# ISBN: 978-85-7522-949-1 (Paperback), 978-85-7522-950-7 (hardcover), 978-85-7522-951-4 (ebook)
#
# File: chapter 10/exercise-10-02.py.py
##############################################################################
class Television:
    def __init__(self, initial_channel, min, max):
        self.powered = False
        self.channel = initial_channel
        self.min_channel = min
        self.max_channel = max

    def channel_down(self):
        if self.channel - 1 >= self.min_channel:
            self.channel -= 1

    def channel_up(self):
        if self.channel + 1 <= self.max_channel:
            self.channel += 1


tv = Television(5, 1, 99)

print(tv.channel)
