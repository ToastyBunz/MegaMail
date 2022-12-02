# Fields
# User email
# Json (single line)
# excel (single line)
# Subject (single line)
# Body (Text box)
# Signature (Text Box, maybe multiple single lines)

# MVP todo
# subject box save input X
# body save input X
# warning pop up have number of emails X
# email loop works X
# body and subj into email send button sends X
# Some sort of completed confirmation (if not loading bar) X

# refresh token every new day login or every 24th token
# email column input
# HTML version of Warner email
# save as exe file
# Logo for exe
# Set Kill date for free trial

# level 2 todo
# attachements
# validate email (does destination exist?)
# Option to use name column
# loading bar
# HTML email
# click add signature
# signature
# 2 threads (A/B testing)
# Email statistics (opens and responses)
# combine fixed_path into spreadsheet_path_exists and json_path exists

# level 3 TODO
# chrome extension
# more than two strands


# make tk pretty again https://github.com/TomSchimansky/CustomTkinter

# Steps
# pick email column and names X
# get excel, clean X
# print new number X
# email subj X
# body (with formatting) X will examine more extensively later
# Allow for name to be replaced ... loc both name and email X
# loop email addresses - send X
# Add signature
# Wrap with Tkinter GUI
# Make TKInter pretty
# Loading bar
# Set a kill date for free trial

# working on
# when they confirm they are ready to send with final pop up it collects information and sends emails
# 181-183 and 203 - 204
# should go into 127


from tkinter import *
from tkinter import messagebox
import os

import pandas as pd

from DataMaid import contacts_processing
from Gmail_funcs import gmail_authenticate
from Gmail_funcs import megamail_send


# Request all access (permission to read/send/receive emails, manage the inbox, and more)
SCOPES = ['https://mail.google.com/']

# get the Gmail API service
# service = gmail_authenticate()

# example message
# send_message(service, receiving_email, 'Excel attchment testing', 'A body has a thumb',
#              ['E:/pythonProject/MegaMail/Emails/Testing_Tools/EmailTesting.xlsx'])


want_name = False


root = Tk()
mm_label = Label(root, text="Mega Mail by Nathan Burns", font='Helvetica 14', foreground='white', background="#34A2FE", width=60)
mm_label.grid(row=0, column=1, columnspan=2)


def fixed_path(path):
    if path[0] == '"':
        path = path[1:]
        path = path[:-1]
    else:
        pass
    return path.replace("\\", '/')


def path_exists(path):
    return os.path.exists(path)


# TODO combine fixed_path into spreadsheet_path_exists and json_path exists
def spredsheet_path_exists(path):
    testing_path = "S:\DevStuff\EmailTesting.xlsx"
    e = '.xlsx'
    c = '.csv'
    if path.endswith(e) or path.endswith(c) and os.path.exists(path):
        return 1
    else:
        messagebox.showerror("Missing Fild", 'This is not a valid Excel or CSV file')

def json_path_exists(path):
    testing_link = "C:/Users/natha/Downloads/dev_key2.json"
    j = '.json'
    if path.endswith(j) and os.path.exists(path):
        return 1
    else:
        messagebox.showerror("Missing Fild", 'This is not a valid json file')

# def popup(window):
#     response = messagebox.askyesno("Ready to send", "Are you ready to send X emails")
#     email_contacts = contacts_processing(fixed_excel_contacts)
#     service = gmail_authenticate(fixed_json_key)
#     if response:
#         Label(window, text='You clicked YES!').grid(row=8, column=1)
#         MegaMail_Send(service, email_contacts, subjt.get(), body.get(1.0, END))
#     else:
#         Label(window, text='You clicked No!').grid(row=8, column=1)


def check_paths():
    global personal_email
    global fixed_json_key
    global fixed_exel_contacts

    # get inputs
    personal_email = email_input.get()
    json_key = jsan_input.get()
    exel_contacts = exel_input.get()

    # files with fixed paths
    fixed_json_key = fixed_path(json_key)
    fixed_exel_contacts = fixed_path(exel_contacts)

    # if not path_exists(fixed_json_key):
    if not json_path_exists(fixed_json_key):
        pass
    elif not spredsheet_path_exists(fixed_exel_contacts):
        pass
    else:
        top = email_window() # subjt, body, signature
        # print(fixed_exel_contacts)

    return

def email_window():
    top = Toplevel()

    # def getting_box():
    #     my_label = Label(top, text='')
    #     my_label.grid(row=9, column=1)
    #     body_stuff = body.get(1.0, END)
    #     my_label.config(text=body_stuff)

    def popup(window):
        contacts_df = contacts_processing(fixed_exel_contacts)
        num_emails = len(contacts_df['email'])
        response = messagebox.askyesno("Ready to send", "Are you ready to send {} emails?".format(num_emails))
        if response:
            # print(contacts_df)
            service = gmail_authenticate(fixed_json_key)
            megamail_send(service, contacts_df, personal_email, subjt.get(), body.get(1.0, END))
            Label(window, text='All Emails Sent!').grid(row=8, column=1)
        else:
            Label(window, text='You clicked No!').grid(row=8, column=1)

    # TODO branches for auto name input and generic emails !!! THIS IS LAST !!!
    subjt = Entry(top, width=75, font=("calibri", 14))
    body = Text(top, width=75, font=("Calibri", 14))
    signature_button = Button(top, text='Click to add signature?')  # if yes, else no
    signature_name = Entry(top, width=40)
    signature_number = Entry(top, width=40)
    signature_email = Entry(top, width=40)
    send_button = Button(top, text='Send', foreground='white', background="#34A2FE", width=15, command=lambda: popup(top))
    # get_text_button = Button(top, text='text box', command=getting_box)

    subjt.grid(row=1, column=1)
    body.grid(row=2, column=1)
    signature_button.grid(row=3, column=1)
    signature_name.grid(row=4, column=1)
    signature_number.grid(row=5, column=1)
    signature_email.grid(row=6, column=1)
    send_button.grid(row=6, column=2)
    # get_text_button.grid(row=7, column=1)

    subjt.insert(0, "Email Subject Here")
    body.insert(INSERT, "Email Body Here")
    signature_name.insert(0, "Enter name: John Doe")
    signature_number.insert(0, "Enter number: Office: (999) 888 - 777")
    signature_email.insert(0, "Enter email. J.Doe@gmail.com")

    # contacts_df = contacts_processing(fixed_excel_contacts)
    # service = gmail_authenticate(fixed_json_key)
    # MegaMail_Send(service, contacts_df, subjt.get(), body.get(1.0, END))


    return top

# TODO white_space = Label(root, text="") Convert the white lines to this if you have time later

sp1 = Label(root, text="")
e_label = Label(root, text="Enter your gmail: ")
email_input = Entry(root, width=60)

sp2 = Label(root, text="")
j_label = Label(root, text="Paste PATH to json email key: ")
jsan_input = Entry(root, width=60)

sp3 = Label(root, text="")
ex_label = Label(root, text="Paste PATH to contacts Excel: ")
exel_input = Entry(root, width=60)

sp4 = Label(root, text="")
nxt_button_input = Button(root, text='Next>', command=check_paths, foreground='white', background="#34A2FE", width=15)

# email_email, _, _ = check_paths()
# _, email_json, _ = check_paths()
# _, _, email_excel = check_paths()


sp1.grid(row=1, column=0)
e_label.grid(row=2, column=1)
email_input.grid(row=2, column=2)

sp2.grid(row=3, column=0)
j_label.grid(row=4, column=1)
jsan_input.grid(row=4, column=2)

sp3.grid(row=5, column=0)
ex_label.grid(row=6, column=1)
exel_input.grid(row=6, column=2)

sp4.grid(row=7, column=0)
nxt_button_input.grid(row=8, column=2)


email_input.insert(0, "mymail@gmail.com")
jsan_input.insert(0, "PATH")
exel_input.insert(0, "PATH")

root.mainloop()

