import tkinter
# from tkinter import *
import customtkinter
from customtkinter import *


"""Notes for tomorrow
Goal 3 frames
1. Fix framing Analytics
2. Outlook emails column, charts, and treeview of pandas
3. Contacts ALL treeview (treeview), Groups (buttons treeview), import excel/csv
4. Gmail settings menu/Outlook"""

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


LARGE_FONT = ("Verdana", 20)

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
        self.gmail_button = CTkButton(self.navigation_frame, corner_radius=0, height=40,
                                       border_spacing=10, text="Gmail",
                                       fg_color="transparent", text_color=("gray10", "gray90"),
                                       hover_color=("gray70", "gray30"),
                                       # image=self.add_user_image,
                                       anchor="w",
                                       command= lambda: self.show_frame(GmailPage, 'gmail')
                                       )
        self.gmail_button.grid(row=1, column=0, sticky="ew")

        # Outlook button
        self.outlook_button = CTkButton(self.navigation_frame, corner_radius=0, height=40,
                                        border_spacing=10, text="Outlook",
                                        fg_color="transparent", text_color=("gray10", "gray90"),
                                        hover_color=("gray70", "gray30"),
                                        # image=self.chat_image,
                                        anchor="w",
                                        command= lambda: self.show_frame(OutlookPage, 'outlook')
                                        )
        self.outlook_button.grid(row=2, column=0, sticky="ew")

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
                                          command=lambda: self.show_frame(AnalyticsPage, 'analytics')
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
                                         command=lambda: self.show_frame(ContactsPage, 'contacts')
                                         )

        self.contacts_button.grid(row=4, column=0, sticky="ew")

        # Appearance mode dropdown
        appearance_mode_menu = CTkOptionMenu(self.navigation_frame,
                                             values=["System", "Light", "Dark"],
                                             command=self.change_appearance_mode_event
                                             )
        appearance_mode_menu.grid(row=6, column=0, padx=20, pady=20, sticky="s")

        # self.container = CTkFrame(self, fg_color='transparent')
        # self.container.grid(row=0, column=1, sticky='nsew')
        #
        # # self.container.grid_rowconfigure(0, weight=1)
        # self.container.grid_columnconfigure(1, weight=1)
        # self.container.grid_rowconfigure(0, weight=1)

        self.frames = {}
        for F in (GmailPage, OutlookPage, AnalyticsPage, ContactsPage):
            frame = F(self, self)
            self.frames[F] = frame
            frame.grid(row=0, column=1, sticky='nsew')

        self.show_frame(GmailPage, 'Gmail')

    def show_frame(self, cont, button_name):
        frame = self.frames[cont]
        frame.tkraise()
        self.gmail_button.configure(fg_color=("gray75", "gray25") if button_name == "gmail" else "transparent")
        self.outlook_button.configure(fg_color=("gray75", "gray25") if button_name == "outlook" else "transparent")
        self.analytics_button.configure(fg_color=("gray75", "gray25") if button_name == "analytics" else "transparent")
        self.contacts_button.configure(fg_color=("gray75", "gray25") if button_name == "contacts" else "transparent")


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

        email_input = CTkEntry(self, placeholder_text="Enter gmail address", width=300)

        jsan_input = CTkEntry(self, placeholder_text="Paste PATH to json gmail key", width=300)

        # Add to Settings window
        # sp3 = CTkLabel(self, text="")
        # ex_label = CTkLabel(self, text="Paste PATH to contacts Excel: ")
        # exel_input = CTkEntry(self, width=60)

        nxt_button_input = CTkButton(self, text='Next>',  # command=check_paths,
                                     width=100)

        email_input.grid(row=2, column=0, pady=50)
        jsan_input.grid(row=3, column=0, pady=20)
        nxt_button_input.grid(row=4, column=1, columnspan=2, sticky='sw', pady=70)


class OutlookPage(CTkFrame):

    def __init__(self, parent, controller):
        CTkFrame.__init__(self, parent, corner_radius=0, fg_color="transparent")
        self.grid_columnconfigure(0, weight=8)
        self.grid_columnconfigure(1, weight=1)

        label = CTkLabel(self, text='Outlook', font=LARGE_FONT, compound='center')
        label.grid(row=0, column=0, pady=10, padx=10, columnspan=2)

        email_input = CTkEntry(self, placeholder_text="Enter Outlook address", width=300)

        jsan_input = CTkEntry(self, placeholder_text="Enter Outlook password", width=300)

        # Add to Settings window
        # sp3 = CTkLabel(self, text="")
        # ex_label = CTkLabel(self, text="Paste PATH to contacts Excel: ")
        # exel_input = CTkEntry(self, width=60)

        nxt_button_input = CTkButton(self, text='Next>',  # command=check_paths,
                                     width=100)

        email_input.grid(row=2, column=0, pady=50)
        jsan_input.grid(row=3, column=0, pady=20)
        nxt_button_input.grid(row=4, column=1, columnspan=2, sticky='sw', pady=70)


class AnalyticsPage(CTkFrame):

    def __init__(self, parent, controller):
        CTkFrame.__init__(self, parent, corner_radius=0, fg_color="transparent")
        self.grid_columnconfigure(0, weight=2)
        self.grid_columnconfigure(1, weight=8)
        self.grid_rowconfigure(1, weight=5)
        self.grid_rowconfigure(2, weight=2)

        label = CTkLabel(self, text='Analytics', font=LARGE_FONT, compound='center')
        label.grid(row=0, column=0, pady=10, padx=10, columnspan=2)

        self.emails_frame = CTkFrame(self, corner_radius=0, fg_color=("gray75", "gray25"))
        self.emails_frame.grid(row=1, column=0, sticky='nsew', rowspan=2)

        self.emails_frame_label = CTkLabel(self.emails_frame, text="Campaigns",
                                           compound="left",
                                           font=CTkFont(size=15, weight="bold"))
        self.emails_frame_label.grid(row=0, column=0, padx=5, pady=10)

        # self.listbox = CtkListbox

        self.charts_frame = CTkFrame(self, corner_radius=0, fg_color='red')
        self.charts_frame.grid(row=1, column=1, sticky='nsew')

        self.spreadsheet_frame = CTkFrame(self, corner_radius=0, fg_color='yellow')
        self.spreadsheet_frame.grid(row=2, column=1, sticky='nsew')



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
