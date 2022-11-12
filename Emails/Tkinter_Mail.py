# Fields
# User email
# Json (single line)
# excel (single line)
# Subject (single line)
# Body (Text box)
# Signature (Text Box, maybe multiple single lines)

from tkinter import *
from tkinter import messagebox
import os


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


def check_paths():
    personal_email = email_input.get()
    json_key = jsan_input.get()
    exel_contacts = exel_input.get()
    fixed_personal_email = fixed_path(personal_email)
    fixed_json_key = fixed_path(json_key)
    fixed_exel_contacts = fixed_path(exel_contacts)
    if not path_exists(fixed_json_key):
        print('Error: Json PATH is not valid')
        print(fixed_json_key)
        # TODO check if a json file
    elif not path_exists(fixed_exel_contacts):
        print('Error: Excel PATH is not Valid')
        print(fixed_exel_contacts)
        # TODO check if CSV or EXCEL
    else:
        top = Toplevel()
        # TODO Try globalizing top

        def popup():
            response = messagebox.askyesno("Ready to send", "Are you ready to send X emails")
            if response:
                Label(top, text='You clicked YES!').grid(row=8, column=1)
            else:
                Label(top, text='You clicked No!').grid(row=8, column=1)

        # TODO branches for auto name input and generic emails
        subjt = Entry(top, width=75)
        body = Text(top, width=75)
        signature_button = Button(top, text='Click to add signature?')  # if yes, else no
        signature_name = Entry(top, width=40)
        signature_number = Entry(top, width=40)
        signature_email = Entry(top, width=40)
        send_button = Button(top, text='Are you Ready to send?', command=popup)

        subjt.grid(row=1, column=1)
        body.grid(row=2, column=1)
        signature_button.grid(row=3, column=1)
        signature_name.grid(row=4, column=1)
        signature_number.grid(row=5, column=1)
        signature_email.grid(row=6, column=1)
        send_button.grid(row=7, column=1)

        subjt.insert(0, "Email Subject Here")
        body.insert(INSERT, "Email Body Here")
        signature_name.insert(0, "Enter name: John Doe")
        signature_number.insert(0, "Enter number: Office (999) 888 - 777")

    return fixed_personal_email, fixed_json_key, fixed_exel_contacts, top


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
# TODO Error pop up that prints errors

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