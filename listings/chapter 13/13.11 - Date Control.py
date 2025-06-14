##############################################################################
# Python From Scratch
# Author: Nilo Ney Coutinho Menezes
# Editora Novatec (c) 2010-2025 - LogiKraft 2025
# Site: https://pythonfromscratch.com
# ISBN: 978-85-7522-949-1 (Paperback), 978-85-7522-950-7 (hardcover), 978-85-7522-951-4 (ebook)
#
# File: chapter 13/13.11 - Date Control.py
##############################################################################
import tkinter as tk
import tkinter.ttk as ttk

class Date(ttk.Frame):
    def __init__(self, parent, min_year=00, max_year=40):
        super().__init__(parent)
        self.min_year = min_year
        self.max_year = max_year
        self.day = tk.StringVar()
        self.month = tk.StringVar()
        self.ano = tk.StringVar()
        self.create_controls()

    def set(self, date):
        day, month, year = date.split("-")
        self.day.set(day)
        self.month.set(month)
        self.year.set(year)

    def get(self):
        return f"{self.day.get()}-{self.month.get()}-{self.year.get()}"

    def create_controls(self):
        self.c_dia = ttk.Combobox(
            self,
            textvariable= self.day,
            width=3,
            values=[f"{d:02d}" for d in range(1, 32)],
            state="readonly")
        self.c_day.pack(side=tk.LEFT)
        self.c_month = ttk.Combobox(
            self,
            textvariable= self.month,
            values=[f"{m:02d}" for m in range(1, 13)],
            width=3,
            state="readonly")
        self.c_month.pack(side=tk.LEFT)
        self.c_year = ttk.Combobox(
            self,
            textvariable=self.year,
            values=[f"{m:02d}" for m in range(self.min_year, self.max_year + 1)],
            width=6,
            state="readonly")
        self.c_year.pack(side=tk.LEFT)
