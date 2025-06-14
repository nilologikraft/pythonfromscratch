##############################################################################
# Python From Scratch
# Author: Nilo Ney Coutinho Menezes
# Editora Novatec (c) 2010-2025 - LogiKraft 2025
# Site: https://pythonfromscratch.com
# ISBN: 978-85-7522-949-1 (Paperback), 978-85-7522-950-7 (hardcover), 978-85-7522-951-4 (ebook)
#
# File: chapter 13/13.04 - Adding Counters.py
##############################################################################
import tkinter as tk
from tkinter import ttk

class Counter(ttk.Frame):
    def __init__(self, number, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.counter = 0
        self.number = number
        self.label = ttk.Label(
            self, text=self.format_counter(self.number, self.counter))
        self.label.pack()
        self.button = ttk.Button(
            self, text=f"Add to counter {self.number}", command= self.add_to_counter)
        self.button.pack()
        self.pack()
    def format_counter(self, counter, value):
        return f"Counter {counter}: {value}"
    def add_to_counter(self):
        self.counter += 1
        self.label["text"] = self.format_counter(self.number, self.counter)
class Application(tk.Tk):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.counters = []
        self.create_frame()
    def create_frame(self):
        self.frame = ttk.Frame(self)
        self.button = ttk.Button(
            self.frame, text="Add new counter", command=self.add_counter)
        self.button.pack()
        self.frame.pack(expand=True)

    def add_counter(self):
        new_counter = Counter(len(self.counters) + 1, master=self.frame)
        self.counters.append(new_counter)

root = Application()
root.mainloop()
