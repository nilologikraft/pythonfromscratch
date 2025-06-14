##############################################################################
# Python From Scratch
# Author: Nilo Ney Coutinho Menezes
# Editora Novatec (c) 2010-2025 - LogiKraft 2025
# Site: https://pythonfromscratch.com
# ISBN: 978-85-7522-949-1 (Paperback), 978-85-7522-950-7 (hardcover), 978-85-7522-951-4 (ebook)
#
# File: chapter 13/13.01 - A first program with tkinter.py
##############################################################################
import tkinter as tk
from tkinter import ttk

root = tk.Tk()
root.title("First Window")
root.geometry("250x50")
frame = ttk.Frame(root)
text = ttk.Label(frame, text="Hello GUI!")
text.pack()

button = ttk.Button(frame, text="Quit", command=root.destroy)
button.pack()
frame.pack(expand=True)
root.mainloop()
