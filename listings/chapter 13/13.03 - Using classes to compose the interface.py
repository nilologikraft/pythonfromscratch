##############################################################################
# Python From Scratch
# Author: Nilo Ney Coutinho Menezes
# Editora Novatec (c) 2010-2025 - LogiKraft 2025
# Site: https://pythonfromscratch.com
# ISBN: 978-85-7522-949-1 (Paperback), 978-85-7522-950-7 (hardcover), 978-85-7522-951-4 (ebook)
#
# File: chapter 13/13.03 - Using classes to compose the interface.py
##############################################################################
import tkinter as tk
from tkinter import ttk

class Application(tk.Tk):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.counter_1 = 0
        self.counter_2 = 0
        self.title("Counters")
        self.geometry("250x100")
        self.create_frame()

    def create_frame(self):
        self.frame = ttk.Frame(self)
        self.l_counter_1 = ttk.Label(
            self.frame, text = self.format_counter(1, self.counter_1))
        self.l_counter_1.pack()
        self.button_1 = ttk.Button(
            self.frame, text="Add to counter 1", command=self.add_to_counter_1)
        self.button_1.pack()
        self.l_counter_2 = ttk.Label(
            self.frame, text=self.format_counter(2, self.counter_2))
        self.l_counter_2.pack()
        self.button_2 = ttk.Button(
            self.frame, text="Add to counter 2", command=self.add_to_counter_2)
        self.button_2.pack()
        self.frame.pack(expand=True)

    def format_counter(self, counter, value):
        return f"Counter {counter}: {value}"

    def add_to_counter_1(self):
        self.counter_1 += 1
        self.l_counter_1["text"] = self.format_counter(1, self.counter_1)

    def add_to_counter_2(self):
        self.counter_2 += 1
        self.l_counter_2["text"] = self.format_counter(2, self.counter_2)

root = Application()
root.mainloop()
