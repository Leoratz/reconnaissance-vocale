import speech_recognition as sr
import pyttsx3
import commands

engine = pyttsx3.init()

def speak(text):
    engine.say(text)
    engine.runAndWait()

def recognize_commands():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Dites quelque chose...")
        

speak("Bonjour, je suis ton assistant vocal.")