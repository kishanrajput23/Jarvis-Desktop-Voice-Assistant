#import dependencies
import pyttsx3
import pywin32_system32
import datetime
import speech_recognition as sr
import wikipedia
import webbrowser as wb
import os
import random
import pyautogui

#import javis actions
from jarvis_actions import speak
from jarvis_actions import time
from jarvis_actions import date
from jarvis_actions import wishme
from jarvis_actions import screenshot
from jarvis_actions import takecommand

#import evaluate query
from evaluate_query import evaluate_query


#start program
if __name__ == "__main__":
    #greet user
    wishme()

    while True:
        #acquire user input
        query = takecommand().lower()
        evaluate_query(query)
