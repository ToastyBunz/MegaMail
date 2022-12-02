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
import os

from PW import dev_email

import pandas as pd

# Request all access (permission to read/send/receive emails, manage the inbox, and more)
SCOPES = ['https://mail.google.com/']


def gmail_authenticate(json_file):
    creds = None
    # the file token.pickle stores the user's access and refresh tokens, and is
    # created automatically when the authorization flow completes for the first time
    if os.path.exists("token.pickle"):
        # TODO add newday validation
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
# service = gmail_authenticate()


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


def send_message(service, email, destination, obj, body, attachments=[]):
    return service.users().messages().send(
        userId="me",
        body=build_message(email, destination, obj, body, attachments)
    ).execute()


# receiving_email = 'devburns22@gmail.com'

# example message
# send_message(service, "destination@domain.com", "This is a subject",
#             "This is the body of the email", ["test.txt", "anyfile.png"])

# send_message(service, receiving_email, 'Excel attchment testing', 'A body has a thumb',
#              ['E:/pythonProject/MegaMail/Emails/Testing_Tools/EmailTesting.xlsx'])


def megamail_send(service, df, sender_email, email_sbj_noname, email_body_noname, want_name=0):
    for i in range(len(df)):
        destination = df.loc[i, 'email']
        name = df.loc[i, 'name']
        # email_sbj_name = 'Hello Mr.{}'.format(name)
        # email_body_name = 'Hello Mr.{} would you like to user our services'.format(name)
        # email_sbj_noname = 'Greetings'
        # email_body_noname = 'hello frick you, would you like to use our services'

        if not want_name:
            send_message(service, sender_email, destination, email_sbj_noname, email_body_noname)
        else:
            # send_message(service, email, email_sbj_name, email_body_name)
            pass


# service = gmail_authenticate("C:/Users/natha/Downloads/dev_key2.json")
#
# send_message(service, 'devburns22@gmail.com', 'devburns22+test1@gmail.com', 'testing send mess on Gmail_funcs', 'yup')