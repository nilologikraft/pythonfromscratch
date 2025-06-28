##############################################################################
# Python From Scratch
# Author: Nilo Ney Coutinho Menezes
# Editora Novatec (c) 2010-2025 - LogiKraft 2025
# Site: https://pythonfromscratch.com
# ISBN: 978-85-7522-949-1 (Paperback), 978-85-7522-950-7 (hardcover), 978-85-7522-951-4 (ebook)
#
# File: chapter 13/exercise-13-05.py.py
##############################################################################
from datetime import date
import tkinter as tk
import tkinter.ttk as ttk
from tkinter.messagebox import showerror
from site_register import Site
from data import Data


class Window(tk.Toplevel):
    MIN_X = 300
    MIN_Y = 300
    PADXY = 10

    def __init__(self, parent, site, on_change=None):
        super().__init__(parent)
        self.geometry(f"{self.MIN_X}x{self.MIN_Y}")
        self.title("Site")
        self.padding = {"padx": self.PADXY, "pady": self.PADXY}
        self.on_change = on_change
        self.create_controls()
        self.minsize(self.MIN_X, self.MIN_Y)
        self.capture_site(site)

    def capture_site(self, site):
        self.site = site or Site()
        self.url.set(self.site.url or "")
        self.date.set(self.site.data)
        self.category.set(self.site.categoria or "")
        self.t_notes.delete("1.0", tk.END)
        self.t_notes.insert("1.0", self.site.notas or "")

    def create_controls(self):
        self.f_url = ttk.Frame(self)
        self.f_url.grid(row=0, column=0, columnspan=3, sticky=tk.EW, **self.padding)
        self.l_url = ttk.Label(self.f_url, text="URL")
        self.l_url.pack(anchor=tk.W)
        self.url = tk.StringVar()
        self.e_url = ttk.Entry(self.f_url, textvariable=self.url)
        self.e_url.pack(fill=tk.X, expand=True)
        self.f_category = ttk.Frame(self)
        self.f_category.grid(row=1, column=0, sticky=tk.W, **self.padding)
        self.l_category = ttk.Label(self.f_category, text="Category")
        self.l_category.pack(anchor=tk.W)
        self.category = tk.StringVar()
        self.e_category = ttk.Entry(self.f_category, textvariable=self.category)
        self.e_category.pack()
        self.f_date = ttk.Frame(self)
        self.f_date.grid(row=1, column=2, sticky=tk.E, **self.padding)
        self.l_date = ttk.Label(self.f_date, text="Date")
        self.l_date.pack(anchor=tk.W)
        self.date = Data(self.f_date)
        self.date.pack()
        self.f_notes = ttk.Frame(self)
        self.f_notes.grid(row=2, column=0, columnspan=3, sticky=tk.NSEW, **self.padding)
        self.l_notes = ttk.Label(self.f_notes, text="Notes")
        self.l_notes.pack(anchor=tk.W)
        self.t_notes = tk.Text(self.f_notes, height=3)
        self.t_notes.pack(expand=True, fill=tk.BOTH)
        self.grid_columnconfigure(0, weight=2)
        self.grid_columnconfigure(2, weight=1)
        self.grid_rowconfigure(2, weight=1)
        self.b_frame = ttk.Frame(self)
        self.b_frame.grid(row=3, column=0, columnspan=3, **self.padding)
        self.b_ok = ttk.Button(self.b_frame, text="Ok", command=self.ok)
        self.b_ok.pack(side=tk.LEFT)
        self.b_cancel = ttk.Button(self.b_frame, text="Cancel", command=self.close)
        self.b_cancel.pack(side=tk.LEFT)

    def close(self):
        self.destroy()

    def ok(self):
        try:
            self.validate_url()
        except ValueError as e:
            showerror("Error", f"Invalid URL\n{e}")
            return
        try:
            self.validate_date()
        except ValueError:
            showerror("Error", "Invalid date")
            return
        self.site.url = self.url.get()
        self.site.categoria = self.category.get()
        self.site.data = self.date.get()
        self.site.notas = self.t_notes.get("1.0", tk.END)
        if self.on_change:
            self.on_change(self.site)
        self.close()

    def validate_url(self):
        url = self.url.get()
        if not url:
            raise ValueError("URL cannot be empty")
        if not (url.startswith("http://") or url.startswith("https://")):
            raise ValueError("URL must start with http:// or https://")

    def validate_date(self):
        day, month, year = self.date.get().split("-")
        valid_date = date(int(year), int(month), int(day))
        return valid_date
