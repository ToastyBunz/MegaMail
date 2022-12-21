import tkinter
# from tkinter import *
from customtkinter import *


# Right frame is not filling the entire right side
# selecting from analytics menu, selected path stays grey

LARGE_FONT = ("Verdana", 12)

class MM(CTk):

    def __init__(self, *args, **kwargs):
        CTk.__init__(self, *args, **kwargs)

        self.title('Mega Mail')
        self.geometry('700x450')
        self.grid_rowconfigure(0, weight=1)
        self.grid_columnconfigure(1, weight=1)

        container = CTkFrame(self)
        container.grid(row=1, column=1)

        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)

        self.frames = {}
        for F in (StartPage, PageOne, PageTwo):
            frame = F(container, self)
            self.frames[F] = frame
            frame.grid(row=0, column=1, sticky='nsew')

        self.show_frame(StartPage)

        navigation = CTkFrame(self, corner_radius=0)
        navigation.grid(row=0, column=0, sticky='nsew')
        navigation.grid_rowconfigure(4, weight=1)

        navigation_frame_label = CTkLabel(navigation, text="Navigation", # image=self.logo_image,
                                          compound="left",
                                          font=CTkFont(size=15, weight="bold"))
        navigation_frame_label.grid(row=0, column=0, padx=20, pady=20)

        analytics_button = CTkButton(navigation, corner_radius=0,
                                     height=40,
                                     border_spacing=10,
                                     text="Analytics",
                                     fg_color="transparent",
                                     text_color=("gray10", "gray90"),
                                     hover_color=("gray70", "gray30"),
                                     # image=self.home_image,
                                     anchor="w",
                                     # command=self.analytics_button_event
                                     )

        analytics_button.grid(row=1, column=0, sticky="ew")

        frame_outlook_button = CTkButton(navigation, corner_radius=0, height=40,
                                         border_spacing=10, text="Outlook",
                                         fg_color="transparent", text_color=("gray10", "gray90"),
                                         hover_color=("gray70", "gray30"),
                                         # image=self.chat_image,
                                         anchor="w",
                                         # command=self.frame_outlook_button_event
                                         )
        frame_outlook_button.grid(row=2, column=0, sticky="ew")

        frame_gmail_button = CTkButton(navigation, corner_radius=0, height=40,
                                       border_spacing=10, text="Gmail",
                                       fg_color="transparent", text_color=("gray10", "gray90"),
                                       hover_color=("gray70", "gray30"),
                                       # image=self.add_user_image,
                                       anchor="w",
                                       # command=self.frame_gmail_button_event
                                       )
        frame_gmail_button.grid(row=3, column=0, sticky="ew")

        appearance_mode_menu = CTkOptionMenu(navigation,
                                             values=["System", "Light", "Dark"],
                                             # command=self.change_appearance_mode_event
                                             )
        appearance_mode_menu.grid(row=6, column=0, padx=20, pady=20, sticky="s")

    def show_frame(self, cont):
        frame = self.frames[cont]
        frame.tkraise()


class StartPage(CTkFrame):

    def __init__(self, parent, controller):
        CTkFrame.__init__(self, parent, corner_radius=0, fg_color="transparent")
        self.grid_columnconfigure(0, weight=1)

        label = CTkLabel(self, text='Mega Mail', font=LARGE_FONT)
        label.pack(container, row=0, column=0, pady=10, padx=10)

        button_1 = CTkButton(self, text="This feature is not ready yet")
        button_1.grid(row=1, column=0, padx=20, pady=10)

class PageOne(CTkFrame):

    def __init__(self, parent, controller):
        CTkFrame.__init__(self, parent, corner_radius=0, fg_color="transparent")
        # self.grid(row=0, column=1)
        self.grid_columnconfigure(0, weight=1)

        label = CTkLabel(self, text='Mega Mail', font=LARGE_FONT, anchor='n')
        label.grid(pady=10, padx=10)

        button_1 = CTkButton(self, text="This feature is not ready yet")
        button_1.grid(row=1, column=0, padx=20, pady=10)

class PageTwo(CTkFrame):

    def __init__(self, parent, controller):
        CTkFrame.__init__(self, parent, corner_radius=0, fg_color="transparent")
        self.grid_columnconfigure(0, weight=1)

        label = CTkLabel(self, text='Mega Mail', font=LARGE_FONT, anchor='n')
        label.grid(pady=10, padx=10)

        button_1 = CTkButton(self, text="This feature is not ready yet")
        button_1.grid(row=1, column=0, padx=20, pady=10)

app = MM()
app.mainloop()
