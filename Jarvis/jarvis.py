import datetime
import os
import random
import subprocess
import sys
import webbrowser as wb
from pathlib import Path

import pyjokes
import pyautogui
import pyttsx3
import speech_recognition as sr
import wikipedia

# BASIC LANGUAGE STRINGS
STRINGS = {
    'fr': {
        'welcome': "Bon retour, monsieur !",
        'morning': "Bon matin !",
        'afternoon': "Bon après-midi !",
        'evening': "Bonsoir !",
        'night': "Bonne nuit, à demain.",
        'service': "{} à votre service. Comment puis-je vous aider ?",
        'time': "L'heure actuelle est ",
        'date': "La date d'aujourd'hui est le ",
        'screenshot': "Capture d'écran sauvegardée sous {}.",
        'listening': "À l'écoute...",
        'recognizing': "Reconnaissance...",
        'error_music': "Répertoire Musique introuvable.",
        'playing': "Lecture de {}.",
        'no_song': "Aucun morceau trouvé.",
        'ask_name': "Comment souhaitez-vous m'appeler ?",
        'name_set': "Très bien, je m'appellerai {} à partir de maintenant.",
        'wiki_search': "Recherche sur Wikipedia...",
        'no_result': "Je n'ai rien trouvé.",
        'shutdown': "Extinction du système !",
        'restart': "Redémarrage du système !",
        'offline': "Je passe en mode hors ligne. Bonne journée !"
    },
    'en': {
        'welcome': "Welcome back, sir!",
        'morning': "Good morning!",
        'afternoon': "Good afternoon!",
        'evening': "Good evening!",
        'night': "Good night, see you tomorrow.",
        'service': "{} at your service. How may I assist you?",
        'time': "The current time is ",
        'date': "The current date is ",
        'screenshot': "Screenshot saved as {}.",
        'listening': "Listening...",
        'recognizing': "Recognizing...",
        'error_music': "Music directory not found.",
        'playing': "Playing {}.",
        'no_song': "No song found.",
        'ask_name': "What would you like to name me?",
        'name_set': "Alright, I will be called {} from now on.",
        'wiki_search': "Searching Wikipedia...",
        'no_result': "I couldn't find anything.",
        'shutdown': "Shutting down system!",
        'restart': "Restarting system!",
        'offline': "Going offline. Have a good day!"
    }
}

# INIT
engine = pyttsx3.init()
voices = engine.getProperty('voices')
VOICE_MAP = {'fr': None, 'en': None}

for voice in voices:
    v_lang = str(voice.languages).lower()
    if "fr-fr" in v_lang or "french" in voice.name.lower():
        VOICE_MAP['fr'] = voice.id
    if "en-us" in v_lang or "english" in voice.name.lower():
        VOICE_MAP['en'] = voice.id

def set_voice(lang):
    if VOICE_MAP.get(lang):
        engine.setProperty('voice', VOICE_MAP[lang])

engine.setProperty('rate', 170)
engine.setProperty('volume', 1)

# CORE FUNCTIONS
def speak(text, lang='en'):
    set_voice(lang)
    engine.say(text)
    engine.runAndWait()

def open_media(path):
    cmd = "xdg-open" if sys.platform != "win32" else "start"
    if sys.platform == "win32":
        os.startfile(path)
    else:
        subprocess.call([cmd, str(path)])

def get_time(lang='en'):
    timer = datetime.datetime.now().strftime("%H:%M:%S")
    speak(STRINGS[lang]['time'], lang)
    speak(timer, lang='en')
    print(f"[{lang}] {timer}")

def get_date(lang='en'):
    now = datetime.datetime.now()
    speak(STRINGS[lang]['date'], lang)
    date_str = f"{now.day} {now.strftime('%B')} {now.year}"
    speak(date_str, lang)
    print(f"[{lang}] {date_str}")

def wish_me(lang='en'):
    speak(STRINGS[lang]['welcome'], lang)
    hour = datetime.datetime.now().hour
    if 4 <= hour < 12: key = 'morning'
    elif 12 <= hour < 18: key = 'afternoon'
    elif 18 <= hour < 24: key = 'evening'
    else: key = 'night'
    speak(STRINGS[lang][key], lang)
    name = load_name()
    speak(STRINGS[lang]['service'].format(name), lang)

def take_screenshot(lang='en'):
    path = Path.home() / "Pictures" / "screenshot.png"
    pyautogui.screenshot().save(str(path))
    speak(STRINGS[lang]['screenshot'].format(path), lang)

def take_command():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        r.adjust_for_ambient_noise(source)
        try:
            audio = r.listen(source, timeout=5)
        except:
            return None

    for lang_code in ["fr-FR", "en-US"]:
        try:
            query = r.recognize_google(audio, language=lang_code)
            print(f"({lang_code}) {query}")
            return query.lower()
        except:
            continue
    return None

def music_player(query, lang='en'):
    music_dir = Path.home() / "Music"
    if not music_dir.exists():
        return speak(STRINGS[lang]['error_music'], lang)
    
    songs = [f for f in music_dir.iterdir() if f.is_file()]
    if music_dir.exists():
        q_clean = query.replace("joue de la musique", "").replace("play music", "").strip()
        if q_clean:
            songs = [s for s in songs if q_clean in s.name.lower()]
        
        if songs:
            song = random.choice(songs)
            open_media(song)
            speak(STRINGS[lang]['playing'].format(song.name), lang)
        else:
            speak(STRINGS[lang]['no_song'], lang)

def wiki_search(query, lang='en'):
    speak(STRINGS[lang]['wiki_search'], lang)
    try:
        wikipedia.set_lang(lang)
        summary = wikipedia.summary(query, sentences=2)
        speak(summary, lang)
    except:
        speak(STRINGS[lang]['no_result'], lang)

def load_name():
    try:
        return Path("assistant_name.txt").read_text().strip()
    except:
        return "Jarvis"

# MAIN
if __name__ == "__main__":
    wish_me('en')
    
    while True:
        query = take_command()
        if not query: continue

        lang = 'fr' if any(w in query for w in ["heure", "date", "musique", "ouvre", "extinction", "redémarrage"]) else 'en'

        if any(w in query for w in ["heure", "time"]): get_time(lang)
        elif "date" in query: get_date(lang)
        elif "wikipedia" in query: wiki_search(query.replace("wikipedia", "").strip(), lang)
        elif any(w in query for w in ["musique", "music"]): music_player(query, lang)
        elif any(w in query for w in ["ouvre youtube", "open youtube"]): wb.open("youtube.com")
        elif any(w in query for w in ["ouvre google", "open google"]): wb.open("google.com")
        elif any(w in query for w in ["capture", "screenshot"]): take_screenshot(lang)
        elif "extinction" in query or "shutdown" in query:
            speak(STRINGS[lang]['shutdown'], lang)
            os.system("systemctl poweroff" if sys.platform != "win32" else "shutdown /s /f /t 1")
            break
        elif "redémarrage" in query or "restart" in query:
            speak(STRINGS[lang]['restart'], lang)
            os.system("systemctl reboot" if sys.platform != "win32" else "shutdown /r /f /t 1")
            break
        elif any(w in query for w in ["repos", "offline", "exit"]):
            speak(STRINGS[lang]['offline'], lang)
            break
