##############################################################################
# Python From Scratch
# Author: Nilo Ney Coutinho Menezes
# Editora Novatec (c) 2010-2025 - LogiKraft 2025
# Site: https://pythonfromscratch.com
# ISBN: 978-85-7522-949-1 (Paperback), 978-85-7522-950-7 (hardcover), 978-85-7522-951-4 (ebook)
#
# File: chapter 10/exercise-10-05.py.py
##############################################################################
class Television:
    def __init__(self, min=2, max=14):
        self.powered = False
        self.channel = min
        self.min_channel = min
        self.max_channel = max

    def channel_down(self):
        if self.channel - 1 >= self.min_channel:
            self.channel -= 1
        else:
            self.channel = self.max_channel

    def channel_up(self):
        if self.channel + 1 <= self.max_channel:
            self.channel += 1
        else:
            self.channel = self.min_channel


tv = Television(min=1, max=22)
tv.channel_down()
print(tv.channel)
tv.channel_up()
print(tv.channel)

tv2 = Television(min=2, max=64)
tv2.channel_down()
print(tv2.channel)
tv2.channel_up()
print(tv2.channel)
