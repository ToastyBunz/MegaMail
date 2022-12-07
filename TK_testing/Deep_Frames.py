# Basic frames Gmail outlook
# Analytics frame (same for both)
# Send mail frame
# forward and backward buttons for each frame
# bar that increases as user goes deeper

import tkinter

import customtkinter
import os
from PIL import Image


class App(customtkinter.CTk):
    def __init__(self):
        super().__init__()

        self.title('Mega Mail')
        self.geometry('700x450')
        self.grid_rowconfigure(0, weight=1)
        self.grid_columnconfigure(1, weight=1)

        # create navigation frame
        self.navigation_frame = customtkinter.CTkFrame(self, corner_radius=0)
        self.navigation_frame.grid(row=0, column=0, sticky='nsew')
        self.navigation_frame.grid_rowconfigure(4, weight=1)

        self.navigation_frame_label = customtkinter.CTkLabel(self.navigation_frame, text="Navigation",
                                                             # image=self.logo_image,
                                                             compound="left",
                                                             font=customtkinter.CTkFont(size=15, weight="bold"))
        self.navigation_frame_label.grid(row=0, column=0, padx=20, pady=20)

        self.home_button = customtkinter.CTkButton(self.navigation_frame, corner_radius=0, height=40, border_spacing=10,
                                                   text="Analytics",
                                                   fg_color="transparent", text_color=("gray10", "gray90"),
                                                   hover_color=("gray70", "gray30"),
                                                   # image=self.home_image,
                                                   anchor="w",
                                                   command=self.home_button_event
                                                   )

        self.home_button.grid(row=1, column=0, sticky="ew")

        self.frame_outlook_button = customtkinter.CTkButton(self.navigation_frame, corner_radius=0, height=40,
                                                            border_spacing=10, text="Outlook",
                                                            fg_color="transparent", text_color=("gray10", "gray90"),
                                                            hover_color=("gray70", "gray30"),
                                                            # image=self.chat_image,
                                                            anchor="w",
                                                            command=self.frame_outlook_button_event
                                                            )
        self.frame_outlook_button.grid(row=2, column=0, sticky="ew")

        self.frame_gmail_button = customtkinter.CTkButton(self.navigation_frame, corner_radius=0, height=40,
                                                          border_spacing=10, text="Gmail",
                                                          fg_color="transparent", text_color=("gray10", "gray90"),
                                                          hover_color=("gray70", "gray30"),
                                                          # image=self.add_user_image,
                                                          anchor="w",
                                                          command=self.frame_gmail_button_event
                                                          )
        self.frame_gmail_button.grid(row=3, column=0, sticky="ew")

        self.appearance_mode_menu = customtkinter.CTkOptionMenu(self.navigation_frame,
                                                                values=["System", "Light", "Dark"],
                                                                command=self.change_appearance_mode_event
                                                                )
        self.appearance_mode_menu.grid(row=6, column=0, padx=20, pady=20, sticky="s")

        self.home_frame = customtkinter.CTkFrame(self, corner_radius=0, fg_color="transparent")
        self.home_frame.grid_columnconfigure(0, weight=1)

        self.home_frame_button_1 = customtkinter.CTkButton(self.home_frame, text="This feature is not ready yet")
        self.home_frame_button_1.grid(row=1, column=0, padx=20, pady=10)

        self.outlook_frame = customtkinter.CTkFrame(self, corner_radius=0, fg_color="transparent")

        # create third frame
        self.gmail_frame = customtkinter.CTkFrame(self, corner_radius=0, fg_color="transparent")

        # select default frame
        self.select_frame_by_name("Analytics")

    def select_frame_by_name(self, name):
        # set button color for selected button
        self.home_button.configure(fg_color=("gray75", "gray25") if name == "Analytics" else "transparent")
        self.frame_outlook_button.configure(fg_color=("gray75", "gray25") if name == "Outlook" else "transparent")
        self.frame_gmail_button.configure(fg_color=("gray75", "gray25") if name == "Gmail" else "transparent")

        # show selected frame
        if name == "Analytics":
            self.home_frame.grid(row=0, column=1, sticky="nsew")
        else:
            self.home_frame.grid_forget()
        if name == "Outlook":
            self.outlook_frame.grid(row=0, column=1, sticky="nsew")
        else:
            self.outlook_frame.grid_forget()
        if name == "Gmail":
            self.gmail_frame.grid(row=0, column=1, sticky="nsew")
        else:
            self.gmail_frame.grid_forget()

    def home_button_event(self):
        self.select_frame_by_name("Analytics")

    def frame_outlook_button_event(self):
        self.select_frame_by_name("Outlook")

    def frame_gmail_button_event(self):
        self.select_frame_by_name("Gmail")

    def change_appearance_mode_event(self, new_appearance_mode):
        customtkinter.set_appearance_mode(new_appearance_mode)


if __name__ == "__main__":
    app = App()
    app.mainloop()