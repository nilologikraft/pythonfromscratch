##############################################################################
# Python From Scratch
# Author: Nilo Ney Coutinho Menezes
# Editora Novatec (c) 2010-2025 - LogiKraft 2025
# Site: https://pythonfromscratch.com
# ISBN: 978-85-7522-949-1 (Paperback), 978-85-7522-950-7 (hardcover), 978-85-7522-951-4 (ebook)
#
# File: chapter 10/exercise-10-03.py.py
##############################################################################
class Television:
    def __init__(self, min, max):
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


tv = Television(2, 10)
tv.channel_down()
print(tv.channel)
tv.channel_up()
print(tv.channel)
