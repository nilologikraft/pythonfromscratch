##############################################################################
# Python From Scratch
# Author: Nilo Ney Coutinho Menezes
# Editora Novatec (c) 2010-2025 - LogiKraft 2025
# Site: https://pythonfromscratch.com
# ISBN: 978-85-7522-949-1 (Paperback), 978-85-7522-950-7 (hardcover), 978-85-7522-951-4 (ebook)
#
# File: chapter 13/13.13 - Complete Site Manager.py
##############################################################################
import tkinter as tk
import tkinter.ttk as ttk
from tkinter.filedialog import askopenfilename, asksaveasfilename
from tkinter.messagebox import askquestion, showinfo
from manager import SiteManager
from window import Window

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
        self.frame.grid(row=0, column=0, columnspan=2, padx=10, pady=10, sticky=tk.NSEW)
        self.grid_rowconfigure(0, weight=1)
        self.table = ttk.Treeview(
            self.frame, columns=["url", "category", "date", "notes"],
            show="headings")
        self.table.heading("url", text="URL")
        self.table.heading("category", text="Category")
        self.table.column("category", anchor=tk.CENTER)
        self.table.heading("date", text="Date")
        self.table.column("date", anchor=tk.CENTER)
        self.table.heading("notes", text="Notes")
        self.table.grid(row=0, column=0, sticky=tk.NSEW)
        self.table.config(selectmode="browse")
        scrollbar = ttk.Scrollbar(self.frame, orient=tk.VERTICAL, command=self.table.yview)
        self.table.configure(yscroll=scrollbar.set)
        self.table.bind("<Double-Button-1>", self.open_window)
        scrollbar.grid(row=0, column=1, sticky=tk.NS)
        self.frame.grid_columnconfigure(0, weight=1)
        self.frame.grid_rowconfigure(0, weight=1)
        self.frame.pack(expand=True, fill=tk.BOTH, padx=10, pady=10)
        self.menu = tk.Menu(self)
        self.m_file = tk.Menu(self.menu, tearoff=0)
        self.m_file.add_command(label="Load", command=self.load)
        self.m_file.add_command(label="Save", command=self.save)
        self.m_sites = tk.Menu(self.menu, tearoff=0)
        self.m_sites.add_command(label="Add", command=self.add)
        self.m_sites.add_command(label="Delete", command=self.delete)
        self.m_sites.add_separator()
        self.m_sites.add_command(label="Delete all", command=self.delete_all)
        self.menu.add_cascade(label="File", menu=self.m_file)
        self.menu.add_cascade(label="Sites", menu=self.m_sites)
        self.menu.add_command(label="About", command=self.about)
        self.config(menu=self.menu)

    def add(self):
        self.show_site(None)

    def delete(self):
        if selected_id := self.get_selected():
            del self.manager.sites[selected_id]
            self.table.delete(selected_id)

    def delete_all(self):
        if askquestion(title="Delete all sites", message="Are you sure you want to delete all sites?") == "yes":
            self.clear()

    def clear(self):
        self.manager.sites.clear()
        self.table.delete(*self.table.get_children())

    def about(self):
        showinfo(title="About",
            message="Introduction to Programming with Python. \nhttps://pythonfromscratch.com ")

    def load(self):
        if name := askopenfilename(filetypes=[("JSON", "*.json")]):
            self.clear()
            self.manager.load(name)
            self.show_data()

    def save(self):
        if name := asksaveasfilename(
            filetypes=[("JSON", "*.json")], defaultextension=".json"):
            self.manager.save(name)

    def add_site_to_table(self, site):
        self.table.insert("", tk.END,
            values=(site.url, site.category, site.date, site.notes),
            iid=site.id)

    def show_data(self):
        for site in self.manager.sites.values():
            self.add_site_to_table(site)

    def get_selected(self):
        if item_selected := self.table.selection():
            selected_id = item_selected[0]
            return selected_id
        return None

    def open_window(self, event):
        if selected_id := self.get_selected():
            site = self.manager.sites[selected_id]
        else:
            site = None
        self.show_site(site)

    def show_site(self, site):
        self.window = Window(self, site, on_change=self.update)
        self.window.grab_set()

    def update(self, site):
        if self.table.exists(site.id):
            self.table.item(site.id, text="",
                values=(site.url, site.category, site.date, site.notes))
        else:
            self.add_site_to_table(site)
        self.manager.sites[site.id] = site

App().mainloop()
