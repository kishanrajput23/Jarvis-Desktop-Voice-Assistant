import customtkinter as ctk


#set default settings - dark theme with blue colour theme
ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("blue")

#create window
app = ctk.CTk()
app.geometry("500x200")
app.title("Jarvis")

#create sidebar frame to hold settings
sidebar_frame = ctk.CTkFrame(app, width=160, corner_radius=0)
sidebar_frame.grid(row=0, column=0, sticky='nsew')

#create main frame to hold jarvis button
main_frame = ctk.CTkFrame(app, width=270)
main_frame.grid(row=0, column=1, padx=37)

#add settings label in sidebar
settings_label = ctk.CTkLabel(sidebar_frame, text="Settings", font= ctk.CTkFont(size=18))
settings_label.place(x=43, y=10)

#add voice gender dropdown menu with label
gender_menu_label = ctk.CTkLabel(sidebar_frame, text='Gender')
gender_menu_label.place(x=55, y=40)
gender_menu = ctk.CTkOptionMenu(sidebar_frame, values=['Male', 'Female'])
gender_menu.place(x=10, y=70)

#add light/dark mode dropdown menu with label
mode_menu_label = ctk.CTkLabel(sidebar_frame, text='Appearence Mode')
mode_menu_label.place(x=23, y=115)
mode_menu = ctk.CTkOptionMenu(sidebar_frame, values=['Dark', 'Light'])
mode_menu.place(x=10, y=150)

#run interface
app.mainloop()
