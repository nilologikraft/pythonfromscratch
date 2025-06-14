##############################################################################
# Python From Scratch
# Author: Nilo Ney Coutinho Menezes
# Editora Novatec (c) 2010-2025 - LogiKraft 2025
# Site: https://pythonfromscratch.com
# ISBN: 978-85-7522-949-1 (Paperback), 978-85-7522-950-7 (hardcover), 978-85-7522-951-4 (ebook)
#
# File: chapter 13/13.06-3 - Layout of the drawing application.py
##############################################################################
import tkinter as tk
import tkinter.ttk as ttk


class App(tk.Tk):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.frame = ttk.Frame(self)
        self.create_toolbar()
        self.create_drawing_area()
        self.title("Drawing")
        self.geometry("800x600")
        self.frame.pack(expand=True, fill="both")
        self.cross = []
        self.cross.append(self.canvas.create_line((0, 0, 0, 0), dash=[2, 4]))
        self.cross.append(self.canvas.create_line((0, 0, 0, 0), dash=[2, 4]))
        self.foreground_color = "black"
        self.state = 0
        self.xi = None
        self.yi = None
        self.curr_id = 0
        self.tool = self.canvas.create_line

    def create_drawing_area(self):
        self.work = ttk.Frame(self.frame, height=600)
        self.work.grid(column=1, row=0, sticky=tk.NSEW)
        self.frame.grid_columnconfigure(1, weight=1)
        self.frame.grid_rowconfigure(0, weight=1)
        self.canvas = tk.Canvas(self.work, background="white")
        self.canvas.pack(fill=tk.BOTH, expand=True)
        self.canvas.bind("<Motion>", self.mouse_move)
        self.coordinates = tk.Label(self.work, text="Move the mouse")
        self.coordinates.pack(ipadx=10, ipady=10)
        self.canvas.bind("<Button-1>", self.mouse_click)
        self.canvas.bind("<ButtonRelease-1>", self.mouse_release)

    def create_toolbar(self):
        self.toolbar = ttk.Frame(self.frame, width=100, height=600)
        self.toolbar.grid(column=0, row=0, sticky=tk.NS)
        self.bline = ttk.Button(
            self.toolbar, text="Line", padding="10", command=self.line_tool
        )
        self.bline.pack()
        self.boval = ttk.Button(
            self.toolbar, text="Circle", padding="10", command=self.oval_tool
        )
        self.boval.pack()
        self.brectangle = ttk.Button(
            self.toolbar, text="Rectangle", padding="10", command=self.rectangle_tool
        )
        self.brectangle.pack()

    def line_tool(self):
        self.tool = self.canvas.create_line

    def oval_tool(self):
        self.tool = self.canvas.create_oval

    def rectangle_tool(self):
        self.tool = self.canvas.create_rectangle

    def mouse_move(self, event):
        self.coordinates["text"] = f"Mouse x={event.x} y={event.y}"
        self.canvas.coords(
            self.cross[0], event.x, 0, event.x, self.canvas.winfo_height()
        )
        self.canvas.coords(
            self.cross[1], 0, event.y, self.canvas.winfo_width(), event.y
        )
        if self.state == 1:
            self.canvas.coords(self.curr_id, self.xi, self.yi, event.x, event.y)

    def mouse_release(self, event):
        if self.state == 1:
            self.state = 0

    def mouse_click(self, event):
        if self.state == 0:
            self.xi = event.x
            self.yi = event.y
            self.curr_id = self.tool(
                (self.xi, self.yi, event.x, event.y),
                fill=self.foreground_color,
                tags=["drawing"],
            )
            self.state = 1


App().mainloop()
