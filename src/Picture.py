import tkinter as tk
from tkinter import ttk
from Square import Square
from Triangle import Triangle
from Rect import Rectangle
from Circle import Circle


class Picture:
    def __init__(self, root=None):
        self.root = root
        self.root.title("House Drawing Application")
        self.root.geometry("800x600")

        # Create main frame
        main_frame = ttk.Frame(root)
        main_frame.pack(fill=tk.BOTH, expand=True, padx=10, pady=10)

        # Create canvas for drawing
        self.canvas = tk.Canvas(main_frame, width=800, height=800, bg='lightblue')
        self.canvas.pack(side=tk.LEFT, padx=(0, 10))

        self.wall = None
        self.window = None
        self.roof = None
        self.sun = None
        self.treeGroove = None



    def draw(self):
        
        # Bottom Row of House
        self.wall = Square(canvas=self.canvas, size=100, color="red", fill="red", line=2)
        self.wall.move_horizontal(300)
        self.wall.move_vertical(420)
        self.wall.make_visible()

        self.wall = Square(canvas=self.canvas, size=100, color="red", fill="red", line=2)
        self.wall.move_horizontal(400)
        self.wall.move_vertical(420)
        self.wall.make_visible()

        self.wall = Square(canvas=self.canvas, size=100, color="red", fill="red", line=2)
        self.wall.move_horizontal(500)
        self.wall.move_vertical(420)
        self.wall.make_visible()

        self.wall = Square(canvas=self.canvas, size=100, color="red", fill="red", line=2)
        self.wall.move_horizontal(600)
        self.wall.move_vertical(420)
        self.wall.make_visible()

        # # Middle Row of House
        self.wall = Square(canvas=self.canvas, size=100, color="gray", fill="gray", line=2)
        self.wall.move_horizontal(330)
        self.wall.move_vertical(320)
        self.wall.make_visible()

        self.wall = Square(canvas=self.canvas, size=100, color="gray", fill="gray", line=2)
        self.wall.move_horizontal(430)
        self.wall.move_vertical(320)
        self.wall.make_visible()

        self.wall = Square(canvas=self.canvas, size=100, color="gray", fill="gray", line=2)
        self.wall.move_horizontal(530)
        self.wall.move_vertical(320)
        self.wall.make_visible()


        # # Top Row of House
        self.wall = Square(canvas=self.canvas, size=100, color="black", fill="black", line=2)
        self.wall.move_horizontal(350)
        self.wall.move_vertical(220)
        self.wall.make_visible()

        self.wall = Square(canvas=self.canvas, size=100, color="black", fill="black", line=2)
        self.wall.move_horizontal(450)
        self.wall.move_vertical(220)
        self.wall.make_visible()


        

        # self.window = Square(canvas=self.canvas, size=30, color="black", fill="black", line=1)
        # self.window.move_horizontal(110)
        # self.window.move_vertical(100)
        # self.window.make_visible()

        # The beginning of my tree
        self.wall = Rectangle(canvas=self.canvas, width=80, height=150, color="brown", fill="brown", line=2)
        self.wall.move_horizontal(40)  # X: 60 (default) + 540 = 600
        self.wall.move_vertical(370)    # Y: 50 (default) + 500 = 550
        self.wall.make_visible()

        # Left Circle
        self.treeGroove = Circle(canvas=self.canvas, diameter=100, color="lightblue", fill="lightblue", line=1)
        self.treeGroove.move_horizontal(5)
        self.treeGroove.move_vertical(380)
        self.treeGroove.make_visible()

        # Right Circle
        self.treeGroove = Circle(canvas=self.canvas, diameter=100, color="lightblue", fill="lightblue", line=1)
        self.treeGroove.move_horizontal(130)
        self.treeGroove.move_vertical(380)
        self.treeGroove.make_visible()

        # Bushes
        self.treeGroove = Circle(canvas=self.canvas, diameter=100, color="lightgreen", fill="green", line=1)
        self.treeGroove.move_horizontal(100)
        self.treeGroove.move_vertical(290)
        self.treeGroove.make_visible()

        self.treeGroove = Circle(canvas=self.canvas, diameter=100, color="lightgreen", fill="green", line=1)
        self.treeGroove.move_horizontal(40)
        self.treeGroove.move_vertical(290)
        self.treeGroove.make_visible()

        self.treeGroove = Circle(canvas=self.canvas, diameter=100, color="green", fill="lightgreen", line=1)
        self.treeGroove.move_horizontal(70)
        self.treeGroove.move_vertical(230)
        self.treeGroove.make_visible()


        # --------------------------------------------

        self.roof = Triangle(canvas=self.canvas, height=120, width=350, color="black", fill="green", line=2)
        self.roof.move_horizontal(300)
        self.roof.move_vertical(275)
        self.roof.make_visible()

        self.sun = Circle(canvas=self.canvas, diameter=100, color="yellow", fill="orange", line=1)
        self.sun.move_horizontal(200)
        self.sun.move_vertical(-10)
        self.sun.make_visible()

    def set_black_and_white(self):
        if self.wall:
            self.wall.change_color("black")
            self.window.change_color("white")
            self.roof.change_color("black")
            self.sun.change_color("black")

    def set_color(self):
        if self.wall:
            self.wall.change_color("red")
            self.window.change_color("black")
            self.roof.change_color("green")
            self.sun.change_color("yellow")
