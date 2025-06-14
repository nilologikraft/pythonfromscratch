##############################################################################
# Python From Scratch
# Author: Nilo Ney Coutinho Menezes
# Editora Novatec (c) 2010-2025 - LogiKraft 2025
# Site: https://pythonfromscratch.com
# ISBN: 978-85-7522-949-1 (Paperback), 978-85-7522-950-7 (hardcover), 978-85-7522-951-4 (ebook)
#
# File: chapter 13/13.08 - Sites.py
##############################################################################
from uuid import uuid4
from datetime import date

class Site:
    def __init__(self, /, url=None, category=None, date_added=None, id=None, notes=None):
        if id is None:
            id = str(uuid4())
        self.id = id
        if date_added is None:
            date_added = date.today().strftime("%d-%m-%y")
        self.date = date_added
        self.url = url
        self.category = category
        self.notes = notes

    def __str__(self):
        return f"Site {self.id} {self.url} {self.category} {self.notes}"
