import customtkinter as ctk
import jarvis_GUI
from jarvis_actions import speak
from listen import listen
#import jarvis


#change between light mode and dark mode
def change_appearence_mode(new_mode):
    ctk.set_appearance_mode(new_mode)


#listen for user input
def jarvis_button_click():
    print("Listening")
    speak("Listening")
    listen()
