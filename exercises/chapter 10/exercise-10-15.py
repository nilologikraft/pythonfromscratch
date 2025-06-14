##############################################################################
# Python From Scratch
# Author: Nilo Ney Coutinho Menezes
# Editora Novatec (c) 2010-2025 - LogiKraft 2025
# Site: https://pythonfromscratch.com
# ISBN: 978-85-7522-949-1 (Paperback), 978-85-7522-950-7 (hardcover), 978-85-7522-951-4 (ebook)
#
# File: chapter 10/exercise-10-15.py.py
##############################################################################
from collections import UserList


class UniqueList(UserList):
    def __init__(self, elem_class, enumerable=None):
        super().__init__(enumerable)
        self.elem_class = elem_class

    def append(self, elem):
        self.check_type(elem)
        if elem not in self.data:
            super().append(elem)

    def extend(self, iterable):
        for elem in iterable:
            self.append(elem)

    def __setitem__(self, position, elem):
        self.check_type(elem)
        if elem not in self.data:
            super().__setitem__(position, elem)

    def check_type(self, elem):
        if not isinstance(elem, self.elem_class):
            raise TypeError("Invalid type")
