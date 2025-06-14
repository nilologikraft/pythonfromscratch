##############################################################################
# Python From Scratch
# Author: Nilo Ney Coutinho Menezes
# Editora Novatec (c) 2010-2025 - LogiKraft 2025
# Site: https://pythonfromscratch.com
# ISBN: 978-85-7522-949-1 (Paperback), 978-85-7522-950-7 (hardcover), 978-85-7522-951-4 (ebook)
#
# File: chapter 13/exercise-13-01.py.py
##############################################################################
import tkinter as tk
import tkinter.ttk as ttk
import json
from tkinter.colorchooser import askcolor
from tkinter.filedialog import asksaveasfilename
from tkinter.filedialog import askopenfilename


class App(tk.Tk):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.background_color = ""
        self.foreground_color = "black"
        self.frame = tk.Frame(self)
        self.create_toolbar()
        self.create_drawing_area()
        self.title("Drawing")
        self.geometry("1200x700")
        self.crosshair = []
        self.crosshair.append(self.canvas.create_line((0, 0, 0, 0), dash=[2, 4]))
        self.crosshair.append(self.canvas.create_line((0, 0, 0, 0), dash=[2, 4]))
        self.state = 0
        self.xi = None
        self.yi = None
        self.curr_id = 0
        self.frame.pack(expand=True, fill=tk.BOTH)
        self.tool = self.canvas.create_line

    def create_drawing_area(self):
        self.work_area = tk.Frame(self.frame, height=600)
        self.work_area.grid(column=1, row=0, sticky=tk.NSEW)
        self.frame.grid_columnconfigure(1, weight=1)
        self.frame.grid_rowconfigure(0, weight=1)
        self.canvas = tk.Canvas(self.work_area, background="white")
        self.canvas.pack(fill=tk.BOTH, expand=True)
        self.canvas.bind("<Motion>", self.mouse_move)
        self.canvas.bind("<Button-1>", self.mouse_click)
        self.canvas.bind("<ButtonRelease-1>", self.mouse_release)
        self.coordinates = tk.Label(self.work_area, text="Move the mouse")
        self.coordinates.pack(ipadx=10, ipady=10)

    def create_toolbar(self):
        self.toolbar = tk.Frame(self.frame, width=100, height=600)
        self.line_button = ttk.Button(
            self.toolbar, text="Line", padding="10", command=self.line_tool
        )
        self.line_button.pack()
        self.oval_button = ttk.Button(
            self.toolbar, text="Circle", padding="10", command=self.oval_tool
        )
        self.oval_button.pack()
        self.rectangle_button = ttk.Button(
            self.toolbar,
            text="Rectangle",
            padding="10",
            command=self.rectangle_tool,
        )
        self.rectangle_button.pack()
        undo_button = ttk.Button(
            self.toolbar, text="Undo", padding="10", command=self.undo
        )
        undo_button.pack()
        clear_button = ttk.Button(
            self.toolbar, text="Clear", padding="10", command=self.clear
        )
        clear_button.pack()
        self.foreground_label = ttk.Label(self.toolbar, text="Foreground Color")
        self.foreground_label.pack()
        self.foreground_button = tk.Button(
            self.toolbar,
            text="Color",
            command=self.foreground_color,
            bg=self.foreground_color,
        )
        self.foreground_button.pack(fill="x")
        self.background_label = ttk.Label(self.toolbar, text="Background Color")
        self.background_label.pack()
        self.background_button = tk.Button(
            self.toolbar, text="Transparent", command=self.background_color, bg=None
        )
        self.background_button.pack(fill="x")
        self.save_button = ttk.Button(
            self.toolbar, text="Save", padding="10", command=self.save
        )
        self.save_button.pack(fill="x")
        self.load_button = ttk.Button(
            self.toolbar, text="Load", padding="10", command=self.load
        )
        self.load_button.pack(fill="x")
        self.toolbar.grid(column=0, row=0, sticky=tk.NS)

    def undo(self):
        if items := self.canvas.find_withtag("drawing"):
            self.canvas.delete(items[-1])

    def clear(self):
        self.canvas.delete("drawing")

    def save(self):
        filename = asksaveasfilename(
            defaultextension=".json", filetypes=[("JSON", ".json")]
        )
        if not filename:
            return  # User cancelled
        drawing = {}  # Create a dictionary with the drawn objects
        for item in self.canvas.find_withtag("drawing"):
            drawing[item] = {
                "type": (type := self.canvas.type(item)),
                "coordinates": self.canvas.coords(item),
                "fill": self.canvas.itemcget(item, "fill"),
            }
            if type in ["rectangle", "oval"]:
                outline = self.canvas.itemcget(item, "outline")
                drawing[item]["outline"] = outline
        with open(filename, "w") as f:
            json.dump(drawing, f)

    def load(self):
        filename = askopenfilename(filetypes=[("JSON", ".json")])
        if not filename:
            return  # User cancelled
        with open(filename, "r") as f:
            drawing = json.load(f)
        self.clear()
        for data in drawing.values():
            match data["type"]:
                case "line":
                    self.canvas.create_line(
                        data["coordinates"], fill=data["fill"], tags=["drawing"]
                    )
                case "rectangle":
                    self.canvas.create_rectangle(
                        data["coordinates"],
                        fill=data["fill"],
                        outline=data["outline"],
                        tags=["drawing"],
                    )
                case "oval":
                    self.canvas.create_oval(
                        data["coordinates"],
                        fill=data["fill"],
                        outline=data["outline"],
                        tags=["drawing"],
                    )

    def background_color(self):
        color = askcolor(title="Background color")
        self.background_color = color[1] or ""
        self.background_button.config(
            text="Transparent" if self.background_color == "" else "",
            background=self.background_color or "SystemButtonFace",
        )

    def foreground_color(self):
        color = askcolor(title="Foreground color")
        if color[1]:
            self.foreground_color = color[1]
            self.foreground_button.config(background=self.foreground_color)

    def line_tool(self):
        self.tool = self.canvas.create_line

    def oval_tool(self):
        self.tool = self.canvas.create_oval

    def rectangle_tool(self):
        self.tool = self.canvas.create_rectangle

    def mouse_move(self, event):
        self.coordinates["text"] = f"Mouse x={event.x} y={event.y}"
        self.canvas.coords(
            self.crosshair[0], event.x, 0, event.x, self.canvas.winfo_height()
        )
        self.canvas.coords(
            self.crosshair[1], 0, event.y, self.canvas.winfo_width(), event.y
        )
        if self.state == 1:
            self.canvas.coords(self.curr_id, self.xi, self.yi, event.x, event.y)

    def mouse_click(self, event):
        if self.state == 0:
            self.xi = event.x
            self.yi = event.y
            self.curr_id = self.tool(
                (self.xi, self.yi, event.x, event.y),
                fill=self.foreground_color,
                tags=["drawing"],
            )
            type = self.canvas.type(self.curr_id)
            if type in ["rectangle", "oval"]:
                self.canvas.itemconfig(
                    self.curr_id,
                    {
                        "outline": self.foreground_color,
                        "fill": self.background_color,
                    },
                )
            self.state = 1

    def mouse_release(self, event):
        if self.state == 1:
            self.state = 0


App().mainloop()
