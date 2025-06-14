##############################################################################
# Python From Scratch
# Author: Nilo Ney Coutinho Menezes
# Editora Novatec (c) 2010-2025 - LogiKraft 2025
# Site: https://pythonfromscratch.com
# ISBN: 978-85-7522-949-1 (Paperback), 978-85-7522-950-7 (hardcover), 978-85-7522-951-4 (ebook)
#
# File: chapter 13/13.05 - Entering data.py
##############################################################################
import tkinter as tk
from tkinter import ttk
class Application(tk.Tk):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.title("Converter")
        self.create_frame()

    def create_frame(self):
        self.frame = ttk.Frame(self)
        self.l_temperature = ttk.Label(self.frame, text="Temperature:")
        self.l_temperature.pack()
        self.temperature = ttk.Entry(self.frame)
        self.temperature.pack()
        self.button_CF = ttk.Button(
            self.frame,
            text="Celsius to Fahrenheit",
            command=self.celsius_to_fahrenheit)
        self.button_CF.pack()
        self.button_FC = ttk.Button(
            self.frame,
            text="Fahrenheit to Celsius",
            command=self.fahrenheit_to_celsius)
        self.button_FC.pack()
        self.l_result = ttk.Label(self.frame, text="Result")
        self.l_result.pack()
        self.frame.pack(expand=True)
    def celsius_to_fahrenheit(self):
        temperature = float(self.temperature.get())
        fahrenheit = 9 / 5.0 * temperature + 32
        self.l_result["text"] = f"{fahrenheit:5.2f}\u00B0f"
    def fahrenheit_to_celsius(self):
        temperature = float(self.temperature.get())
        celsius = (temperature - 32) * 5 / 9.0
        self.l_result["text"] = f"{celsius:5.2f}\u00B0c"
root = Application()
root.mainloop()
