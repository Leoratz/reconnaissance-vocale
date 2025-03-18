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
        audio = r.listen(source)
        try:
            command = r.recognize_google(audio, language="fr-FR").lower()
            print(f"Commande reconnue : {command}")
            return command
        except sr.UnknownValueError:
            text = "Je n'ai pas compris ce que vous avez dit."
            print(text)
            speak(text)
        except sr.RequestError:
            text = "Erreur réseau."
            print(text)
            speak(text)

def process_command(command):
    if "ouvre navigateur" in command:
        speak("Ouverture du navigateur")
        commands.open_browser()

    elif "donne moi l'heure" in command:
        time = commands.tell_time()
        speak(time)

    elif "donne moi la date" in command:
        date = commands.tell_date()
        speak(date)

    elif "verrouille" in command:
        speak("Verrouillage de l'écran")
        commands.lock()

    else:
        speak("Commande non reconnue")

while True:
    cmd = recognize_commands()	
    if cmd:
        process_command(cmd)