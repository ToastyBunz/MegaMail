from customtkinter import *
from tkinter import ttk

class MM(CTk):
    def __init__(self, *args, **kwargs):
        CTk.__init__(self, *args, **kwargs)

        self.title('CTK Testing')
        self.geometry('700x450')

        self.my_notebook = ttk.Notebook()
        self.my_notebook.pack(pady=10)

        self.frame_1 = CTkFrame(self, width=500, height=500)
        self.frame_2 = CTkFrame(self, width=500, height=500)

        self.frame_1.pack(fill='both', expand=1)
        self.frame_2.pack(fill='both', expand=1)



        self.my_notebook.add(self.frame_1, text='blue')
        self.my_notebook.add(self.frame_2, text='red')

app = MM()
app.mainloop()


