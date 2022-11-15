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
# authenticate and send
# warning pop up have number of emails
# body and subj into email send button sends
# authenticate and send
# Test loop
# save as exe file
# expire dec 15

# level 2 todo
# Option to use name column
# loading bar
# HTML email
# click add signature
# signature
# combine fixed_path into spreadsheet_path_exists and json_path exists



# from functools import partial
from tkinter import *
from tkinter import messagebox
import os

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

import os
import pickle
from googleapiclient.discovery import build
from google_auth_oauthlib.flow import InstalledAppFlow
from google.auth.transport.requests import Request
# for encoding/decoding messages in base 64

from base64 import urlsafe_b64decode, urlsafe_b64encode
# for dealing with attachement MIME types
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.image import MIMEImage
from email.mime.audio import MIMEAudio
from email.mime.base import MIMEBase
from mimetypes import guess_type as guess_mime_type
# from PW import dev_email

import pandas as pd
# import xlr
import tkinter as tk

# window = tk.Tk()
# theLabel = tk.Label(window, text='Mega Mail', foreground='white', background='black')
# theLabel.pack()
# window.mainloop()

outreach_file = "E:/EmailTesting.xlsx"


# email = 'email'
# name = 'name'

class MyError(Exception):
    def __int__(self, message):
        self.message = message


unkown_file = MyError('Unknown filetype, please enter CSV or Excel')

def contacts_processing():
    if '.xlsx' in outreach_file:
        df = pd.DataFrame(pd.read_excel(outreach_file))
    elif '.csv' in outreach_file:
        df = pd.DataFrame(pd.read_csv(outreach_file))
    else:
        raise unkown_file

    df['email'] = df['email'].astype('string')

    df = df.dropna(axis=0, subset=['email'])
    df = df.fillna(0, axis=0)
    df = df.drop_duplicates(subset='email')
    df = df.reset_index()
    del df['index']
    return df

# Request all access (permission to read/send/receive emails, manage the inbox, and more)
SCOPES = ['https://mail.google.com/']


def gmail_authenticate(json_file):
    creds = None
    # the file token.pickle stores the user's access and refresh tokens, and is
    # created automatically when the authorization flow completes for the first time
    if os.path.exists("token.pickle"):
        with open("token.pickle", "rb") as token:
            creds = pickle.load(token)
            print('this is token', creds)
    # if there are no (valid) credentials availablle, let the user log in.
    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())
        else:
            flow = InstalledAppFlow.from_client_secrets_file(json_file, SCOPES)
            creds = flow.run_local_server(port=0)
        # save the credentials for the next run
        with open("token.pickle", "wb") as token:
            pickle.dump(creds, token)
    return build('gmail', 'v1', credentials=creds)


# get the Gmail API service
service = gmail_authenticate()


# Adds the attachment with the given filename to the given message
def add_attachment(message, filename):
    content_type, encoding = guess_mime_type(filename)
    if content_type is None or encoding is not None:
        content_type = 'application/octet-stream'
    main_type, sub_type = content_type.split('/', 1)
    if main_type == 'text':
        fp = open(filename, 'rb')
        msg = MIMEText(fp.read().decode(), _subtype=sub_type)
        fp.close()
    elif main_type == 'image':
        fp = open(filename, 'rb')
        msg = MIMEImage(fp.read(), _subtype=sub_type)
        fp.close()
    elif main_type == 'audio':
        fp = open(filename, 'rb')
        msg = MIMEAudio(fp.read(), _subtype=sub_type)
        fp.close()
    else:
        fp = open(filename, 'rb')
        msg = MIMEBase(main_type, sub_type)
        msg.set_payload(fp.read())
        fp.close()
    filename = os.path.basename(filename)
    msg.add_header('Content-Disposition', 'attachment', filename=filename)
    message.attach(msg)


def build_message(email, destination, obj, body, attachments=[]):
    if not attachments:  # no attachments given
        message = MIMEText(body)
        message['to'] = destination
        message['from'] = email
        message['subject'] = obj
    else:
        message = MIMEMultipart()
        message['to'] = destination
        message['from'] = email
        message['subject'] = obj
        message.attach(MIMEText(body))
        for filename in attachments:
            add_attachment(message, filename)
    return {'raw': urlsafe_b64encode(message.as_bytes()).decode()}


def send_message(service, destination, obj, body, attachments=[]):
    return service.users().messages().send(
        userId="me",
        body=build_message(destination, obj, body, attachments)
    ).execute()


# receiving_email = 'devburns22@gmail.com'

# example message
# send_message(service, "destination@domain.com", "This is a subject",
#             "This is the body of the email", ["test.txt", "anyfile.png"])

# send_message(service, receiving_email, 'Excel attchment testing', 'A body has a thumb',
#              ['E:/pythonProject/MegaMail/Emails/Testing_Tools/EmailTesting.xlsx'])

want_name = True

def MegaMail_Send(df):
    for i in range(len(df)):
        email = df.loc[i, 'email']
        name = df.loc[i, 'name']
        email_sbj_name = 'Hello Mr.{}'.format(name)
        email_body_name = 'Hello Mr.{} would you like to user our services'.format(name)
        email_sbj_noname = 'Greetings'
        email_body_noname = 'hello frick you, would you like to use our services'

        if name == 0 or want_name is False:
            send_message(service, email, email_sbj_noname, email_body_noname)
        else:
            send_message(service, email, email_sbj_name, email_body_name)

# MegaMail_Send()
print('all done')


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
    testing_link = "C:/Users/natha/Downloads/dev_key.json"
    j = '.json'
    if path.endswith(j) and os.path.exists(path):
        return 1
    else:
        messagebox.showerror("Missing Fild", 'This is not a valid json file')

def popup(window):
    response = messagebox.askyesno("Ready to send", "Are you ready to send X emails")
    if response:
        Label(window, text='You clicked YES!').grid(row=8, column=1)
    else:
        Label(window, text='You clicked No!').grid(row=8, column=1)




def email_window():
    top = Toplevel()

    def getting_box():
        my_label = Label(top, text='')
        my_label.grid(row=9, column=1)
        my_label.config(text=body.get(1.0, END))


    # TODO branches for auto name input and generic emails !!! THIS IS LAST !!!
    subjt = Entry(top, width=75)
    body = Text(top, width=75, font=("Helvetica", 12))
    signature_button = Button(top, text='Click to add signature?')  # if yes, else no
    signature_name = Entry(top, width=40)
    signature_number = Entry(top, width=40)
    signature_email = Entry(top, width=40)
    send_button = Button(top, text='Are you Ready to send?', command=lambda: popup(top))
    get_text_button = Button(top, text='text box', command=getting_box)

    subjt.grid(row=1, column=1)
    body.grid(row=2, column=1)
    signature_button.grid(row=3, column=1)
    signature_name.grid(row=4, column=1)
    signature_number.grid(row=5, column=1)
    signature_email.grid(row=6, column=1)
    send_button.grid(row=7, column=1)
    get_text_button.grid(row=8, column=1)

    subjt.insert(0, "Email Subject Here")
    body.insert(INSERT, "Email Body Here")
    signature_name.insert(0, "Enter name: John Doe")
    signature_number.insert(0, "Enter number: Office (999) 888 - 777")

    MegaMail_Send()

    subjt_string = ''
    email_string = ''
    signature_string = ''

    return top


def check_paths():
    personal_email = email_input.get()
    json_key = jsan_input.get()
    exel_contacts = exel_input.get()
    fixed_json_key = fixed_path(json_key)
    fixed_exel_contacts = fixed_path(exel_contacts)
    # if not path_exists(fixed_json_key):
    if not path_exists(fixed_json_key):  # TODO Switch back
        pass
    elif not path_exists(fixed_exel_contacts):  # TODO Switch back
        pass
    else:
        top = email_window() # subjt, body, signature

    return personal_email, fixed_json_key, fixed_exel_contacts, top


# def popup():
#     response = messagebox.askyesno("Ready to send", "Are you ready to send X emails")
#     if response:
#         Label(top, text='You clicked YES!').pack()
#     else:
#         Label(top, text='You clicked No!').pack()

# white_space = Label(root, text="") Convert the white lines to this if you have time later


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



# subjt = Entry(top, width=75)
# body = Text(top, width=75)
# signature_button = Button(top, text='Click to add signature?')  # if yes, else no
# signature_name = Entry(top, width=40)
# signature_number = Entry(top, width=40)
# signature_email = Entry(top, width=40)
# send_button = Button(top, text='Are you Ready to send?', command=popup)
#
#
# subjt.grid(row=4, column=1)
# body.grid(row=5, column=1)
# signature_button.grid(row=6, column=1)
# signature_name.grid(row=7, column=1)
# signature_number.grid(row=8, column=1)
# signature_email.grid(row=9, column=1)
# send_button.grid(row=10, column=1)
#
# subjt.insert(0, "Email Subject Here")
# body.insert(INSERT, "Email Body Here")
# signature_name.insert(0, "Enter name: John Doe")
# signature_number.insert(0, "Enter number: Office (999) 888 - 777")
# signature_name.insert(0, email.get())

root.mainloop()