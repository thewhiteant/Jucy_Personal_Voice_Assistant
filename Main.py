import time
import PIL.Image as Image
import io
import subprocess
import wolframalpha
import pyttsx3
import speech_recognition as sr
import webbrowser
import os
from pynput.keyboard import Key, Controller

# Initialize keyboard and text-to-speech engine
keyboard = Controller()
engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)
engine.setProperty('rate', 160)

# List of recognized commands
all_commands = ["google search", "youtube", "youtube search", "web",
                "competitive game time", "grinding game", "cartoon", "play",
                "pause", "continue", "shutdown pc", "restart the pc", "log off",
                "increase volume", "decrease volume", "prevous", "next", "open"]

#wolframalpha
app_id = "G375LT-LXHW8RY4ET"

def big_main():
    while True:
        r = sr.Recognizer()
        with sr.Microphone() as source:
            #os.system("clear")
            print("Listening...")
            r.pause_threshold = 0.5
            audio = r.listen(source)
        try:
            #os.system("clear")
            print("Processing...")
            query = r.recognize_google(audio, language='en-us')
            if any(k in query.lower() for k in ["cherry", "jerry", "sirri", "bot", "monu", "hey"]):
                tell("Yes Sir!")
                playsound('sound.wav')
                main()

            elif ("close" in query.lower()):
                tell("Ok")
                exit()

        except Exception as e:
            #os.system("clear")
            print("Couldn't recognize. Try again.")

def qna(q):
    client = wolframalpha.Client(app_id)
    res = client.query(q)
    answer = next(res.results).text
    return answer

def take_command():
    """Listens for voice commands and returns the recognized text."""
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source)
    try:
        print("Processing...")
        query = r.recognize_google(audio, language='en-us')
        return query.lower()  # Convert to lowercase for case-insensitive matching
    except Exception as e:
        print("Couldn't recognize. Try again.")
        return None

        
def g_search(keyword):
    webbrowser.open(f"https://www.google.com/search?q={keyword}", new=2)

def you_s(keyword):
    webbrowser.open(f"https://www.youtube.com/results?search_query={keyword}", new=2)

def p_s(keyword):
    webbrowser.open(f"https://www.{keyword}.com/", new=2)

def tell(talk):
    engine.say(talk)
    engine.runAndWait()

def say(something):
    """Speaks the given text aloud."""
    engine.say(something)
    engine.runAndWait()


def sound_Inc():
    for _ in range(5):
        keyboard.press(Key.media_volume_up)
        keyboard.release(Key.media_volume_up)
        time.sleep(0.1)

def sound_Dec():
    for _ in range(10):
        keyboard.press(Key.media_volume_down)
        keyboard.release(Key.media_volume_down)
        time.sleep(0.1)

def pause():
    keyboard.press(Key.media_play_pause)
    keyboard.release(Key.media_play_pause)

def prev_med():
    keyboard.press(Key.media_previous)
    keyboard.release(Key.media_previous)

def next_med():
    keyboard.press(Key.media_next)
    keyboard.release(Key.media_next)

def O_app(me):
    if any(k in me for k in ["visual studio", "vs code"]):
        os.system("code")
    else:
        subprocess.run(me, shell=True)

def chat(name):
    pass

qn = ["what", "how", "where", "who", "why", "when"]

# main
def main():
    al = takeCommand().lower()

    data = al
    if(data == ""):
        return 0

    if any(c in data for c in qn):
        tell(qna(data))

    elif "google search" in data:
        if(data[13:]):
            tell("Searching.... ")
            g_search(data[13:])
        else:
            tell("No keyword")

    elif "youtube search" in data:
        if(data[14:]):
            tell("Searching.... ")
            you_s(data[14:])
        else:
            tell("No keyword")

    elif "web" in data:
        if(data[3:]):
            tell("Wait a second")
            p_s(data[3:])
        else:
            tell("No keyword")

   

    elif "youtube" in data:
        os.system("firefox https://youtube.com &")

    elif "cartoon" in data:
        os.system("firefox https://9anime.id/ &")

    elif "shutdown pc" in data:
        os.system("shutdown now")

    elif "restart the pc" in data:
        os.system("reboot")

    elif "log off" in data:
        os.system("logout")

    elif 'repeat' in data:
        say(data[6:])

    elif "increase volume" in data:
        sound_Inc()

    elif "decrease volume" in data:
        sound_Dec()

    elif any(k in data for k in ["play", "pause", "continue"]):
        pause()
        tell("Done")

    elif "prevous" in data:
        prev_med()

    elif "next" in data:
        next_med()

    elif "open" in data:
        tell("Ok")
        O_app(data[4:])

    else:
        tell("No command found")

if __name__ == '__main__':
    #os.system("clear")
    big_main()
