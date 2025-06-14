##############################################################################
# Python From Scratch
# Author: Nilo Ney Coutinho Menezes
# Editora Novatec (c) 2010-2025 - LogiKraft 2025
# Site: https://pythonfromscratch.com
# ISBN: 978-85-7522-949-1 (Paperback), 978-85-7522-950-7 (hardcover), 978-85-7522-951-4 (ebook)
#
# File: chapter 13/13.02 - Counting Clicks.py
##############################################################################
import tkinter as tk
from tkinter import ttk

counter_1 = 0
counter_2 = 0

def format_counter(counter, value):
    return f"Counter {counter}: {value}"

def add_to_counter_1():
    global counter_1, l_counter_1
    counter_1 += 1
    l_counter_1["text"] = format_counter(1, counter_1)

def add_to_counter_2():
    global counter_2, l_counter_2
    counter_2 += 1
    l_counter_2["text"] = format_counter(2, counter_2)

root = tk.Tk()
root.title("Counters")
root.geometry("250x100")
frame = ttk.Frame(root)
l_counter_1 = ttk.Label(frame, text=format_counter(1, counter_1))
l_counter_1.pack()
button_1 = ttk.Button(frame, text="Add to counter 1", command=add_to_counter_1)
button_1.pack()
l_counter_2 = ttk.Label(frame, text=format_counter(2, counter_2))
l_counter_2.pack()
button_2 = ttk.Button(frame, text="Add to counter 2", command=add_to_counter_2)
button_2.pack()
frame.pack(expand=True)
root.mainloop()
