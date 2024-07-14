import customtkinter as ctk


#set default settings - dark theme with blue colour theme
ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("blue")

#create window
app = ctk.CTk()
app.geometry("500x200")
app.title("Jarvis")

#create sidebar frame
sidebar_frame = ctk.CTkFrame(app, width=130, corner_radius=0)
sidebar_frame.grid(row=0, column=0, sticky='nsew')

#create main frame
main_frame = ctk.CTkFrame(app, width=300)
main_frame.grid(row=0, column=1, padx=37)

#run interface
app.mainloop()
