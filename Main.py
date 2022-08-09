from distutils.command.clean import clean
from time import sleep
from unicodedata import decimal
from antapi import decrypt , encrypt
import PIL.Image as Image
import io
import subprocess
import wolframalpha
import pyttsx3
import tkinter
import json
import random
import operator
import speech_recognition as sr
import datetime
import wikipedia
import webbrowser
import os
import winshell
import pyjokes
import feedparser
import smtplib
import ctypes
import time
import shutil
from twilio.rest import Client
from clint.textui import progress
from ecapture import ecapture as ec
from bs4 import BeautifulSoup
import win32com.client as wincl
from urllib.request import urlopen




engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)
engine.setProperty('rate', 140)




def takeCommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        os.system("cls")
        print("^.^")
        r.pause_threshold = 1
        audio = r.listen(source)
    try:
        os.system("cls")
        print("^_^'")
        query = r.recognize_google(audio, language ='en-US')

    except Exception as e:
        os.system("cls")
        print("^_^'")
    return query



def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour>= 0 and hour<12:
        tell("Good Morning Sir !")

    elif hour>= 12 and hour<18:
        tell("Good Afternoon Sir !")

    else:
        tell("Good Evening Sir !")
    assname =("Cherry")
    tell("I am White Ant personal Assistant")
    tell(assname)



def sendEmail(to, content):
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()

    # Enable low security in gmail
    server.login('your email id', 'your email password')
    server.sendmail('your email id', to, content)
    server.close()










#my




def g_search(keyword):
    webbrowser.open(f"https://www.google.com/search?q={keyword}", new=2)

def p_s(keword):
    os.system(f"start firefox -private https://www.google.com/search?q={keyword}")

def POMH(hash):

    path = "Sources/ok"
    key = int(decrypt(hash))
    fin = open(path, 'rb')
    image = fin.read()
    fin.close()
    image = bytearray(image)
    for index, values in enumerate(image):
        image[index] = values ^ key


    image = Image.open(io.BytesIO(image))
    image.show()





def tell(talk):
        engine.say(talk)
        engine.runAndWait()




def writesome(x):
    print(x)


def main():
    data = takeCommand().lower()
  #v hobe edike
    if decrypt("vw}y$bshxIyllhJEehJDH") in data:
        tell("Pass Code")
        dat = takeCommand()
        if dat  == decrypt("9z4y4rIBD"):
             POMH(encrypt(dat))
    elif "google search" in data:
        if(data[13:]):
               tell("Searching.... ")
               g_search(data[13:])
        else:
            tell("No keyword")
    elif "private search" in data:
        if(data[14:]):
               tell("Searching.... ")
               g_search(data[14:])
        else:
            tell("No keyword")

    elif "competitive game time" in data:
        tell("Valorant loading")
        subprocess.call("C:\\Riot Games\\Riot Client\\RiotClientServices.exe")
    elif "youtube" in data:
        os.system("start firefox youtube.com")
    elif "stop" in data:
        tell("Good Bye Pi pi ")
        return 0
    elif "cartoon" in data:
        os.system("start firefox https://9anime.id/")
    elif "shutdown pc" in data:
        subprocess.call(["shutdown", "/s"])
    elif "restart the pc" in data:
        subprocess.call(["shutdown", "/r"])
    elif "log off" in data:
        subprocess.call(["shutdown", "/l "])



if __name__ == '__main__':
        clean = lambda: os.system("cls")
        clean()


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
                query = r.recognize_google(audio, language='en-US')
                if ("cherry" in query.lower()):
                        wishMe()
                        while True:
                            if main() == 0:
                                break
                elif ("close" in query.lower()):
                    exit()

           except Exception as e:
                        os.system("cls")
                        print("*")
