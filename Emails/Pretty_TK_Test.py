from tkinter import *
from tkinter import messagebox
import customtkinter

customtkinter.set_appearance_mode("System")  # Modes: system (default), light, dark
customtkinter.set_default_color_theme("blue")

app = customtkinter.CTk()
app.geometry(f"{600}x{500}")
app.title("CTk example")


entry = customtkinter.CTkEntry(master=app, placeholder_text="CTkEntry")
entry.grid(row=0, column=2, padx=20, pady=10)

label = customtkinter.CTkLabel(master=app, text="CTkLabel")
label.grid(row=0, column=1, padx=20, pady=10)

app.mainloop()