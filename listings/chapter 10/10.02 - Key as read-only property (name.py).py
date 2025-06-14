##############################################################################
# Python From Scratch
# Author: Nilo Ney Coutinho Menezes
# Editora Novatec (c) 2010-2025 - LogiKraft 2025
# Site: https://pythonfromscratch.com
# ISBN: 978-85-7522-949-1 (Paperback), 978-85-7522-950-7 (hardcover), 978-85-7522-951-4 (ebook)
#
# File: chapter 10/10.02 - Key as read-only property (name.py).py
##############################################################################
from functools import total_ordering
@total_ordering
class Name:
    def __init__(self, name):
        self.name = name
    def __str__(self):
        return self.name
    def __repr__(self):
        return f"<Class {type(self).__name__} in 0x{id(self):x} Name: {self.__name} Key: {self.__key}>"
    def __eq__(self, other):
        return self.name == other.name
    def __lt__(self, other):
        return self.name < other.name
    @property
    def name(self):
        return self.__name
    @name.setter
    def name(self, value):
        if value is None or not value.strip():
            raise ValueError("Name cannot be null or blank")
        self.__name = value
        self.__key = Name.CreateKey(value)
    @property
    def key(self):
        return self.__key
    @staticmethod
    def CreateKey(name):
        return name.strip().lower()
