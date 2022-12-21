import tkinter as tk
from tkinter import ttk

class App(tk.Tk):
    def __init__(self):
        super().__init__()

        self.geometry("500x500")

        # Create the frames
        self.frame1 = tk.Frame(self, bg="red")
        self.frame2 = tk.Frame(self, bg="green")
        self.frame3 = tk.Frame(self, bg="blue")

        self.frame1.pack(fill='both', expand=1)
        self.frame2.pack(fill='both', expand=1)
        self.frame3.pack(fill='both', expand=1)

        # Create the notebook widget
        self.notebook = ttk.Notebook(self)

        # Add the frames to the notebook
        self.notebook.add(self.frame1, text="Frame 1")
        self.notebook.add(self.frame2, text="Frame 2")
        self.notebook.add(self.frame3, text="Frame 3")

        # Pack the notebook
        self.notebook.pack()

app = App()
app.mainloop()