import inspect
import tkinter
# from tkinter import *
import customtkinter
from customtkinter import *

# inspect.getsource(tkinter.Listbox)

print(inspect.getfile(tkinter.Listbox))


"""Notes for tomorrow
1. should I initialize a new frame inside of the right frame or just have the frames fill the 1 column of root?
2. get Outlook frame to fill full window
3. finish outlook login window
4. finish outlook settings window"""

# Right frame is not filling the entire right side
# selecting from analytics menu, selected path stays grey

# Notebook does not exist in CTK use tabs

'''Order of code blocks
root window
navigation frame
Home Frame ( next to navigation)
Gmail Frame 
- login
- settings
- email
Outlook
- login
- settings
- email
Analytics
- email list
- bar chart / open or responses
Contacts (Tabs)
- all
- groups
- inport
Functions'''


LARGE_FONT = ("Verdana", 12)

class MM(CTk):

    def __init__(self, *args, **kwargs):
        CTk.__init__(self, *args, **kwargs)
        # Root Frame
        self.title('Mega Mail')
        self.geometry('700x450')

        # configure parameters set what percentage of the window
        # is given to each column through the weight (I think max is 10)
        self.grid_rowconfigure(0, weight=1)
        self.grid_columnconfigure(1, weight=9)



        # Create and fill navigation frame
        self.navigation_frame = CTkFrame(self, corner_radius=0)
        self.navigation_frame.grid(row=0, column=0, sticky='nsew')
        self.navigation_frame.grid_rowconfigure(5, weight=1)

        self.navigation_frame_label = CTkLabel(self.navigation_frame, text="Navigation",
                                          compound="left",
                                          font=CTkFont(size=15, weight="bold"))

        self.navigation_frame_label.grid(row=0, column=0, padx=20, pady=20)

        # Creating buttons for Navigation
        # Gmail button
        frame_gmail_button = CTkButton(self.navigation_frame, corner_radius=0, height=40,
                                       border_spacing=10, text="Gmail",
                                       fg_color="transparent", text_color=("gray10", "gray90"),
                                       hover_color=("gray70", "gray30"),
                                       # image=self.add_user_image,
                                       anchor="w",
                                       # command=self.frame_gmail_button_event
                                       )
        frame_gmail_button.grid(row=1, column=0, sticky="ew")

        # Outlook button
        self.frame_outlook_button = CTkButton(self.navigation_frame, corner_radius=0, height=40,
                                         border_spacing=10, text="Outlook",
                                         fg_color="transparent", text_color=("gray10", "gray90"),
                                         hover_color=("gray70", "gray30"),
                                         # image=self.chat_image,
                                         anchor="w",
                                         # command=self.frame_outlook_button_event
                                         )
        self.frame_outlook_button.grid(row=2, column=0, sticky="ew")

        # Analytics Button
        self.analytics_button = CTkButton(self.navigation_frame, corner_radius=0,
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

        self.analytics_button.grid(row=3, column=0, sticky="ew")

        # Contacts button
        self.contacts_button = CTkButton(self.navigation_frame, corner_radius=0,
                                     height=40,
                                     border_spacing=10,
                                     text="Contacts",
                                     fg_color="transparent",
                                     text_color=("gray10", "gray90"),
                                     hover_color=("gray70", "gray30"),
                                     # image=self.home_image,
                                     anchor="w",
                                     # command=self.analytics_button_event
                                     )

        self.contacts_button.grid(row=4, column=0, sticky="ew")

        # Appearance mode dropdown
        appearance_mode_menu = CTkOptionMenu(self.navigation_frame,
                                             values=["System", "Light", "Dark"],
                                             command=self.change_appearance_mode_event
                                             )
        appearance_mode_menu.grid(row=6, column=0, padx=20, pady=20, sticky="s")

        self.container = CTkFrame(self, fg_color='transparent')
        self.container.grid(row=0, column=1, sticky='nsew')

        # self.container.grid_rowconfigure(0, weight=1)
        self.container.grid_columnconfigure(1, weight=1)

        self.frames = {}
        for F in (GmailPage, OutlookPage, AnalyticsPage, ContactsPage):
            frame = F(self.container, self)
            self.frames[F] = frame
            frame.grid(row=0, column=1, sticky='nsew')

        self.show_frame(GmailPage)

    def show_frame(self, cont):
        frame = self.frames[cont]
        frame.tkraise()

    def change_appearance_mode_event(self, new_appearance_mode):
        customtkinter.set_appearance_mode(new_appearance_mode)

# Creating Frames for different paths (Gmail, Outlook, Analytics, Contacts)

class GmailPage(CTkFrame):

    def __init__(self, parent, controller):
        CTkFrame.__init__(self, parent, corner_radius=0, fg_color="transparent")
        self.grid_columnconfigure(0, weight=8)
        self.grid_columnconfigure(1, weight=1)

        label = CTkLabel(self, text='Gmail', font=LARGE_FONT, compound='center')
        label.grid(row=0, column=0, pady=10, padx=10, columnspan=2)

        email_input = CTkEntry(self, placeholder_text="Enter your gmail: ", width=250)

        jsan_input = CTkEntry(self, placeholder_text="Paste PATH to json email key: ", width=250)

        # Add to Settings window
        # sp3 = CTkLabel(self, text="")
        # ex_label = CTkLabel(self, text="Paste PATH to contacts Excel: ")
        # exel_input = CTkEntry(self, width=60)

        # sp4 = CTkLabel(self, text="")
        nxt_button_input = CTkButton(self, text='Next>',  # command=check_paths,
                                     width=50)

        email_input.grid(row=2, column=0, pady=20)
        jsan_input.grid(row=3, column=0, pady=20)

        # sp4.grid(row=7, column=0)
        nxt_button_input.grid(row=4, column=1, columnspan=2)


class OutlookPage(CTkFrame):

    def __init__(self, parent, controller):
        CTkFrame.__init__(self, parent, corner_radius=0, fg_color="transparent")
        # self.grid(row=0, column=1)
        # self.grid_columnconfigure(0, weight=1)

        label = CTkLabel(self, text='Mega Mail', font=LARGE_FONT, anchor='n')
        label.grid(pady=10, padx=10)

        # button_1 = CTkButton(self, text="This feature is not ready yet")
        # button_1.grid(row=1, column=0, padx=20, pady=10)

        # sp1 = CTkLabel(self, text="")
        e_label = CTkLabel(self, text="Enter your gmail: ")
        email_input = CTkLabel(self, width=60)

        # sp2 = CTkLabel(self, text="")
        j_label = CTkLabel(self, text="Paste PATH to json email key: ")
        jsan_input = CTkEntry(self, width=60)

        # Add to Settings window
        # sp3 = CTkLabel(self, text="")
        # ex_label = CTkLabel(self, text="Paste PATH to contacts Excel: ")
        # exel_input = CTkEntry(self, width=60)

        # sp4 = CTkLabel(self, text="")
        nxt_button_input = CTkButton(self, text='Next>',  # command=check_paths,
                                     width=15)

        # sp1.grid(row=1, column=0)
        e_label.grid(row=2, column=0)
        email_input.grid(row=2, column=1)

        # sp2.grid(row=3, column=0)
        j_label.grid(row=3, column=0)
        jsan_input.grid(row=3, column=1)

        # sp4.grid(row=7, column=0)
        nxt_button_input.grid(row=8, column=2)


class AnalyticsPage(CTkFrame):

    def __init__(self, parent, controller):
        CTkFrame.__init__(self, parent, corner_radius=0, fg_color="transparent")
        self.grid_columnconfigure(0, weight=1)

        label = CTkLabel(self, text='Mega Mail', font=LARGE_FONT, anchor='n')
        label.grid(pady=10, padx=10)

        # button_1 = CTkButton(self, text="This feature is not ready yet")
        # button_1.grid(row=1, column=0, padx=20, pady=10)

        sp1 = CTkLabel(self, text="")
        e_label = CTkLabel(self, text="Enter your gmail: ")
        email_input = CTkLabel(self, width=60)

        sp2 = CTkLabel(self, text="")
        j_label = CTkLabel(self, text="Paste PATH to json email key: ")
        jsan_input = CTkEntry(self, width=60)

        # Add to Settings window
        # sp3 = CTkLabel(self, text="")
        # ex_label = CTkLabel(self, text="Paste PATH to contacts Excel: ")
        # exel_input = CTkEntry(self, width=60)

        sp4 = CTkLabel(self, text="")
        nxt_button_input = CTkButton(self, text='Next>',  # command=check_paths,
                                     width=15)

        sp1.grid(row=1, column=0)
        e_label.grid(row=2, column=1)
        email_input.grid(row=2, column=2)

        sp2.grid(row=3, column=0)
        j_label.grid(row=4, column=1)
        jsan_input.grid(row=4, column=2)

        sp4.grid(row=7, column=0)
        nxt_button_input.grid(row=8, column=2)


class ContactsPage(CTkFrame):

    def __init__(self, parent, controller):
        CTkFrame.__init__(self, parent, corner_radius=0, fg_color="transparent")
        self.grid_columnconfigure(0, weight=1)

        label = CTkLabel(self, text='Mega Mail', font=LARGE_FONT, anchor='n')
        label.grid(pady=10, padx=10)

        button_1 = CTkButton(self, text="This feature is not ready yet")
        button_1.grid(row=1, column=0, padx=20, pady=10)


app = MM()
app.mainloop()
