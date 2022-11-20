# imports
from sys import path
import pyttsx3
import speech_recognition as sr
import datetime
import os
import cv2
import random
from requests import get
import wikipedia
import webbrowser
import pywhatkit as kit
import smtplib
import sys
import phonenumbers
from phonenumbers import geocoder
from phonenumbers import carrier
from opencage.geocoder import OpenCageGeocode
import requests
from bs4 import BeautifulSoup


# engine
engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
# print(voices[1].id)
engine.setProperty('voice', voices[1].id)


# print text to speech
def speak(audio):
    engine.say(audio)
    print(audio)
    engine.runAndWait()


# convert voice into text
def takecommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("listening...")
        r.pause_threshold = 2
        audio = r.listen(source, timeout=2, phrase_time_limit=5)

    try:
        print("Recognizing...")
        query = r.recognize_google(audio, language='en-in')
        print(f"user said: {query}")

    except Exception as e:
        speak("say that again please...")
        return "none"
    return query


# to wish
def wish():
    hour = int(datetime.datetime.now().hour)
    if hour >= 0 and hour < 12:
        speak("Good Morning")
    elif hour > 12 and hour < 18:
        speak("Good Afternoon")
    else:
        speak("Good Evening")
    speak("I am FRIDAY, please tell me what can I do for you")


# to send email
def sendEmail(to, content):
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.login('shreyasmithbawkar03@gmail.com', 'SHreyas@#1703')
    server.sendmail('shreyasmithbawkar03@gmail.com', to, content)


# define time
def time():
    time = datetime.datetime.now().strftime("%H:%M:%S")
    speak(time)


# main
if __name__ == "__main__":
    wish()
    while True:
        if 1:
            query = takecommand().lower()

            # logic building for task

            # to open notepad
            if "open notepad" in query:
                npath = "C:\\Windows\\system32\\notepad.exe"
                os.startfile(npath)
            elif"close notepad" in query:
                speak("Okay sir closing Notepad")
                os.system("taskkill /f /im notepad.exe")

            # to open pycharm
            elif "open pycharm" in query:
                npath = "C:\\Program Files\\JetBrains\\PyCharm Community Edition 2021.3\\bin\\pycharm64.exe"
                os.startfile(npath)
            elif"close pycharm" in query:
                speak("Okay sir closing pycharm")
                os.system("taskkill /f /im pycharm.exe")

            # to open vs code
            elif "open vscode" in query:
                npath = "C:\\Users\\LENOVO\\AppData\\Local\\Programs\\Microsoft VS Code"
                os.startfile(npath)
            elif"close vs code" in query:
                speak("Okay sir closing vs code")
                os.system("taskkill /f /im notepad.exe")

            # to open command prompt
            elif"close command prompt" in query:
                speak("Okay sir closing command prompt")
                os.system("taskkill /f /im cmd.exe")
            elif "command prompt" in query:
                os.system("start cmd")

            # to open camera
            elif "open camera" in query:
                cap = cv2.VideoCapture(0)
                while True:
                    ret, img = cap.read()
                    cv2.imshow('webcam', img)
                    k = cv2.waitKey(50)
                    if k == 27:
                        break
                cap.release()
                cv2.destroyAllWindows()

            # to play music
            elif "play music" in query:
                music_dir = "D:\\music"
                songs = os.listdir(music_dir)
                # rd = random.choice(songs)
                for song in songs:
                    if song.endswith('.mp3'):
                        os.startfile(os.path.join(music_dir, song))

            # to get IP address
            elif "ip address" in query:
                ip = get('https://api.ipify.org').text
                speak(f"Your IP address is {ip}")

            # to search on wikipedia
            elif "wikipedia" in query:
                speak("searching wikipedia.....")
                query = query.replace("wikipedia", "")
                results = wikipedia.summary(query, sentences=2)
                speak("according to wikipedia")
                speak(results)
                # print(results)

            # to open youtube
            elif "open youtube" in query:
                webbrowser.open("www.youtube.com")

            # to open facebook
            elif "open facebook" in query:
                webbrowser.open("www.facebook.com")

            # # to open Google
            elif "open google" in query:
                speak("Sir what should I search on Google")
                cm = takecommand().lower()
                webbrowser.open("{cm}")

            # to open whatsapp and send message
            elif "send message" in query:
                # parameters of time should be set accodring to the time at hich the message needs to be sent
                kit.sendwhatmsg("+917887821895",
                                "This is a testing message", 11, 10)

            # to open yotube and play a particular video
            elif "play song on youtube" in query:
                kit.playonyt("ranjha")

            # to open Gmail and send a mail to someone
            elif "send email to sharad" in query:
                try:
                    speak("What should I say?")
                    content = takecommand().lower()
                    to = "sharad.mithbawkar@gmail.com"
                    sendEmail(to, content)
                    speak("Email has been sent to Sharad")
                except Exception as e:
                    print(e)
                    speak("sorry sir I'm Not able to send this mail to Sharad")

            # to check the timing
            elif "the time" in query:
                strTime = datetime.datetime.now().strftime("%H:%M:%S")
                speak(f"Sir, The Time is {strTime}")

            # to track mobile location
            elif "track mobile location" in query:
                speak("Sir , what number should is search for?")
                tp = takecommand()
                tp = "+91 " + str(tp)
                ch_num = phonenumbers.parse(tp, "CH")
                print(geocoder.description_for_number(ch_num, "en"))
                service_num = phonenumbers.parse(tp, "RO")
                print(carrier.name_for_number(service_num, "en"))
                key = '56aa1028c4ae440889540998c2bafee8'
                geocoder = OpenCageGeocode(key)
                query = str(ch_num)
                results = geocoder.geocode(query)
                print(results)

            # to tell a joke
            # elif "tell me a joke" in query:
            #     joke = pyjokes.get_joke()
            #     speak(joke)

            # to restart, sleep, shutdown system

            elif "shut down the system" in query:
                os.system("shutdown /s /t 5")

            elif "restart the system" in query:
                os.system("shutdown /s /t 5")

            elif "sleep the system" in query:
                os.system("rund1132.exe powrprof.dll,SetSuspendState 0,1,0")

            # how was your day
            elif"how are you friday" in query:
                speak("I'm Good sir how are you?")
                query = takecommand().lower()
                if("i am good") in query:
                    speak("good to know sir")
                elif("i am not so good") in query:
                    speak("Hang in there sir, everything will be alright!")

            # friday defination
            elif"friday who are you" in query:
                speak("Friday stands for Female Replacement Intelligent Digital Assistant Youth, i'm an AI assistant, here to make your wok easy by setting alarms, sending emails, sending messages and lots of other stuff just on your command")

            # to exit
            elif "no thanks" in query:
                speak("Thanks for Using me sir, have a good day")
                sys.exit()

            elif "you can sleep now" in query:
                speak("Thanks for using me Sir, have a good day")
                sys.exit()

            elif "go to sleep" in query:
                speak("Thanks for using me Sir, have a good day")
                sys.exit()

        speak("Sir, do you need anything else?")
