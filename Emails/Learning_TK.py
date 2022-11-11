import tkinter as tk

window = tk.Tk()
greeting = tk.Label(window, text="Hello Master Nathan",foreground='white', background="#34A2FE", width=20, height=10)

button = tk.Button(window, text='Self Destruct', width=20, height=5, background='red', foreground='black')
greeting.pack()
button.pack()
window.mainloop()
