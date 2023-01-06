import tkinter
# from tkinter import *
from tkinter import ttk
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
        for F in (GmailPage, OutlookPage, AnalyticsPage, ContactsPage, GmailPage_2, GmailPage_3):
            frame = F(self.container, self)
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

        # input boxes
        email_input = CTkEntry(self, placeholder_text="Enter gmail address", width=300)
        pass_input = CTkEntry(self, placeholder_text="Paste PATH to json gmail key", width=300)
        campaign_input = CTkEntry(self, placeholder_text="New Campaign Name", width=300)

        # Add to Settings window
        # sp3 = CTkLabel(self, text="")
        # ex_label = CTkLabel(self, text="Paste PATH to contacts Excel: ")
        # exel_input = CTkEntry(self, width=60)

        nxt_button_input = CTkButton(self, text='Next>', command=lambda: controller.show_frame(GmailPage_2, 'Gmail'),
                                     width=100)

        label.grid(row=0, column=0, pady=10, padx=10, columnspan=2)
        email_input.grid(row=2, column=0, pady=(50, 30), padx=(135, 0))
        pass_input.grid(row=3, column=0, pady=50, padx=(135, 0))
        campaign_input.grid(row=4, column=0, pady=30, padx=(135, 0))
        nxt_button_input.grid(row=5, column=1, columnspan=2, sticky='sw', pady=70)



class GmailPage_2(CTkFrame):

    def __init__(self, parent, controller):
        CTkFrame.__init__(self, parent, corner_radius=0, fg_color="transparent")
        self.grid_columnconfigure(0, weight=1)
        # self.grid_columnconfigure(1, weight=1)
        self.grid_rowconfigure(3, weight=1)

        from_label = CTkLabel(self, text='From: ', font=LARGE_FONT, compound='center')
        to_label = CTkLabel(self, text='To: ', font=LARGE_FONT, compound='center')

        from_input = CTkEntry(self, placeholder_text="E.G. John Doe or MyCompany.net", width=300)

        # Tab Frame
        recipients_tabs = CTkTabview(self)
        recipients_tabs.add(" All  ")
        recipients_tabs.add(" Groups")
        recipients_tabs.add(" New Group  ")

        # Filling the "All" tab
        all_column_label = CTkLabel(recipients_tabs.tab(" All  "), text="Which column holds emails?")
        all_column_dropdown = CTkOptionMenu(recipients_tabs.tab(" All  "), dynamic_resizing=False, width=250,
                                            values=["Value 1", "Value 2", "Value Long Long Long"])

        # Create a frame for Radio Button and grid them
        all_radbutton_frame = CTkFrame(recipients_tabs.tab(" All  "), fg_color="transparent")
        all_radio_var = tkinter.IntVar(value=0)
        all_radbutton_frame_label = CTkLabel(all_radbutton_frame, text="would you like to greet recipients by name?")
        all_radio_button_no = CTkRadioButton(master=all_radbutton_frame, text='No', variable=all_radio_var, value=0)
        all_radio_button_yes = CTkRadioButton(master=all_radbutton_frame, text='Yes', variable=all_radio_var, value=1)

        # Grids for Rad button Frame
        all_radbutton_frame_label.grid(row=0, column=0, columnspan=2)
        all_radio_button_no.grid(row=1, column=0)
        all_radio_button_yes.grid(row=1, column=2)

        # back to outside radbutton frame
        all_personalize_label = CTkLabel(recipients_tabs.tab(" All  "), text="Which column holds names?")
        all_personalize_dropdown = CTkOptionMenu(recipients_tabs.tab(" All  "), dynamic_resizing=False, width=250,
                                            values=["Value 1", "Value 2", "Value Long Long Long"])

        # gridding the "All" tab
        all_column_label.grid(row=0, column=0)
        all_column_dropdown.grid(row=1, column=0)
        all_radbutton_frame.grid(row=2, column=0, padx=20, pady=(20, 0), sticky='nsew')
        all_personalize_label.grid(row=3, column=0)
        all_personalize_dropdown.grid(row=4, column=0)


        # Filling the Groups Tab
        group_group_label = CTkLabel(recipients_tabs.tab(" Groups"), text="Which group would you like to use?")
        group_column_label = CTkLabel(recipients_tabs.tab(" Groups"), text="Which column holds emails?")

        group_group_dropdown = CTkOptionMenu(recipients_tabs.tab(" Groups"), dynamic_resizing=False, width=250,
                                             values=["Value 1", "Value 2", "Value Long Long Long"])

        group_column_dropdown = CTkOptionMenu(recipients_tabs.tab(" Groups"), dynamic_resizing=False, width=250,
                                              values=["Value 1", "Value 2", "Value Long Long Long"])

        group_radbutton_frame = CTkFrame(recipients_tabs.tab(" Groups"), fg_color="transparent")
        group_radio_var = tkinter.IntVar(value=0)
        group_radbutton_frame_label = CTkLabel(group_radbutton_frame, text="would you like to greet recipients by name?")
        group_radio_button_no = CTkRadioButton(master=group_radbutton_frame, text='No', variable=group_radio_var, value=0)
        group_radio_button_yes = CTkRadioButton(master=group_radbutton_frame, text='Yes', variable=group_radio_var, value=1)

        group_personalize_label = CTkLabel(recipients_tabs.tab(" Groups"), text="Which column holds names?")
        group_personalize_dropdown = CTkOptionMenu(recipients_tabs.tab(" Groups"), dynamic_resizing=False, width=250,
                                                 values=["Value 1", "Value 2", "Value Long Long Long"])

        # inside group radframe griding
        group_radbutton_frame_label.grid(row=0, column=0, sticky='e')
        group_radio_button_no.grid(row=0, column=1, padx=(20, 0))
        group_radio_button_yes.grid(row=0, column=2)


        # grid group objects
        group_group_label.grid(row=0, column=0)
        group_column_label.grid(row=0, column=1)
        group_group_dropdown.grid(row=1, column=0)
        group_column_dropdown.grid(row=1, column=1)
        group_radbutton_frame.grid(row=2, column=0, padx=20, pady=(20, 0), sticky='nsew')
        group_personalize_label.grid(row=3, column=0)
        group_personalize_dropdown.grid(row=4, column=0)


        # Filling New Group tab
        ngroup_name_entry = CTkEntry(recipients_tabs.tab(" New Group  "), placeholder_text="New Group Name", width=300)


        ngroup_tree = ttk.Treeview(recipients_tabs.tab(" New Group  "))

        # define columns
        ngroup_tree['columns'] = ('Name', 'Email', "Age", 'Company')

        # Formate our columns
        # ngroup_tree.column('#0', width=0)
        ngroup_tree.column("Name", anchor='w')
        ngroup_tree.column("Email", anchor='w')
        ngroup_tree.column("Age", anchor='w')
        ngroup_tree.column("Company", anchor='w')

        # Create Headings
        # ngroup_tree.heading("#0", text="label", anchor='w')
        ngroup_tree.heading("Name", text="Name", anchor='w')
        ngroup_tree.heading("Email", text="Email", anchor='w')
        ngroup_tree.heading("Age", text="Age", anchor='w')
        ngroup_tree.heading("Company", text="Company", anchor='w')

        ngroup_tree.insert(parent='', index='end', iid='0', text='', values=("Name", 'thisismyemail@email.com', 25, 'bs.com'))
        ngroup_all_button = CTkButton(recipients_tabs.tab(" New Group  "), text='Add contacts from All')
        ngroup_groups_button = CTkButton(recipients_tabs.tab(" New Group  "), text='Import previous group')
        ngroup_import_button = CTkButton(recipients_tabs.tab(" New Group  "), text='Import new contacts')

        # Filling the "All" tab
        ngroup_column_label = CTkLabel(recipients_tabs.tab(" New Group  "), text="Which column holds emails?")
        ngroup_column_dropdown = CTkOptionMenu(recipients_tabs.tab(" New Group  "), dynamic_resizing=False, width=250,
                                            values=["Value 1", "Value 2", "Value Long Long Long"])

        # Create a frame for Radio Button and grid them
        ngroup_radbutton_frame = CTkFrame(recipients_tabs.tab(" New Group  "), fg_color="transparent")
        ngroup_radio_var = tkinter.IntVar(value=0)
        ngroup_radbutton_frame_label = CTkLabel(ngroup_radbutton_frame, text="would you like to greet recipients by name?")
        ngroup_radio_button_no = CTkRadioButton(master=ngroup_radbutton_frame, text='No', variable=ngroup_radio_var, value=0)
        ngroup_radio_button_yes = CTkRadioButton(master=ngroup_radbutton_frame, text='Yes', variable=ngroup_radio_var, value=1)

        # Grids for Rad button Frame
        ngroup_radbutton_frame_label.grid(row=0, column=0, columnspan=2)
        ngroup_radio_button_no.grid(row=1, column=0)
        ngroup_radio_button_yes.grid(row=1, column=2)

        # back to outside radbutton frame
        ngroup_personalize_label = CTkLabel(recipients_tabs.tab(" New Group  "), text="Which column holds names?")
        ngroup_personalize_dropdown = CTkOptionMenu(recipients_tabs.tab(" New Group  "), dynamic_resizing=False, width=250,
                                                 values=["Value 1", "Value 2", "Value Long Long Long"])


        # Gridding New Group Tab
        ngroup_name_entry.grid(row=0, column=0)
        ngroup_tree.grid(row=1, column=0)
        ngroup_all_button.grid(row=2, column=0, padx=5, pady=5)
        ngroup_groups_button.grid(row=3, column=0, padx=5, pady=5)
        ngroup_import_button.grid(row=4, column=0, padx=5, pady=5)
        ngroup_column_label.grid(row=5, column=0)
        ngroup_column_dropdown.grid(row=6, column=0)
        ngroup_radbutton_frame.grid(row=7, column=0, padx=20, pady=(20, 0), sticky='nsew')
        ngroup_personalize_label.grid(row=8, column=0)
        ngroup_personalize_dropdown.grid(row=9, column=0)


        nxt_button_input = CTkButton(self, text='Use Settings>',  command=lambda: controller.show_frame(GmailPage_3, 'Gmail'),
                                     width=100)
        bck_button_input = CTkButton(self, text='<Back', command=lambda: controller.show_frame(GmailPage, 'gmail'),
                                     width=100)

        from_label.grid(row=0, column=0, pady=(10, 5), padx=10, sticky='w')
        from_input.grid(row=1, column=0, pady=(20, 20), padx=(100, 0), sticky='w')
        to_label.grid(row=2, column=0, pady=5, padx=10, sticky='w')
        # from_label.grid(row=1, column=1, pady=10, padx=10, columnspan=2)
        recipients_tabs.grid(row=3, column=0, sticky='nsew', columnspan=2)
        nxt_button_input.grid(row=4, column=1, sticky='sw', pady=(0, 30))
        bck_button_input.grid(row=4, column=0, sticky='sw', pady=(0, 30))


class GmailPage_3(CTkFrame):

    def __init__(self, parent, controller):
        CTkFrame.__init__(self, parent, corner_radius=0, fg_color="transparent")
        # self.grid_columnconfigure(0, weight=1)
        # self.grid_rowconfigure(3, weight=1)

        abc_label = CTkLabel(self, text='A/B/C Testing', font=LARGE_FONT)
        abc_about_button = CTkButton(self, text='What is ABC Testing?',  command=lambda: controller.show_frame(GmailPage_3, 'Gmail'),
                                     width=100)

        abc_radbutton_frame = CTkFrame(self, fg_color="transparent")

        abc_radio_var = tkinter.IntVar(value=0)
        abc_sub_body_var = tkinter.IntVar(value=0)
        abc_b_c_var = tkinter.IntVar(value=0)

        abc_test_frame_label = CTkLabel(abc_radbutton_frame, text="Use A/B/C Testing?")
        abc_radio_button_no = CTkRadioButton(master=abc_radbutton_frame, text='No', variable=abc_radio_var, value=0)
        abc_radio_button_yes = CTkRadioButton(master=abc_radbutton_frame, text='Yes', variable=abc_radio_var, value=1)

        abc_sub_body_label = CTkLabel(abc_radbutton_frame, text="Vary the Subject or Body")
        abc_sub_body_button_no = CTkRadioButton(master=abc_radbutton_frame, text='Subject', variable=abc_sub_body_var, value=0)
        abc_sub_body_button_yes = CTkRadioButton(master=abc_radbutton_frame, text='Body', variable=abc_sub_body_var, value=1)

        abc_b_c_label = CTkLabel(abc_radbutton_frame, text="2 Variations(B) or 3 Variations (C)")
        abc_b_c_button_no = CTkRadioButton(master=abc_radbutton_frame, text='B', variable=abc_b_c_var, value=0)
        abc_b_c_button_yes = CTkRadioButton(master=abc_radbutton_frame, text='C', variable=abc_b_c_var, value=1)


        # inside group radframe griding
        abc_test_frame_label.grid(row=0, column=0, sticky='e', pady=25)
        abc_radio_button_no.grid(row=0, column=1, padx=(20, 0))
        abc_radio_button_yes.grid(row=0, column=2)

        abc_sub_body_label.grid(row=1, column=0, sticky='e', pady=25)
        abc_sub_body_button_no.grid(row=1, column=1, padx=(20, 0))
        abc_sub_body_button_yes.grid(row=1, column=2)

        abc_b_c_label.grid(row=2, column=0, sticky='e', pady=25)
        abc_b_c_button_no.grid(row=2, column=1, padx=(20, 0))
        abc_b_c_button_yes.grid(row=2, column=2)



        abc_label.grid(row=0, column=0, padx=50, pady=50)
        abc_about_button.grid(row=0, column=1, sticky='w')
        abc_radbutton_frame.grid(row=1, column=0)


class ABC_info(CTkFrame):

    def __init__(self, parent, controller):
        CTkFrame.__init__(self, parent, corner_radius=0, fg_color="transparent")
        # self.grid_columnconfigure(0, weight=1)
        # self.grid_rowconfigure(3, weight=1)

        self.textbox = customtkinter.CTkTextbox(self, width=250)
        self.textbox.grid(row=0, column=1, padx=(20, 0), pady=(20, 0), sticky="nsew")
        self.textbox.insert("0.0",
                            "CTkTextbox\n\n" + "Lorem ipsum dolor sit amet, consetetur sadipscing elitr, sed diam nonumy eirmod tempor invidunt ut labore et dolore magna aliquyam erat, sed diam voluptua.\n\n" * 20)


class OutlookPage(CTkFrame):

    def __init__(self, parent, controller):
        CTkFrame.__init__(self, parent, corner_radius=0, fg_color="transparent")
        self.grid_columnconfigure(0, weight=8)
        self.grid_columnconfigure(1, weight=1)

        label = CTkLabel(self, text='Outlook', font=LARGE_FONT, compound='center')

        email_input = CTkEntry(self, placeholder_text="Enter Outlook address", width=300)
        pass_input = CTkEntry(self, placeholder_text="Enter Outlook password", width=300)
        campaign_input = CTkEntry(self, placeholder_text="New Campaign Name", width=300)

        # Add to Settings window
        # sp3 = CTkLabel(self, text="")
        # ex_label = CTkLabel(self, text="Paste PATH to contacts Excel: ")
        # exel_input = CTkEntry(self, width=60)

        nxt_button_input = CTkButton(self, text='Next>',  # command=check_paths,
                                     width=100)

        label.grid(row=0, column=0, pady=10, padx=10, columnspan=2)
        email_input.grid(row=2, column=0, pady=(50, 30), padx=(135, 0))
        pass_input.grid(row=3, column=0, pady=50, padx=(135, 0))
        campaign_input.grid(row=4, column=0, pady=30, padx=(135, 0))
        nxt_button_input.grid(row=5, column=1, columnspan=2, sticky='sw', pady=70)


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
