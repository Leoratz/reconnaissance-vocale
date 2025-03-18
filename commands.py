import subprocess
import datetime
import platform
import webbrowser

def open_browser():
    webbrowser.open('https://www.google.com')

def tell_date():
    today = datetime.datetime.now().strftime('%Y-%m-%d')
    return f'Nous sommes le {today}'

def tell_time():
    time = datetime.datetime.now().strftime('%H:%M:%S')
    return f"Il est {time}."
    

def lock():
    if platform.system() == 'Darwin':
        subprocess.call('pmset displaysleepnow')
    elif platform.system() == 'Windows':
        subprocess.call('rundll32.exe user32.dll,LockWorkStation')
    elif platform.system() == 'Linux':
        subprocess.call('gnome-screensaver-command -l')