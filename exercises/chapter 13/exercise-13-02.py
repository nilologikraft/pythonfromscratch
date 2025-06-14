##############################################################################
# Python From Scratch
# Author: Nilo Ney Coutinho Menezes
# Editora Novatec (c) 2010-2025 - LogiKraft 2025
# Site: https://pythonfromscratch.com
# ISBN: 978-85-7522-949-1 (Paperback), 978-85-7522-950-7 (hardcover), 978-85-7522-951-4 (ebook)
#
# File: chapter 13/exercise-13-02.py.py
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
        self.save_svg_button = ttk.Button(
            self.toolbar, text="Save SVG", padding="10", command=self.save_svg
        )
        self.save_svg_button.pack(fill="x")
        self.toolbar.grid(column=0, row=0, sticky=tk.NS)

    def undo(self):
        if items := self.canvas.find_withtag("drawing"):
            self.canvas.delete(items[-1])

    def clear(self):
        self.canvas.delete("drawing")

    def create_drawing_dict(self):
        drawing = {}  # Creates a dictionary with the drawn objects
        for item in self.canvas.find_withtag("drawing"):
            drawing[item] = {
                "type": (type := self.canvas.type(item)),
                "coordinates": self.canvas.coords(item),
                "fill": self.canvas.itemcget(item, "fill"),
            }
            if type in ["rectangle", "oval"]:
                outline = self.canvas.itemcget(item, "outline")
                drawing[item]["outline"] = outline
        return drawing

    def save(self):
        name = asksaveasfilename(
            defaultextension=".json", filetypes=[("JSON", ".json")]
        )
        if not name:
            return  # User cancelled

        with open(name, "w") as f:
            json.dump(self.create_drawing_dict(), f)

    def save_svg(self):
        name = asksaveasfilename(defaultextension=".svg", filetypes=[("SVG", ".svg")])
        if not name:
            return
        size = self.canvas.winfo_width(), self.canvas.winfo_height()
        base = f"""<?xml version="1.0" encoding="UTF-8" standalone="no"?>
<svg width="{size[0]}mm" height="{size[1]}mm" viewBox="0 0 {size[0]} {size[1]}" version="1.1" id="svg1" xmlns="http://www.w3.org/2000/svg" xmlns:svg="http://www.w3.org/2000/svg">
    <g id="layer1">"""
        for i, item in enumerate(self.create_drawing_dict().values()):
            x, y, xf, yf = item["coordinates"]
            width, height = xf - x, yf - y
            match item["type"]:
                case "line":
                    base += f"""<path style="fill:none;stroke:{item["fill"]};stroke-width:0.264583px;strokelinecap:butt;stroke-linejoin:miter;stroke-opacity:1" d="m {x},{y} {width},{height}" id="line{i}" />"""
                case "rectangle":
                    base += f"""<rect style="fill:{item["fill"] or "none"};stroke:{item["outline"] or "none"};stroke-width:0.264583" id="rect{i}" width="{width}" height="{height}" x="{item["coordinates"][0]}" y="{item["coordinates"][1]}" />"""
                case "oval":
                    base += f"""<ellipse style="fill:{item["fill"] or "none"};stroke:{item["outline"] or "none"};stroke-width:0.264583" id="oval{i}" cx="{x + width // 2}" cy="{y + height // 2}" rx="{width//2}" ry="{height//2}" />"""

        base += """</g></svg>"""
        with open(name, "w") as f:
            f.write(base)

    def load(self):
        name = askopenfilename(filetypes=[("JSON", ".json")])
        if not name:
            return  # User cancelled
        with open(name, "r") as f:
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
        color = askcolor(title="Background Color")
        self.background_color = color[1] or ""
        self.background_button.config(
            text="Transparent" if self.background_color == "" else "",
            background=self.background_color or "SystemButtonFace",
        )

    def foreground_color(self):
        color = askcolor(title="Foreground Color")
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
        self.coordenadas["text"] = f"Mouse x={event.x} y ={event.y}"
        self.canvas.coords(
            self.cruz[0], event.x, 0, event.x, self.canvas.winfo_height()
        )
        self.canvas.coords(self.cruz[1], 0, event.y, self.canvas.winfo_width(), event.y)
        if self.estado == 1:
            self.canvas.coords(self.curr_id, self.xi, self.yi, event.x, event.y)

    def mouse_click(self, event):
        if self.estado == 0:
            self.xi = event.x
            self.yi = event.y
            self.curr_id = self.ferramenta(
                (self.xi, self.yi, event.x, event.y),
                fill=self.cor_de_frente,
                tags=["desenho"],
            )
            tipo = self.canvas.type(self.curr_id)
            if tipo in ["rectangle", "oval"]:
                self.canvas.itemconfig(
                    self.curr_id,
                    {
                        "outline": self.cor_de_frente,
                        "fill": self.cor_de_fundo,
                    },
                )
            self.estado = 1

    def mouse_release(self, event):
        if self.estado == 1:
            self.estado = 0


App().mainloop()
