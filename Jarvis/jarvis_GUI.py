#import dependencies
import customtkinter as ctk

#import gui commands
from GUI_commands import change_appearence_mode


#set default settings - dark theme with blue colour theme
ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("blue")

#create app class
class App(ctk.CTk):
    def __init__(self):
        super().__init__()

        #create window
        #app = ctk.CTk()
        self.geometry("500x200")
        self.title("Jarvis")

        #create sidebar frame to hold settings
        self.sidebar_frame = ctk.CTkFrame(self, width=160, corner_radius=0)
        self.sidebar_frame.grid(row=0, column=0, sticky='nsew')

        #create main frame to hold jarvis button
        self.main_frame = ctk.CTkFrame(self, width=270)
        self.main_frame.grid(row=0, column=1, padx=37)

        #add settings label in sidebar
        self.settings_label = ctk.CTkLabel(self.sidebar_frame, text="Settings", font= ctk.CTkFont(size=18))
        self.settings_label.place(x=43, y=10)

        #add voice gender dropdown menu with label
        self.gender_menu_label = ctk.CTkLabel(self.sidebar_frame, text='Gender')
        self.gender_menu_label.place(x=55, y=40)
        self.gender_menu = ctk.CTkOptionMenu(self.sidebar_frame, values=['Male', 'Female'])
        self.gender_menu.place(x=10, y=70)

        #add light/dark mode dropdown menu with label
        self.mode_menu_label = ctk.CTkLabel(self.sidebar_frame, text='Appearence Mode')
        self.mode_menu_label.place(x=23, y=115)
        self.mode_menu = ctk.CTkOptionMenu(self.sidebar_frame, values=['Dark', 'Light'], command=change_appearence_mode)
        self.mode_menu.place(x=10, y=150)

        #add main button
        self.main_button = ctk.CTkButton(self.main_frame, text='Jarvis', height=75, width=100)
        self.main_button.place(x=85, y=62.5)
