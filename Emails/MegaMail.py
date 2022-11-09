# make tk pretty again https://github.com/TomSchimansky/CustomTkinter

# Steps
# pick email column and names X
# get excel, clean X
# print new number X
# email subj, body (with formatting), attach. Allow for name to be replaced
# loop email addresses - send
# Loading bar
# Wrap with GUI
# Make TKInter pretty
# Set a kill date for free trial


import pandas as pd
# import xlrd
import tkinter as tk

# window = tk.Tk()
# theLabel = tk.Label(window, text='Mega Mail', foreground='white', background='black')
# theLabel.pack()
# window.mainloop()

excel_file = "E:/EmailTesting.xlsx"
email = 'email'
name = 'name'

df = pd.DataFrame(pd.read_excel(excel_file))
df[email] = df[email].astype('string')

df = df.dropna(axis=0, subset=[email])
df = df.fillna(0, axis=0)
df = df.drop_duplicates(subset=email)
df = df.reset_index()
del df['index']
print(df)

print('there are now {} emails after cleaning'.format(len(df)))