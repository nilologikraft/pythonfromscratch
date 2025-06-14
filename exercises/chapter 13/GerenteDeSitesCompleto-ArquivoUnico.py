##############################################################################
# Python From Scratch
# Author: Nilo Ney Coutinho Menezes
# Editora Novatec (c) 2010-2025 - LogiKraft 2025
# Site: https://pythonfromscratch.com
# ISBN: 978-85-7522-949-1 (Paperback), 978-85-7522-950-7 (hardcover), 978-85-7522-951-4 (ebook)
#
# File: chapter 13/GerenteDeSitesCompleto-ArquivoUnico.py
##############################################################################
import json
import tkinter as tk
import tkinter.ttk as ttk
from tkinter.filedialog import askopenfilename, asksaveasfilename
from tkinter.messagebox import askquestion, showinfo, showerror

from uuid import uuid4
from datetime import date


class Date(ttk.Frame):
    def __init__(self, parent, min_year=00, max_year=40):
        super().__init__(parent)
        self.min_year = min_year
        self.max_year = max_year
        self.day = tk.StringVar()
        self.month = tk.StringVar()
        self.year = tk.StringVar()
        self.create_controls()

    def set(self, date):
        day, month, year = date.split("-")
        self.day.set(day)
        self.month.set(month)
        self.year.set(year)

    def get(self):
        return f"{self.day.get()}-{self.month.get()}-{self.year.get()}"

    def create_controls(self):
        self.c_day = ttk.Combobox(
            self,
            textvariable=self.day,
            width=3,
            values=[f"{d:02d}" for d in range(1, 32)],
            state="readonly",
        )
        self.c_day.pack(side=tk.LEFT)
        self.c_month = ttk.Combobox(
            self,
            textvariable=self.month,
            values=[f"{m:02d}" for m in range(1, 13)],
            width=3,
            state="readonly",
        )
        self.c_month.pack(side=tk.LEFT)
        self.c_year = ttk.Combobox(
            self,
            textvariable=self.year,
            values=[f"{m:02d}" for m in range(self.min_year, self.max_year + 1)],
            width=6,
            state="readonly",
        )
        self.c_year.pack(side=tk.LEFT)


class Site:
    def __init__(self, /, url=None, category=None, date=None, id=None, notes=None):
        if id is None:
            id = str(uuid4())
        self.id = id
        if date is None:
            date = date.today().strftime("%d-%m-%y")
        self.date = date
        self.url = url
        self.category = category
        self.notes = notes

    def __str__(self):
        return f"Site {self.id} {self.url} {self.category} {self.notes}"


class SiteManager:
    def __init__(self):
        self.sites = {}

    def load(self, filename):
        try:
            with open(filename) as file:
                data = json.load(file)
        except FileNotFoundError:
            data = []
        self.sites.clear()
        for item in data:
            site = Site(
                id=item.get("id"),
                category=item.get("category"),
                date=item["date"],
                url=item["url"],
                notes=item.get("notes"),
            )
            self.sites[site.id] = site


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
        self.site.category = self.category.get()
        self.site.date = self.date.get()
        self.site.notes = self.t_notes.get("1.0", tk.END)
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


class App(tk.Tk):
    MIN_X = 800
    MIN_Y = 200

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.title("Interesting Sites Manager")
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
            self.frame, columns=["url", "category", "date", "notes"], show="headings"
        )
        self.table.heading("url", text="URL")
        self.table.heading("category", text="Category")
        self.table.column("category", anchor=tk.CENTER)
        self.table.heading("date", text="Date")
        self.table.column("date", anchor=tk.CENTER)
        self.table.heading("notes", text="Notes")
        self.table.grid(row=0, column=0, sticky=tk.NSEW)
        self.table.config(selectmode="browse")
        scrollbar = ttk.Scrollbar(
            self.frame, orient=tk.VERTICAL, command=self.table.yview
        )
        self.table.configure(yscroll=scrollbar.set)
        self.table.bind("<Double-Button-1>", self.open_window)
        self.tabela.heading("url", text="URL")
        self.tabela.heading("categoria", text="Categoria")
        self.tabela.column("categoria", anchor=tk.CENTER)
        self.tabela.heading("data", text="Data")
        self.tabela.column("data", anchor=tk.CENTER)
        self.tabela.heading("notas", text="Notas")
        self.tabela.grid(row=0, column=0, sticky=tk.NSEW)
        self.tabela.config(selectmode="browse")
        scrollbar = ttk.Scrollbar(
            self.quadro, orient=tk.VERTICAL, command=self.tabela.yview
        )
        self.tabela.configure(yscroll=scrollbar.set)
        self.tabela.bind("<Double-Button-1>", self.abre_janela)
        scrollbar.grid(row=0, column=1, sticky=tk.NS)
        self.quadro.grid_columnconfigure(0, weight=1)
        self.quadro.grid_rowconfigure(0, weight=1)
        self.quadro.pack(expand=True, fill=tk.BOTH, padx=10, pady=10)
        self.menu = tk.Menu(self)
        self.m_arquivo = tk.Menu(self.menu, tearoff=0)
        self.m_arquivo.add_command(label="Ler", command=self.lê)
        self.m_arquivo.add_command(label="Gravar", command=self.grava)
        self.m_sites = tk.Menu(self.menu, tearoff=0)
        self.m_sites.add_command(label="Adiciona", command=self.adiciona)
        self.m_sites.add_command(label="Apaga", command=self.apaga)
        self.m_sites.add_separator()
        self.m_sites.add_command(label="Apaga todos", command=self.apaga_todos)
        self.menu.add_cascade(label="Arquivo", menu=self.m_arquivo)
        self.menu.add_cascade(label="Sites", menu=self.m_sites)
        self.menu.add_command(label="Sobre", command=self.sobre)
        self.config(menu=self.menu)

    def adiciona(self):
        self.mostra_site(None)

    def apaga(self):
        if id_selecionado := self.pega_selecionado():
            del self.gerente.sites[id_selecionado]
            self.tabela.delete(id_selecionado)

    def apaga_todos(self):
        if (
            askquestion(
                title="Apagar todos os sites", message="Confirma apagar todos os sites?"
            )
            == "yes"
        ):
            self.limpa()

    def limpa(self):
        self.gerente.sites.clear()
        self.tabela.delete(*self.tabela.get_children())

    def sobre(self):
        showinfo(
            title="Sobre",
            message="Introdução à Programação com Python.\nhttps://python.nilo.pro.br",
        )

    def lê(self):
        if nome := askopenfilename(filetypes=[("JSON", "*.json")]):
            self.limpa()
            self.gerente.carrega(nome)
            self.mostra_dados()

    def grava(self):
        if nome := asksaveasfilename(
            filetypes=[("JSON", "*.json")], defaultextension=".json"
        ):
            self.gerente.grava(nome)

    def adiciona_site_a_tabela(self, site):
        self.tabela.insert(
            "",
            tk.END,
            values=(site.url, site.categoria, site.data, site.notas),
            iid=site.id,
        )

    def mostra_dados(self):
        for site in self.gerente.sites.values():
            self.adiciona_site_a_tabela(site)

    def pega_selecionado(self):
        if item_selecionado := self.tabela.selection():
            id_selecionado = item_selecionado[0]
            return id_selecionado
        return None

    def abre_janela(self, event):
        if id_selecionado := self.pega_selecionado():
            site = self.gerente.sites[id_selecionado]
        else:
            site = None
        self.mostra_site(site)

    def mostra_site(self, site):
        self.janela = Janela(self, site, on_change=self.atualiza)
        self.janela.grab_set()

    def atualiza(self, site):
        if self.tabela.exists(site.id):
            self.tabela.item(
                site.id,
                text="",
                values=(site.url, site.categoria, site.data, site.notas),
            )
        else:
            self.adiciona_site_a_tabela(site)
        self.gerente.sites[site.id] = site


App().mainloop()
