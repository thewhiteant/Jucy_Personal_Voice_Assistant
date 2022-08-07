from time import sleep
import speech_recognition as sr
import pyttsx3
import os
# Talking Feaature
engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)
engine.setProperty('rate', 140) 
    

def tell(talk):
        engine.say(talk)      
        engine.runAndWait()



def takeCommand():
     
    r = sr.Recognizer()
     
    with sr.Microphone() as source:
         
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source)
  
    try:
        print("Recognizing...")   
        query = r.recognize_google(audio, language ='en-in')
        print(f"User said: {query}\n")
  
    except Exception as e:
        print(e)   
        print("Unable to Recognize your voice.") 
        return "None"
     
    return query


def writesome(x):
    print(x)


def main():
    data = takeCommand()
    if data.lower() == "clear the screen":
        os.system('cls')
        tell("Complete Screen Cleaning")
    elif data.lower() == "where am i":
        sleep(1)
        print(os.path)
        tell(f"Your Path Is {os.path}")
    elif data.lower() == "who are you":
           tell("Hi I am White Ant's Personal Assistant")
           sleep(1)
    elif data.lower() == "my friends":
           tell("Arpita And konamona")
           sleep(1)
    elif data.lower() == "stop":
           tell("Oky Bye Bye")
           exit()

    else:
        tell("What you Say I don't Recognise Say Again ")






if __name__ == '__main__':
        while True:
            main()
            sleep(3)


#v1 incomming