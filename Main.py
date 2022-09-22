import time
from antapi import decrypt, encrypt
import PIL.Image as Image
import io
import subprocess
import wolframalpha
import pyttsx3
import speech_recognition as sr
import webbrowser
import os
from playsound import playsound

from pynput.keyboard import Key,Controller
keyboard = Controller()


engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)
engine.setProperty('rate', 160)
all_command= ["google search","youtube","youtube search","web",
             "competitive game time","grinding game","cartoon","play",
             "pause", "continue","shutdown pc","restart the pc","log off",
             "increase volume","decrease volume","prevous","next","open"]


#wolframal
app_id = "G375LT-LXHW8RY4ET"

def big_main():
        while True:
           r = sr.Recognizer()
           with sr.Microphone() as source:
                os.system("cls")
                print(".")
                r.pause_threshold = 0.5
                audio = r.listen(source)
           try:
                os.system("cls")
                print("-")
                query = r.recognize_google(audio, language='en-us')
                if any(k in query.lower() for k in  ["cherry" , "jerry","sirri","bot","monu","hey"]):
                            tell("Yes Sir!")  
                            playsound('O:\\Works\\JucyAssistant\\sound.wav')
                            main()
            

                elif ("close" in query.lower()):
                        tell("ok")
                        exit()
                        
           except Exception as e:
                        os.system("cls")
                        print("*")


def qna(q):
    client = wolframalpha.Client(app_id)
    res = client.query(q)
    answer = next(res.results).text
    return answer



def takeCommand():
    query = ""
    r = sr.Recognizer()
    with sr.Microphone() as source:
        os.system("cls")
        print("^.^")
        r.pause_threshold = 1
        audio = r.listen(source)
    try:
        os.system("cls")
        print("^_^'")
        query = r.recognize_google(audio, language ='en-us')

    except Exception as e:
        os.system("cls")
        print("^_^'")
    return query


def g_search(keyword):
    webbrowser.open(f"https://www.google.com/search?q={keyword}", new=2)

def you_s(keyword):\
        webbrowser.open(f"https://www.youtube.com/results?search_query={keyword}", new=2)


def p_s(keword):
    # subprocess.call("start firefox -private ")
   webbrowser.open(f"https://www.{keword}.com/", new=2)






def tell(talk):
        engine.say(talk)
        engine.runAndWait()

def say(something):
    tell(something)


def writesome(x):
    os.system(f"echo '{x}'")


def sound_Inc():
        for i in range(5):
            keyboard.press(Key.media_volume_up)
            keyboard.release(Key.media_volume_up)
            time.sleep(0.1)


def sound_Dec():
        for i in range(10):
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
    if any(k in me for k in  ["visual studio" , "vs code"]):
            os.system("code")
    else:
        os.system(me)
    

def chat(name):
    pass

qn =  ["what" , "how" , "where" , "who" , "why" , "when"]

#main
def main():   
        al = takeCommand().lower()
    # matches = [x for x in all_command if x in al]
    # for data in matches:
    #     tell(data)

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

        elif "competitive game time" in data:
            tell("Valorant loading")
            subprocess.call("C:\\Riot Games\\Riot Client\\RiotClientServices.exe")
        elif "grinding game" in data:
            subprocess.call("M:\\Game\\Genshin\\Genshin Impact game\\GenshinImpact.exe")
        elif "youtube" in data:
            os.system("start firefox youtube.com")
        elif "cartoon" in data:
            os.system("start firefox https://9anime.id/")
        elif "shutdown pc" in data:
            subprocess.call(["shutdown", "/s"])
        elif "restart the pc" in data:
            subprocess.call(["shutdown", "/r"])
        elif "log off" in data:
            subprocess.call(["shutdown", "/l "])
        elif 'repeat' in data:
            say(data[6:])
        elif "increase volume" in data:
            sound_Inc()
        elif "decrease volume" in data:
            sound_Dec()
        elif any(k in data for k in  ["play" , "pause", "continue"]):
            pause()
            tell("done")
        elif "prevous" in data:
            prev_med()
        elif "next" in data:
            next_med()
        elif "open" in data:
            tell("ok")
            O_app(data[4:])   
        else:
            tell("NO Command")
        



if __name__ == '__main__':
        os.system("cls")
        big_main()




        # q = takeCommand()
        # print(q)
        
        # str = "play and increase volume pause"
        # matches = [x for x in all_command if x in str]
        # print(matches)
        

        #TODO: React Face
        #TODO: Multiple Command