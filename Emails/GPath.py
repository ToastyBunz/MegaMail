import tkinter
# from tkinter import *
from tkinter import ttk
import customtkinter
from customtkinter import *

LARGE_FONT = ("Verdana", 20)


class GmailPage(CTkFrame):

    def __init__(self, parent, controller):
        CTkFrame.__init__(self, parent, corner_radius=0, fg_color="transparent")
        self.grid_columnconfigure(0, weight=8)
        self.grid_columnconfigure(1, weight=1)

        window_label_frame = CTkFrame(self, fg_color="transparent")
        window_label_frame.pack()

        label = CTkLabel(window_label_frame, text='Gmail', font=LARGE_FONT, compound='center')
        label.grid(row=0, column=0, pady=(20, 60), padx=10, columnspan=3)

        gmail_inputs_frame = CTkFrame(self, fg_color="transparent")
        gmail_inputs_frame.pack()

        # input boxes
        email_input = CTkEntry(gmail_inputs_frame, placeholder_text="Enter gmail address", width=300)
        pass_input = CTkEntry(gmail_inputs_frame, placeholder_text="Paste PATH to json gmail key", width=300)
        campaign_input = CTkEntry(gmail_inputs_frame, placeholder_text="New Campaign Name", width=300)

        # Add to Settings window
        # sp3 = CTkLabel(self, text="")
        # ex_label = CTkLabel(self, text="Paste PATH to contacts Excel: ")
        # exel_input = CTkEntry(self, width=60)

        label.grid(row=0, column=0, pady=10, padx=10, columnspan=2)
        email_input.grid(row=2, column=0, pady=(50, 30))
        pass_input.grid(row=3, column=0, pady=50)
        campaign_input.grid(row=4, column=0, pady=30)


        # Same forward and backward buttons
        nxtbck_frame = CTkFrame(self, fg_color="transparent")
        nxtbck_frame.pack(side=BOTTOM, anchor='e')

        nxt_button_input = CTkButton(nxtbck_frame, text='Next>', command=lambda: controller.show_frame(GmailPage_2, 'Gmail'),
                                     width=100)

        nxt_button_input.grid(row=2, column=2, sticky='se', pady=10, padx=(0, 0))


class GmailPage_2(CTkFrame):

    def __init__(self, parent, controller):
        CTkFrame.__init__(self, parent, corner_radius=0, fg_color="transparent")
        # self.grid_columnconfigure(0, weight=1)
        # self.grid_columnconfigure(1, weight=1)
        # self.grid_rowconfigure(3, weight=1)

        label_frame = CTkFrame(self, fg_color="transparent")
        label_frame.grid_columnconfigure(0, weight=1)
        label_frame.grid_columnconfigure(1, weight=8)
        label_frame.pack(side=TOP, anchor='w')

        from_label = CTkLabel(label_frame, text='From: ', font=LARGE_FONT, compound='center')
        from_input = CTkEntry(label_frame, placeholder_text="E.G. John Doe or MyCompany.net", width=400)
        to_label = CTkLabel(label_frame, text='To: ', font=LARGE_FONT, compound='center')

        from_label.grid(row=0, column=0, pady=20, padx=(85, 0))
        from_input.grid(row=0, column=1, pady=20, padx=(95, 0))
        to_label.grid(row=1, column=0, pady=20, padx=(65, 0))



        # Tab Frame
        recipients_tabs = CTkTabview(self, width=750, height=400)
        recipients_tabs.add(" All  ")
        recipients_tabs.add(" Groups")
        recipients_tabs.add(" New Group  ")

        # Filling the "All" tab
        all_column_label = CTkLabel(recipients_tabs.tab(" All  "), text="Which column holds emails?", compound='center')
        all_column_dropdown = CTkOptionMenu(recipients_tabs.tab(" All  "), dynamic_resizing=False, width=250,
                                            values=["Value 1", "Value 2", "Value Long Long Long"])

        # Create a frame for Radio Button and grid them
        all_radbutton_frame = CTkFrame(recipients_tabs.tab(" All  "), fg_color="transparent")
        all_radio_var = tkinter.IntVar(value=0)
        all_radbutton_frame_label = CTkLabel(all_radbutton_frame, text="Would you like to greet recipients by name?")
        all_radio_button_no = CTkRadioButton(master=all_radbutton_frame, text='No', variable=all_radio_var, value=0)
        all_radio_button_yes = CTkRadioButton(master=all_radbutton_frame, text='Yes', variable=all_radio_var, value=1)

        # Grids for Rad button Frame
        all_radbutton_frame_label.grid(row=0, column=0, columnspan=2, padx=(75, 0))
        all_radio_button_no.grid(row=1, column=0)
        all_radio_button_yes.grid(row=1, column=2)

        # back to outside radbutton frame
        all_personalize_label = CTkLabel(recipients_tabs.tab(" All  "), text="Which column holds names?")
        all_personalize_dropdown = CTkOptionMenu(recipients_tabs.tab(" All  "), dynamic_resizing=False, width=250,
                                            values=["Value 1", "Value 2", "Value Long Long Long"])

        # filling the "All" tab
        all_column_label.pack(pady=(30, 0))
        all_column_dropdown.pack(pady=(0,30))
        all_radbutton_frame.pack(pady=(30,0))
        all_personalize_label.pack(pady=(10,0))
        all_personalize_dropdown.pack()


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
        # group_group_label.grid(row=0, column=0)
        # group_column_label.grid(row=0, column=1)
        # group_group_dropdown.grid(row=1, column=0)
        # group_column_dropdown.grid(row=1, column=1)
        # group_radbutton_frame.grid(row=2, column=0, padx=20, pady=(20, 0), sticky='nsew')
        # group_personalize_label.grid(row=3, column=0)
        # group_personalize_dropdown.grid(row=4, column=0)

        group_group_label.pack(pady=(30,0))
        group_group_dropdown.pack()
        group_column_label.pack(pady=(30,0))
        group_column_dropdown.pack()
        group_radbutton_frame.pack(pady=(30,0))
        group_personalize_label.pack(pady=(15,0))
        group_personalize_dropdown.pack()


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
        ngroup_tree_buttons_frame = CTkFrame(recipients_tabs.tab(" New Group  "), fg_color="transparent")



        ngroup_all_button = CTkButton(ngroup_tree_buttons_frame, text='Add contacts from All')
        ngroup_groups_button = CTkButton(ngroup_tree_buttons_frame, text='Import previous group')
        ngroup_import_button = CTkButton(ngroup_tree_buttons_frame, text='Import new contacts')

        # filling ngroup_tree_buttons_frame
        ngroup_all_button.grid(row=0, column=0, padx=(0, 20))
        ngroup_groups_button.grid(row=0, column=1, padx=(0, 20))
        ngroup_import_button.grid(row=0, column=2)

        # Filling the "New Group" tab
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
        ngroup_radbutton_frame_label.grid(row=0, column=0, columnspan=3)
        ngroup_radio_button_no.grid(row=1, column=0)
        ngroup_radio_button_yes.grid(row=1, column=2)

        # back to outside radbutton frame
        ngroup_personalize_label = CTkLabel(recipients_tabs.tab(" New Group  "), text="Which column holds names?")
        ngroup_personalize_dropdown = CTkOptionMenu(recipients_tabs.tab(" New Group  "), dynamic_resizing=False, width=250,
                                                 values=["Value 1", "Value 2", "Value Long Long Long"])


        # Gridding New Group Tab
        ngroup_name_entry.pack(pady=(30, 10))
        ngroup_tree.pack(pady=(0, 10))
        ngroup_tree_buttons_frame.pack(pady=(0, 10))
        ngroup_column_label.pack()
        ngroup_column_dropdown.pack(pady=(0, 20))
        ngroup_radbutton_frame.pack(pady=(0, 20))
        ngroup_personalize_label.pack()
        ngroup_personalize_dropdown.pack()



        recipients_tabs.pack()

        # Same forward and backward buttons
        nxtbck_frame = CTkFrame(self, fg_color="transparent")
        nxtbck_frame.pack(side=BOTTOM)

        bck_button_input = CTkButton(nxtbck_frame, text='<Back', command=lambda: controller.show_frame(GmailPage, 'Gmail'),
                                     width=100)

        nxt_button_input = CTkButton(nxtbck_frame, text='Next>', command=lambda: controller.show_frame(GmailPage_3, 'Gmail'),
                                     width=100)

        bck_button_input.grid(row=2, column=0, sticky='sw', pady=10, padx=(0, 720))
        nxt_button_input.grid(row=2, column=2, sticky='se', pady=10, padx=(0, 0))


class GmailPage_3(CTkFrame):

    def __init__(self, parent, controller):
        CTkFrame.__init__(self, parent, corner_radius=0, fg_color="transparent")
        # self.grid_columnconfigure(0, weight=1)
        # self.grid_rowconfigure(3, weight=1)

        abc_frame = CTkFrame(self, fg_color="transparent")

        abc_label = CTkLabel(abc_frame, text='A/B/C Testing', font=LARGE_FONT)
        abc_about_button = CTkButton(abc_frame, text='What is ABC Testing?',  command=lambda: controller.show_frame(ABC_info, 'Gmail'),
                                     width=100)

        # Filling abc_frame
        abc_label.grid(row=0, column=0, padx=(0, 30))
        abc_about_button.grid(row=0, column=1)

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

        abc_frame.pack(pady=(30, 40))
        abc_radbutton_frame.pack()

        # Same forward and backward buttons
        nxtbck_frame = CTkFrame(self, fg_color="transparent")
        nxtbck_frame.pack(side=BOTTOM)

        bck_button_input = CTkButton(nxtbck_frame, text='<Back', command=lambda: controller.show_frame(GmailPage_2, 'Gmail'),
                                     width=100)

        nxt_button_input = CTkButton(nxtbck_frame, text='Next>', command=lambda: controller.show_frame(GmailPage_4, 'Gmail'),
                                     width=100)

        bck_button_input.grid(row=2, column=0, sticky='sw', pady=10, padx=(0, 720))
        nxt_button_input.grid(row=2, column=2, sticky='se', pady=10, padx=(0, 0))


class ABC_info(CTkFrame):
    def __init__(self, parent, controller):
        CTkFrame.__init__(self, parent, corner_radius=0, fg_color="transparent")
        self.grid_columnconfigure(0, weight=1)
        self.grid_rowconfigure(0, weight=1)

        self.textbox = customtkinter.CTkTextbox(self, width=250)
        self.textbox.grid(row=0, column=0, padx=(20, 0), pady=(20, 0), sticky="nsew")
        self.textbox.insert("0.0", text="What is A/B Testing?:\n\n"
                                        "A/B Testing, which can also be called splilt testing or bucket testing, is a"
                                        " method of camparing two variations of an email subject or email body and\n"
                                        "determining which preforms better. The Sender (You) creates two versions of"
                                        " the same email, then the program takes the mailing list and randomly divides"
                                        "\nthe recipiants into two groups, Group 1 receives version 1 and Group 2"
                                        " receives version 2. After the email is sent it tracks the Open, Click"
                                        " Through, and\nUnsubscibe Rates to determine the wininning version.\n\nIn"
                                        " A/B/C Testing, tests a third variation and randomly splits the mailing list"
                                        " into thirds, otherwise it is identical to A/B Testing ")

        bck_button_input = CTkButton(self, text='<Back', command=lambda: controller.show_frame(GmailPage_3, 'Gmail'),
                                     width=100)

        bck_button_input.grid(row=4, column=0, sticky='sw', pady=(0, 30))



class GmailPage_4(CTkFrame):

    def __init__(self, parent, controller):
        CTkFrame.__init__(self, parent, corner_radius=0, fg_color="transparent")
        # self.grid_columnconfigure(0, weight=1)
        # self.grid_columnconfigure(1, weight=8)
        # self.grid_columnconfigure(2, weight=1)

        label = CTkLabel(self, text='Subjects', font=LARGE_FONT, compound='center')
        label.pack(pady=10, padx=10)

        entry_frame = CTkFrame(self, fg_color="transparent")
        entry_frame.pack(pady=(100, 0))

        # input boxes
        a_label = CTkLabel(entry_frame, text='Email A')
        subject_a_entry = CTkEntry(entry_frame, placeholder_text="Subject A", width=280)

        b_label = CTkLabel(entry_frame, text='Email B')
        subject_ab_entry = CTkEntry(entry_frame, placeholder_text="Subject B", width=280)

        c_label = CTkLabel(entry_frame, text='Email C')
        subject_c_entry = CTkEntry(entry_frame, placeholder_text="Subject C", width=280)

        # gridding elements for frame
        a_label.grid(column=0, row=0)
        subject_a_entry.grid(column=0, row=1, padx=(0, 35))

        b_label.grid(column=1, row=0)
        subject_ab_entry.grid(column=1, row=1, padx=(0, 35))

        c_label.grid(column=2, row=0)
        subject_c_entry.grid(column=2, row=1)

        # Same forward and backward buttons
        nxtbck_frame = CTkFrame(self, fg_color="transparent")
        nxtbck_frame.pack(side=BOTTOM)

        bck_button_input = CTkButton(nxtbck_frame, text='<Back', command=lambda: controller.show_frame(GmailPage_3, 'Gmail'),
                                     width=100)

        nxt_button_input = CTkButton(nxtbck_frame, text='Next>', command=lambda: controller.show_frame(GmailPage_5, 'Gmail'),
                                     width=100)

        bck_button_input.grid(row=2, column=0, sticky='sw', pady=10, padx=(0, 720))
        nxt_button_input.grid(row=2, column=2, sticky='se', pady=10, padx=(0, 0))


class GmailPage_5(CTkFrame):

    def __init__(self, parent, controller):
        CTkFrame.__init__(self, parent, corner_radius=0, fg_color="transparent")
        # self.grid_columnconfigure(0, weight=1)
        # self.grid_columnconfigure(1, weight=8)
        # self.grid_columnconfigure(2, weight=1)

        label = CTkLabel(self, text='Email Bodies', font=LARGE_FONT, compound='center')
        label.pack(pady=10, padx=10)

        textbox_frame = CTkFrame(self, fg_color="transparent")
        textbox_frame.pack()

        # input boxes
        a_label = CTkLabel(textbox_frame, text='Body A')
        body_a_box = CTkTextbox(textbox_frame, width=905, height=375)
        button_frame =CTkFrame(textbox_frame, fg_color='transparent')

        import_button_box = CTkButton(button_frame, text='Import Template')
        new_button_box = CTkButton(button_frame, text='New Template')

        #filling button box
        import_button_box.grid(row=0, column=0, padx=(0, 20))
        new_button_box.grid(row=0, column=1, padx=(20, 0))

        # gridding elements for frame
        a_label.pack()
        body_a_box.pack()
        button_frame.pack(pady=(10, 0))


        # Same forward and backward buttons
        nxtbck_frame = CTkFrame(self, fg_color="transparent")
        nxtbck_frame.pack(side=BOTTOM)

        bck_button_input = CTkButton(nxtbck_frame, text='<Back', command=lambda: controller.show_frame(GmailPage_4, 'Gmail'),
                                     width=100)

        nxt_button_input = CTkButton(nxtbck_frame, text='Next>', command=lambda: controller.show_frame(GmailPage_6, 'Gmail'),
                                     width=100)

        bck_button_input.grid(row=2, column=0, sticky='sw', pady=10, padx=(0, 720))
        nxt_button_input.grid(row=2, column=2, sticky='se', pady=10, padx=(0, 0))


class GmailPage_6(CTkFrame):

    def __init__(self, parent, controller):
        CTkFrame.__init__(self, parent, corner_radius=0, fg_color="transparent")
        # self.grid_columnconfigure(0, weight=1)
        # self.grid_columnconfigure(1, weight=8)
        # self.grid_columnconfigure(2, weight=1)

        label = CTkLabel(self, text='Email Bodies', font=LARGE_FONT, compound='center')
        label.pack(pady=10, padx=10)

        textbox_frame = CTkFrame(self, fg_color="transparent")
        textbox_frame.pack()

        # input boxes
        b_label = CTkLabel(textbox_frame, text='Body B')
        body_b_box = CTkTextbox(textbox_frame, width=905, height=375)
        button_frame =CTkFrame(textbox_frame, fg_color='transparent')

        import_button_box = CTkButton(button_frame, text='Import Template')
        new_button_box = CTkButton(button_frame, text='New Template')

        #filling button box
        import_button_box.grid(row=0, column=0, padx=(0, 20))
        new_button_box.grid(row=0, column=1, padx=(20, 0))

        # gridding elements for frame
        b_label.pack()
        body_b_box.pack()
        button_frame.pack(pady=(10, 0))


        # Same forward and backward buttons
        nxtbck_frame = CTkFrame(self, fg_color="transparent")
        nxtbck_frame.pack(side=BOTTOM)

        bck_button_input = CTkButton(nxtbck_frame, text='<Back', command=lambda: controller.show_frame(GmailPage_5, 'Gmail'),
                                     width=100)

        nxt_button_input = CTkButton(nxtbck_frame, text='Next>', command=lambda: controller.show_frame(GmailPage_7, 'Gmail'),
                                     width=100)

        bck_button_input.grid(row=2, column=0, sticky='sw', pady=10, padx=(0, 720))
        nxt_button_input.grid(row=2, column=2, sticky='se', pady=10, padx=(0, 0))


class GmailPage_7(CTkFrame):

    def __init__(self, parent, controller):
        CTkFrame.__init__(self, parent, corner_radius=0, fg_color="transparent")
        # self.grid_columnconfigure(0, weight=1)
        # self.grid_columnconfigure(1, weight=8)
        # self.grid_columnconfigure(2, weight=1)

        label = CTkLabel(self, text='Email Bodies', font=LARGE_FONT, compound='center')
        label.pack(pady=10, padx=10)

        textbox_frame = CTkFrame(self, fg_color="transparent")
        textbox_frame.pack()

        # input boxes
        c_label = CTkLabel(textbox_frame, text='Body C')
        body_c_box = CTkTextbox(textbox_frame, width=905, height=375)
        button_frame =CTkFrame(textbox_frame, fg_color='transparent')

        import_button_box = CTkButton(button_frame, text='Import Template')
        new_button_box = CTkButton(button_frame, text='New Template')

        #filling button box
        import_button_box.grid(row=0, column=0, padx=(0, 20))
        new_button_box.grid(row=0, column=1, padx=(20, 0))

        # gridding elements for frame
        c_label.pack()
        body_c_box.pack()
        button_frame.pack(pady=(10, 0))


        # Same forward and backward buttons
        nxtbck_frame = CTkFrame(self, fg_color="transparent")
        nxtbck_frame.pack(side=BOTTOM)

        bck_button_input = CTkButton(nxtbck_frame, text='<Back', command=lambda: controller.show_frame(GmailPage_6, 'Gmail'),
                                     width=100)

        nxt_button_input = CTkButton(nxtbck_frame, text='Next>', command=lambda: controller.show_frame(GmailPage_Sending, 'Gmail'),
                                     width=100)

        bck_button_input.grid(row=2, column=0, sticky='sw', pady=10, padx=(0, 720))
        nxt_button_input.grid(row=2, column=2, sticky='se', pady=10, padx=(0, 0))


class GmailPage_Sending(CTkFrame):
    # Future update allow users to change settings and names in the final page

    def __init__(self, parent, controller):
        CTkFrame.__init__(self, parent, corner_radius=0, fg_color="transparent")
        # self.grid_columnconfigure(0, weight=1)
        # self.grid_columnconfigure(1, weight=8)
        # self.grid_columnconfigure(2, weight=1)

        window_label_frame = CTkFrame(self, fg_color="transparent")
        window_label_frame.pack()

        label = CTkLabel(window_label_frame, text='Sending Emails', font=LARGE_FONT, compound='center')
        label.grid(row=0, column=0, pady=(20, 60), padx=10, columnspan=3)

        campeign_settings_frame = CTkFrame(self, fg_color="transparent")
        campeign_settings_frame.pack()

        # input boxes
        name_label = CTkLabel(campeign_settings_frame, text='Name:', font=LARGE_FONT)
        email_label = CTkLabel(campeign_settings_frame, text='Email: ', font=LARGE_FONT)
        campaign_label = CTkLabel(campeign_settings_frame, text='Campaign name:', font=LARGE_FONT)
        ab_label = CTkLabel(campeign_settings_frame, text='A/B/C Testing:', font=LARGE_FONT)
        sb_label = CTkLabel(campeign_settings_frame, text='Subj/Body: ', font=LARGE_FONT)

        name_actual_label = CTkLabel(campeign_settings_frame, text='ZZZ BBB')
        email_actual_label = CTkLabel(campeign_settings_frame, text='ZZZ@boob.com')
        campaign_actual_label = CTkLabel(campeign_settings_frame, text='Massive')
        yn_label = CTkLabel(campeign_settings_frame, text='Yes (PH)')
        sb_label_actual = CTkLabel(campeign_settings_frame, text='Subj (PH)')

        # gridding elements for frame
        name_label.grid(row=0, column=0, padx=(0, 20))
        email_label.grid(row=0, column=1, padx=(0, 20))
        campaign_label.grid(row=0, column=2, padx=(0, 20))
        ab_label.grid(row=0, column=4, padx=(0, 20))
        sb_label.grid(row=0, column=5)

        name_actual_label.grid(row=1, column=0, padx=(0, 20))
        email_actual_label.grid(row=1, column=1, padx=(0, 20))
        campaign_actual_label.grid(row=1, column=2, padx=(0, 20))
        yn_label.grid(row=1, column=4, padx=(0, 20))
        sb_label_actual.grid(row=1, column=5)

        # Readey to send Frame
        ready_send_frame = CTkFrame(self, fg_color="transparent")
        ready_send_frame.pack(pady=(50, 10))
        send_label = CTkLabel(ready_send_frame, text='Ready to send 3000 emails?')
        send_yes_button = CTkButton(ready_send_frame, text='Yes')
        send_no_button = CTkButton(ready_send_frame, text='No')

        send_label.grid(row=0, column=0, columnspan=2)
        send_yes_button.grid(row=1, column=0)
        send_no_button.grid(row=1, column=1)

        # Progress window
        sending_progress_frame = CTkFrame(self, fg_color="transparent")
        sending_progress_frame.pack()

        progressbar = CTkProgressBar(sending_progress_frame, width=600)
        progressbar.grid(row=0, column=0, padx=20, pady=(60, 0))
        progress_tally = CTkLabel(sending_progress_frame, text='300 of 3000 sent')
        progress_tally.grid(row=1, column=0, padx=20, pady=(10, 0))
        progress_time = CTkLabel(sending_progress_frame, text='Approx 1hr 20min left')
        progress_time.grid(row=2, column=0, padx=20, pady=10)


        # Same forward and backward buttons
        nxtbck_frame = CTkFrame(self, fg_color="transparent")
        nxtbck_frame.pack(side=BOTTOM)

        bck_button_input = CTkButton(nxtbck_frame, text='<Back', command=lambda: controller.show_frame(GmailPage_6, 'Gmail'),
                                     width=100)

        nxt_button_input = CTkButton(nxtbck_frame, text='Done', command=lambda: controller.show_frame(GmailPage, 'Gmail'),
                                     width=100)

        bck_button_input.grid(row=2, column=0, sticky='sw', pady=10, padx=(0, 720))
        nxt_button_input.grid(row=2, column=2, sticky='se', pady=10, padx=(0, 0))
