##############################################################################
# Python From Scratch
# Author: Nilo Ney Coutinho Menezes
# Editora Novatec (c) 2010-2025 - LogiKraft 2025
# Site: https://pythonfromscratch.com
# ISBN: 978-85-7522-949-1 (Paperback), 978-85-7522-950-7 (hardcover), 978-85-7522-951-4 (ebook)
#
# File: chapter 13/13.12 - Window Class.py
##############################################################################
import tkinter as tk
import tkinter.ttk as ttk
from site_register import Site
from date import Date

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
        self.date.set(self.site.date)
        self.category.set(self.site.category or "")
        self.t_notes.delete("1.0", tk.END)
        self.t_notes.insert("1.0", self.site.notes or "")

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
        self.date = Date(self.f_date)
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
        self.b_cancel = ttk.Button(self.b_frame, text="Cancel", command=self.fecha)
        self.b_cancel.pack(side=tk.LEFT)

    def close(self):
        self.destroy()

    def ok(self):
        self.site.url = self.url.get()
        self.site.category = self.category.get()
        self.site.date = self.date.get()
        self.site.notes = self.t_notas.get("1.0", tk.END)
        if self.on_change:
            self.on_change(self.site)
        self.close()
