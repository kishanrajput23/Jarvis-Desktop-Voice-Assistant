import customtkinter as ctk


#set default settings - dark theme with blue colour theme
ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("blue")

#create window
app = ctk.CTk()
app.geometry("500x200")
app.title("Jarvis")

#

#run interface
app.mainloop()
