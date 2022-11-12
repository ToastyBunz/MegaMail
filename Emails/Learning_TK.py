import tkinter as tk

# window one
# window = tk.Tk()
# greeting = tk.Label(window, text="Hello Master Nathan",foreground='white', background="#34A2FE", width=20, height=10)
# button = tk.Button(window, text='Self Destruct', width=20, height=5, background='red', foreground='black')
# greeting.pack()
# button.pack()
# window.mainloop()

# Window 2
# def on_change(e):
#     print(e.widget.get())
#
# window = tk.Tk()
# greeting = tk.Label(window, text='please input your name and rank')
# entry_name = tk.Entry(width=20)
# entry_rank = tk.Entry()
#
# greeting.pack()
# entry_name.pack()
# entry_rank.pack()
# entry_name.bind("<Return>", on_change)
# entry_rank.bind("<Return>", on_change)
# window.mainloop()

# Window 3
# def on_change(e):
#     print(e.widget.get())
#
# root = tk.Tk()
# e = tk.Entry(root)
# e.pack()
# # Calling on_change when you press the return key
# e.bind("<Return>", on_change)
#
# root.mainloop()


# Window 4 Text Box
# Email_1 = {}
#
# window = tk.Tk()
# frame_a = tk.Frame()
# frame_b = tk.Frame()
#
# label_a = tk.Label()
# # greeting = tk.Label(window, text="Hello Master Nathan",foreground='white', background="#34A2FE", width=20, height=10)
#
# text_box = tk.Text()
# text_box.pack()
# window.mainloop()


window = tk.Tk()
e = tk.Entry(window)
e.pack()
e.insert(0, 'Enter Your name')
window.mainloop()

