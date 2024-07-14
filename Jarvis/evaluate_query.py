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


#####################-functions-#####################
def evaluate_query(query):
    #if the user mentions the time, report what time it is
    if "time" in query:
        time()

    #if the user mentions the date, report what the date is
    elif "date" in query:
        date()

    #if the user asks for information about the personal assistant, it is provided
    elif "who are you" in query:
        speak("I'm JARVIS created by Mr. Kishan and I'm a desktop voice assistant.")
        print("I'm JARVIS created by Mr. Kishan and I'm a desktop voice assistant.")

    #if the user asks the assistant how they are, an appropriate response is given
    elif "how are you" in query:
        speak("I'm fine sir, What about you?")
        print("I'm fine sir, What about you?")

    #if the user says that they are fine, then an appropriate response is given
    elif "fine" in query:
        speak("Glad to hear that sir!!")
        print("Glad to hear that sir!!")

    #if the user says that they are good, an appropriate response is given
    elif "good" in query:
        speak("Glad to hear that sir!!")
        print("Glad to hear that sir!!")

    #if the user wishes to recieve a wikipedia summary
    elif "wikipedia" in query:
        try:
            #feedback to let the user know that the assistant is working on it
            speak("Ok wait sir, I'm searching...")

            #remove the word wikipedia from the query and produce a result
            query = query.replace("wikipedia", "")
            result = wikipedia.summary(query, sentences=2)

            #output result
            print(result)
            speak(result)
        except:
            #if unsuccessful, inform the user
            speak("Can't find this page sir, please ask something else")

    #open youtube.com in default browser
    elif "open youtube" in query:
        wb.open("youtube.com")

    #open google.com in default browser
    elif "open google" in query:
        wb.open("google.com")

    #open stack overflow in default browser
    elif "open stack overflow" in query:
        wb.open("stackoverflow.com")

    #play music from a playlist
    elif "play music" in query:
        song_dir = os.path.expanduser("~\\Music")
        songs = os.listdir(song_dir)
        print(songs)
        x = len(songs)
        y = random.randint(0, x)
        os.startfile(os.path.join(song_dir, songs[y]))

    #open the chrome app
    elif "open chrome" in query:
        #FileNotFoundError causes termination - that is not where chrome is stored on my computer
        try:
            chromePath = "C:\\Program Files (x86)\\Google\\Chrome\\Application\\chrome.exe"
            os.startfile(chromePath)
        
        #FileNotFoundError - cannot find chrome in specified location
        except FileNotFoundError:
            speak("Could not find Chrome on your computer")
            print("Could not find Chrome on your computer")

    #open a chrome tab with a google search
    elif "search on chrome" in query:
        try:
            speak("What should I search?")
            print("What should I search?")
            chromePath = "C:\\Program Files (x86)\\Google\\Chrome\\Application\\chrome.exe"
            search = takecommand()
            wb.get(chromePath).open_new_tab(search)
            print(search)

        ##FileNotFoundError - cannot find chrome in specified location
        except FileNotFoundError:
            speak("Could not find Chrome on your computer")
            print("Could not find Chrome on your computer")

        except Exception as e:
            speak("Can't open now, please try again later.")
            print("Can't open now, please try again later.")

    #transcribe a note
    elif "remember that" in query:
        speak("What should I remember")
        data = takecommand()
        speak("You said me to remember that" + data)
        print("You said me to remember that " + str(data))
        remember = open("data.txt", "w")
        remember.write(data)
        remember.close()

    #read out transcribed notes
    elif "do you remember anything" in query:
        remember = open("data.txt", "r")
        speak("You told me to remember that" + remember.read())
        print("You told me to remember that " + str(remember))

    #perform a screesnhsot
    elif "screenshot" in query:
        screenshot()
        speak("I've taken screenshot, please check it")

    #end the program
    elif "offline" in query:
        quit()