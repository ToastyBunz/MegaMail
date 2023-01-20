import tkinter
# from tkinter import *
from tkinter import ttk
import customtkinter
from customtkinter import *
from Emails import GPath
from Emails import OPath

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
        self.geometry('1100x600')

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

        self.container = CTkFrame(self, fg_color='transparent')
        self.container.grid(row=0, column=1, sticky='nsew')

        # self.container.grid_rowconfigure(0, weight=1)
        self.container.grid_columnconfigure(1, weight=1)
        self.container.grid_rowconfigure(0, weight=1)

        self.frames = {}
        for F in (GmailPage, AnalyticsPage, ContactsPage, GmailPage_2, GmailPage_3, ABC_info_gmail, GmailPage_4,
                  GmailPage_5, GmailPage_6, GmailPage_7, GmailPage_Sending, OutlookPage, OutlookPage_2, OutlookPage_3,
                  OutlookPage_4, OutlookPage_5, OutlookPage_6, OutlookPage_7, OutlookPage_Sending, ABC_info_outlook):
            frame = F(self.container, self)
            self.frames[F] = frame
            frame.grid(row=0, column=1, sticky='nsew')

        self.show_frame(GmailPage, 'gmail')

    def show_frame(self, cont, button_name):
        frame = self.frames[cont]
        frame.tkraise()
        self.gmail_button.configure(fg_color=("gray75", "gray25") if button_name == "gmail" else "transparent")
        self.outlook_button.configure(fg_color=("gray75", "gray25") if button_name == "outlook" else "transparent")
        self.analytics_button.configure(fg_color=("gray75", "gray25") if button_name == "analytics" else "transparent")
        self.contacts_button.configure(fg_color=("gray75", "gray25") if button_name == "contacts" else "transparent")


    def change_appearance_mode_event(self, new_appearance_mode):
        customtkinter.set_appearance_mode(new_appearance_mode)


# Assign Classes from Opath to Variables
GmailPage = GPath.GmailPage
GmailPage_2 = GPath.GmailPage_2
GmailPage_3 = GPath.GmailPage_3
GmailPage_4 = GPath.GmailPage_4
GmailPage_5 = GPath.GmailPage_5
GmailPage_6 = GPath.GmailPage_6
GmailPage_7 = GPath.GmailPage_7
GmailPage_Sending = GPath.GmailPage_Sending
ABC_info_gmail = GPath.ABC_info


# Assign Classes from OPath to Variables
OutlookPage = OPath.OutlookPage
OutlookPage_2 = OPath.OutlookPage_2
OutlookPage_3 = OPath.OutlookPage_3
OutlookPage_4 = OPath.OutlookPage_4
OutlookPage_5 = OPath.OutlookPage_5
OutlookPage_6 = OPath.OutlookPage_6
OutlookPage_7 = OPath.OutlookPage_7
OutlookPage_Sending = OPath.OutlookPage_Sending
ABC_info_outlook = OPath.ABC_info


class AnalyticsPage(CTkFrame):

    def __init__(self, parent, controller):
        CTkFrame.__init__(self, parent, corner_radius=0, fg_color="transparent")
        self.grid_columnconfigure(0, weight=2)
        self.grid_columnconfigure(1, weight=8)
        self.grid_rowconfigure(2, weight=5)
        self.grid_rowconfigure(3, weight=5)

        label = CTkLabel(self, text='Analytics', font=LARGE_FONT, compound='center')
        label.grid(row=0, column=0, pady=10, padx=10, columnspan=2)

        # create Entry and Listbox
        self.campaign_entry = CTkEntry(self, placeholder_text="Enter campaign or date")
        self.campaign_entry.grid(row=1, column=0, pady=10, sticky='new')

        self.campaigns_listbox = tkinter.Listbox(self, width=17, background=("grey10"),
                                                 borderwidth=3, font=("Helvetica", 12), fg='white', relief=FLAT)
        self.campaigns_listbox.grid(row=2, column=0, sticky='nsew', rowspan=3)


        self.my_list = ["one", "two", "three three three three three", 'four', 'five']
        for i in self.my_list:
            self.campaigns_listbox.insert(END, i)  # can also use END
            self.campaigns_listbox.insert(END, '')  # can also use END



        # TODO Selected listbox anchor appears in spreadsheet frame after select_campaign click
        def select_campaign():
            # campaign_label.configure(text=self.campaigns_listbox.get(ANCHOR))
            return print(self.campaigns_listbox.get(ANCHOR))



        self.select_campaign_button = CTkButton(self, text='Select Campaign', command=select_campaign())
        self.select_campaign_button.grid(row=1, column=1, padx=5, pady=5, sticky='w')

        self.charts_frame = CTkFrame(self, corner_radius=0, fg_color='transparent', border_width=3)
        self.charts_frame.grid(row=2, column=1, sticky='nsew')

        def remove_row():
            pass

        self.spreadsheet_frame = CTkFrame(self, corner_radius=0, fg_color='transparent', border_width=3)
        self.spreadsheet_frame.grid(row=3, column=1, sticky='nsew', rowspan=2)
        self.remove_button = CTkButton(self.spreadsheet_frame, text='Remove', command=remove_row)
        self.remove_button.grid(row=0, column=0, padx=5, pady=5)
        self.remove_all = CTkButton(self.spreadsheet_frame, text='Remove All')
        self.remove_all.grid(row=0, column=1, padx=5, pady=5)


        self.campaign_label = CTkLabel(self.spreadsheet_frame, text='hello')
        self.campaign_label.grid(row=1, column=0)



class ContactsPage(CTkFrame):

    def __init__(self, parent, controller):
        CTkFrame.__init__(self, parent, corner_radius=0, fg_color="transparent")
        self.grid_columnconfigure(0, weight=1)
        self.grid_rowconfigure(1, weight=1)
        contacts_label = CTkLabel(self, text="Contacts", font=LARGE_FONT)
        contacts_label.grid(row=0, column=0)

        contact_tabs = CTkTabview(self)
        contact_tabs.grid(row=1, column=0, sticky='nsew')
        contact_tabs.add(" All  ")
        contact_tabs.add(" Groups")
        contact_tabs.add(" Import  ")

        all_tree = ttk.Treeview(contact_tabs.tab(" All  "))

        # define columns
        all_tree['columns'] = ('Name', 'Email', "Age", 'Company')

        # Formate our columns
        # all_tree.column('#0', width=0)
        all_tree.column("Name", anchor='w')
        all_tree.column("Email", anchor='w')
        all_tree.column("Age", anchor='w')
        all_tree.column("Company", anchor='w')

        # Create Headings
        # all_tree.heading("#0", text="label", anchor='w')
        all_tree.heading("Name", text="Name", anchor='w')
        all_tree.heading("Email", text="Email", anchor='w')
        all_tree.heading("Age", text="Age", anchor='w')
        all_tree.heading("Company", text="Company", anchor='w')

        all_tree.insert(parent='', index='end', iid='0', text='', values=("Name", 'thisismyemail@email.com', 25, 'bs.com'))
        all_tree.grid(row=0, column=0)




app = MM()
app.mainloop()
