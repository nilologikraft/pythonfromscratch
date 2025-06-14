##############################################################################
# Python From Scratch
# Author: Nilo Ney Coutinho Menezes
# Editora Novatec (c) 2010-2025 - LogiKraft 2025
# Site: https://pythonfromscratch.com
# ISBN: 978-85-7522-949-1 (Paperback), 978-85-7522-950-7 (hardcover), 978-85-7522-951-4 (ebook)
#
# File: chapter 13/13.09 - Site Manager.py
##############################################################################
import json
from site_register import Site

class SiteManager:
    def __init__(self):
        self.sites = {}

    def load(self, filename):
        with open(filename) as file:
            data = json.load(file)
        self.sites.clear()
        for record in data:
            site = Site(
                id = record.get("id"),
                category = record.get("category"),
                date_added = record["date"],
                url = record["url"],
                notes = record.get("notes"))
            self.sites[site.id] = site
