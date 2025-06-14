##############################################################################
# Python From Scratch
# Author: Nilo Ney Coutinho Menezes
# Editora Novatec (c) 2010-2025 - LogiKraft 2025
# Site: https://pythonfromscratch.com
# ISBN: 978-85-7522-949-1 (Paperback), 978-85-7522-950-7 (hardcover), 978-85-7522-951-4 (ebook)
#
# File: chapter 13/13.10 - Site Registration.py
##############################################################################
import tkinter as tk
import tkinter.ttk as ttk
from manager import SiteManager

class App(tk.Tk):
    MIN_X = 800
    MIN_Y = 200
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.title("Web Sites Bookmarker")
        self.geometry(f"{self.MIN_X}x{self.MIN_Y}")
        self.create_controls()
        self.manager = SiteManager()
        self.manager.load("data.json")
        self.show_data()
        self.minsize(self.MIN_X, self.MIN_Y)

    def create_controls(self):
        self.frame = ttk.Frame(self)
        self.frame.grid(
            row=0, column=0, columnspan=2, padx=10, pady=10, sticky=tk.NSEW)
        self.grid_rowconfigure(0, weight=1)
        self.table = ttk.TreeView(
            self.frame,
            columns=["url", "category", "date", "notes"],
            show="headings")
        self.table.heading("url", text="URL")
        self.table.heading("category", text="Category")
        self.table.column("category", anchor=tk.CENTER)
        self.table.heading("date", text="Date")
        self.table.column("date", anchor=tk.CENTER)
        self.table.heading("notes", text="Notes")
        self.table.grid(
            row=0,
            column=0,
            sticky=tk.NSEW)
        self.table.config(selectmode="browse")
        scrollbar = ttk.Scrollbar(
            self.frame, orient=tk.VERTICAL, command=self.table.yview)
        self.table.configure(yscroll=scrollbar.set)
        scrollbar.grid(row=0, column=1, sticky=tk.NS)
        self.frame.grid_columnconfigure(0, weight=1)
        self.frame.grid_rowconfigure(0, weight=1)
        self.frame.pack(expand=True, fill=tk.BOTH, padx=10, pady=10)

    def add_site_to_table(self, site):
        self.table.insert(
            "",
            tk.END,
            values=(site.url, site.category, site.date, site.notes),
            iid=site.id)

    def show_data(self):
        for site in self.manager.sites.values():
            self.add_site_to_table(site)

App().mainloop()
