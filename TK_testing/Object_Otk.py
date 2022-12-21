import tkinter
# from tkinter import *
from customtkinter import *

LARGE_FONT = ("Verdana", 12)

class MM(CTk):

    def __init__(self, *args, **kwargs):
        CTk.__init__(self, *args, **kwargs)
        container = CTkFrame(self)
        container.pack(side='top', fill='both', expand=True)

        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)

        self.frames = {}
        for F in (StartPage, PageOne, PageTwo):
            frame = F(container, self)
            self.frames[F] = frame
            frame.grid(row=0, column=0, sticky='nsew')

        self.show_frame(StartPage)

    def show_frame(self, cont):
        frame = self.frames[cont]
        frame.tkraise()

def dumb():
    print('You push da button')

class StartPage(CTkFrame):

    def __init__(self, parent, controller):
        CTkFrame.__init__(self, parent)
        label = CTkLabel(self, text='Mega Mail', font=LARGE_FONT)
        label.pack(pady=10, padx=10)

        button1 = CTkButton(self, text="Page One",
                         command=lambda: controller.show_frame(PageOne))
        button1.pack()
        button2 = CTkButton(self, text="Page Two",
                         command=lambda: controller.show_frame(PageTwo))
        button2.pack()

class PageOne(CTkFrame):

    def __init__(self, parent, controller):
        CTkFrame.__init__(self, parent)
        label = CTkLabel(self, text='Page 1', font=LARGE_FONT)
        label.pack(pady=10, padx=10)

        button1 = CTkButton(self, text="back to Home",
                         command=lambda: controller.show_frame(StartPage))

        button1.pack()

class PageTwo(CTkFrame):

    def __init__(self, parent, controller):
        CTkFrame.__init__(self, parent)
        label = CTkLabel(self, text='Page 2', font=LARGE_FONT)
        label.pack(pady=10, padx=10)

        button1 = CTkButton(self, text="Back to Home",
                         command=lambda: controller.show_frame(StartPage))
        button1.pack()

        button2 = CTkButton(self, text="Page 1",
                         command=lambda: controller.show_frame(PageOne))
        button2.pack()

app = MM()
app.mainloop()
