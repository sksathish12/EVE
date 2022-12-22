import sys
import time
import pyautogui
import pyttsx3
import pywhatkit
import speech_recognition as sr
import datetime
import os.path
import os
import cv2
import random
import requests
from requests import get
import wikipedia
import webbrowser
import pywhatkit as kit
import smtplib
import pyjokes
import PyPDF2
import speedtest
from tkinter import *
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase
from email import encoders
from bs4 import BeautifulSoup
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import QTimer, QTime, QDate, Qt
from PyQt5.QtGui import QMovie
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.uic import loadUiType
from evegui2 import Ui_evegui2
import platform
from PySide2 import QtCore, QtGui, QtWidgets
from PySide2.QtCore import (QCoreApplication, QPropertyAnimation, QDate, QDateTime, QMetaObject,
                            QObject, QPoint, QRect, QSize, QUrl, Qt, QEvent, QTimer)
from PySide2.QtGui import (QBrush, QColor, QConicalGradient, QCursor, QFont,
                           QFontDatabase, QIcon, QKeySequence, QLinearGradient, QPalette, QPainter, QPixmap,
                           QRadialGradient)
from PySide2.QtWidgets import *
from ui_main import Ui_MainWindow

engine = pyttsx3.init('sapi5')
voices=engine.getProperty('voices')
print(voices[0].id)
engine.setProperty('voices',voices[0].id)

GREETINGS = ["hello eve", "eve", "wake up eve", "you there eve", "time to work eve", "hey eve",
             "ok eve", "are you there"]
GREETINGS_RES = ["always there for you master", "i am ready master",
                 "your wish my command", "how can i help you master?", "i am online and ready master"]
UI = Ui_MainWindow()
#text to speah
def speak(audio):
    engine.say(audio)
    print(audio)
    engine.runAndWait()
def setDiscussionValue(valueDiscuss):
    UI.textDisplayConversation.append(f"{valueDiscuss}")


def setDisplayValue(valueDisp):
    UI.display.setText(f"{valueDisp}")
def voice():
    rec = sr.Recognizer()

    with sr.Microphone() as source:
        print("Listening...")
        audio = rec.listen(source)
        said = ""

        try:
            said = rec.recognize_google(audio)
            print(said)

        except Exception as e:
            print(e)
            print("Unable to Recognize your voice.")
        return "None"

    return query
def email(self):
    to = self.btn_audio_mode.text()

#------------------latest news-----------------
def news():
    main_url='http://newsapi.org/v2/top-headlines?sources=techcrunch&apikey=9f1a68ff964743f6a90a493bcba39e78'

    main_page = requests.get(main_url).json()
    articles = main_page["articles"]
    head = []
    day = ["first","second","third","fourth","fifth","sixth","seventh","eigth","ninth","tenth"]
    for ar in articles:
        head.append(ar["title"])
    for i in range (len(day)):
        setDiscussionValue(f"Eve: today's {day[i]} news is: {head[i]}")
        setDisplayValue("Speaking...")
        speak(f"today's {day[i]} news is: {head[i]}")
#----------------------pdf reader--------------
def pdf_reader():
    book = open('half-girlfriend(eve).pdf', 'rb')
    pdfReader = PyPDF2.PdfFileReader(book)
    pages = pdfReader.numPages
    speak(f"Total numbers of pages in this book {pages}")
    speak("master please enter the page number i have to read")
    pg = int(input("Please enter the page number: "))
    for num in range(pg,pages):
        page = pdfReader.getPage(pg)
        text = page.extractText()
        speak(text)
#-------------------egular wish-----------------
def wish():
        hour = int(datetime.datetime.now().hour)
        tt = time.strftime("%I:%M %p")

        if hour >= 0 and hour <= 12:
            setDiscussionValue(f"Eve: good morning ,its {tt}")
            setDisplayValue("Speaking...")
            speak(f"good morning ,its {tt}")

        elif hour >= 12 and hour <= 18:
            setDiscussionValue(f"Eve: good afternoon ,its {tt}")
            setDisplayValue("Speaking...")
            speak(f"good afternoon ,its {tt}")

        else:
            setDiscussionValue(f"Eve: good evening ,its {tt}")
            setDisplayValue("Speaking...")
            speak(f"good evening ,its {tt}")
        setDiscussionValue("Eve: master  i am EVE .  please tell how can i help you")
        setDisplayValue("Speaking...")
        speak("master  i am EVE .  please tell how can i help you")
#------------covid--------------
def coronaVirus(country):
            countries = str(country).replace(" ", "")
            url = f"https://www.worldometers.info/coronavirus/country/{countries}/"
            result = requests.get(url)
            soups = BeautifulSoup(result.text, 'lxml')
            corona = soups.find_all('div', class_='maincounter-number')
            Data = []
            for case in corona:
                span = case.find('span')
                Data.append(span.string)
            cases, Death, recovored = Data
            setDiscussionValue(f"Eve: Cases : {cases}")
            setDisplayValue("Speaking...")
            speak(f"Cases : {cases}")
            setDiscussionValue(f"Eve: Deaths : {Death}")
            setDisplayValue("Speaking...")
            speak(f"Deaths : {Death}")
            setDiscussionValue(f"Eve: Recovered : {recovored}")
            setDisplayValue("Speaking...")
            speak(f"Recovered : {recovored}")
class MainThread(QThread):
    def _init_(self):
        super(MainThread, self)._init_()
    def run(self):
        self.Totaltask()

    # speah to text
    def takecommand(self):
        r = sr.Recognizer()
        with sr.Microphone() as source:
            print("Listening...")
            setDisplayValue("Listening...")
            r.pause_threshold = 1
            audio = r.listen(source)
        try:
            print("Recognizing...")
            setDisplayValue("Recognizing...")
            query = r.recognize_google(audio, language='en-in')
            print(f"User said: {query}\n")
            setDiscussionValue(f"User: {query}\n")
        except Exception as e:
            print(e)

            print("Say that again please...")
            UI.display.setText("Say that again please...")
            return "None"
        return query

    @property
    def Totaltask(self):
        wish()
        while True:
            self.query = self.takecommand().lower()
            # ---------------To open windows application-----------------
            if "open notepad" in self.query:
                setDiscussionValue("Eve: Opening notepad")
                setDisplayValue("Speaking...")
                speak("okay master, opening notepad")
                # s="opening note pad"
                # Main().user(s)
                npath = "C:\\WINDOWS\\system32\\notepad.exe"
                os.startfile(npath)

            elif "open command prompt" in self.query:
                setDiscussionValue("Eve: Opening command prompt")
                setDisplayValue("Speaking...")
                speak("okay master, opening command prompt")
                os.system("start cmd")

            elif "open discord" in self.query:
                setDiscussionValue("Eve: Opening Discord")
                setDisplayValue("Speaking...")
                speak("okay master, opening Discord")
                npath = "C:\\Users\\sksat\\AppData\Local\\Discord\\app-0.0.309\\Discord.exe"
                os.startfile(npath)

            elif "open camera" in self.query:
                setDiscussionValue("Eve: Opening camera")
                setDisplayValue("Speaking...")
                speak("okay master, opening camera")
                cap = cv2.VideoCapture(0)
                while True:
                    ret, img = cap.read()
                    cv2.imshow('webcam', img)
                    k = cv2.waitKey(1)
                    if k == 0.5:
                        break;
                cap.release()
                cv2.destroyAllWindows()

            elif "play music" in self.query:
                setDiscussionValue("Eve: playing music")
                setDisplayValue("Speaking...")
                speak("okay master, playing music")
                music_dir = "D:\\android\\songs"
                songs = os.listdir(music_dir)
                rd = random.choice(songs)
                os.startfile(os.path.join(music_dir, rd))
            elif "ip address" in self.query:
                setDiscussionValue("Eve: getting ip address")
                setDisplayValue("Speaking...")
                speak("okay master, getting ip address")
                ip = get('https://api.ipify.org').text
                setDiscussionValue(f"Eve: your IP address is {ip}")
                setDisplayValue("Speaking...")
                speak(f"your IP address is {ip}")
            elif self.query in GREETINGS:
                greet = random.choice(GREETINGS_RES)
                #setDiscussionValue(f"{greet}")
                speak(f"{greet}")
            elif "wikipedia" in self.query:
                setDiscussionValue("Eve: searching wikipedia")
                setDisplayValue("Speaking...")
                speak("searching wikipedia...")
                self.query = self.query.replace("wikipedia","")
                results = wikipedia.summary(self.query, sentences=2)
                setDiscussionValue("Eve: according to wikipedia")
                setDisplayValue("Speaking...")
                speak("according to wikipedia")
                setDiscussionValue(f"Eve: {results}")
                setDisplayValue("Speaking...")
                speak(results)
                # print(results)
            elif "open youtube" in self.query:
                setDiscussionValue("Eve: Opening youtube")
                setDisplayValue("Speaking...")
                speak("okay master, opening youtube")
                webbrowser.open("www.youtube.com")
            elif "open facebook" in self.query:
                setDiscussionValue("Eve: Opening facebook")
                setDisplayValue("Speaking...")
                speak("okay master, opening facebook")
                webbrowser.open("www.facebook.com")
            # ---------------To close windows application-----------------
            elif "close notepad" in self.query:
                setDiscussionValue("Eve: closing notepad")
                setDisplayValue("Speaking...")
                speak("okay master, closing notepad")
                os.system("taskkill /f /im notepad.exe")
            elif "close command prompt" in self.query:
                setDiscussionValue("Eve: closing command prompt")
                setDisplayValue("Speaking...")
                speak("okay master, closing command prompt")
                os.system("taskkill /f /im cmd.exe")
            elif "close discord" in self.query:
                setDiscussionValue("Eve: closing discord")
                setDisplayValue("Speaking...")
                speak("okay master, closing discord")
                os.system("taskkill /f /im Discord.exe")
            elif "close camera" in self.query:
                setDiscussionValue("Eve: closing camera")
                setDisplayValue("Speaking...")
                speak("okay master, closing camera")
                os.system("taskkill /f /im camera.exe")
            # ---------------To take notes-----------------
            elif "write a note" in self.query:
                setDiscussionValue("Eve: What should i write, sir")
                setDisplayValue("Speaking...")
                speak("What should i write, sir")
                note = voice()
                file = open('eve.txt', 'w')
                setDiscussionValue("Eve: Should i include date and time")
                setDisplayValue("Speaking...")
                speak("Sir, Should i include date and time")
                snfm = voice()
                if 'yes' in snfm or 'sure' in snfm:
                    strTime = datetime.datetime.now().strftime("% H:% M:% S")
                    file.write(strTime)
                    file.write(" :- ")
                    file.write(note)
                    setDiscussionValue("Eve: i wrote the note with date and time")
                    setDisplayValue("Speaking...")
                    speak("sir,i wrote the note with date and time")
                else:
                    file.write(note)

            elif "show note" in self.query:
                setDiscussionValue("Eve: Opening notes")
                setDisplayValue("Speaking...")
                speak("opening Notes")
                file = open("eve.txt", "r")
                print(file.read())
                setDiscussionValue(f"Eve: {file.read(6)}")
                setDisplayValue("Speaking...")
                speak(file.read(6))
            # ---------------To search on google with voice input ---------------
            elif "open google" in self.query:
                setDiscussionValue("Eve: what should i search on google")
                setDisplayValue("Speaking...")
                speak("sir,  what should i search on google")
                cn = self.takecommand().lower()
                webbrowser.open(f"{cn}")
            # ---------------To what'sapp message---------------
            elif "send a whatsapp message" in self.query:
                setDiscussionValue("Eve: please enter the user phone number correctly.")
                setDisplayValue("Speaking...")
                speak("master please enter the user phone number correctly.")
                number = input("enter username here:")
                setDiscussionValue("Eve: what should i send")
                setDisplayValue("Speaking...")
                speak("master,  what should i send")
                cn = self.takecommand().lower()
                #speak("At what time i can send this message")
                #t1 = input("enter time in hour:")
                #t2 = input("enter time in minutes:")
                kit.sendwhatmsg(f"+91{number},{cn}", 11,12)
                time.sleep(120)
                setDiscussionValue("Eve: message has been sent")
                setDisplayValue("Speaking...")
                speak("message has been sent")
            # ---------------To play songs on you tube---------------
            elif "play songs on youtube" in self.query:
                setDiscussionValue("Eve: which song would you like to play")
                setDisplayValue("Speaking...")
                speak("sir,  which song would you like to play")
                cn = self.takecommand().lower()
                kit.playonyt(f"{cn}")
            # ---------------To tell jokes---------------
            elif "tell me a joke" in self.query:
                joke = pyjokes.get_joke()
                setDiscussionValue(f"Eve: here you go.. {joke}")
                setDisplayValue("Speaking...")
                speak(joke)
                return joke
            # ---------------To find latest news---------------
            elif "tell me news" in self.query:
                setDiscussionValue("Eve: please wait while,fetching the latest news")
                setDisplayValue("Speaking...")
                speak("please wait master,fetching the latest news")
                news()

            # ---------------To switch wimdows---------------
            elif "switch window" in self.query:
                pyautogui.keyDown("alt")
                pyautogui.press("tab")
                time.sleep(1)
                pyautogui.keyUp("alt")

            # ---------------To Hide or visible files---------------
            elif "hide all filse" in self.query or "hide this folder" in self.query or "visible for everyone" in self.query:
                speak("master please tell me you want to hide this folder or make it visible for everyone")
                condition = self.takecommand().lower()
                if "hide" in condition:
                    os.system("attrib +h /s /d")  # os module
                    speak("master,all the files in this folder are now hidden.")

                elif "visible" in condition:
                    os.system("attrib -h /s /d")
                    speak("master,all the files in this folder are now visible to everyone.i wish you are taking")

                elif "leave it" in condition or "leave for now" in condition:
                    speak("ok sir")
                    speak("master, do you have any other work")
            # ---------------To check internet speed---------------
            elif "internet speed" in self.query:
                # st = Speedtest.speedtest()
                # d1 = st.download()
                # up = st.upload()
                try:
                    os.system('cmd /k "speedtest"')
                except:
                    speak("there is no internet connection")
                speak("master, do you have any other work")
            # ---------------To send message---------------
            elif "send message" in self.query:
                speak("sir what should i say")
                msz = self.takecommand()
                from twilio.rest import Client

                account_sid = 'ACc8a67f5dfb58efc6ff1078844418bd4a'
                auth_token = '2005bfd570a39841f7334b7b0fdaed92'

                client = Client(account_sid, auth_token)
                client = Client(account_sid, auth_token)

                message = client.messages \
                    .create(
                    body=msz,
                    from_='+19144854479',
                    to='+919360193155'
                )
                speak("master, message has been sent")
                speak("Do you have any other work")
            # ---------------To take screenshoot---------------
            elif "take screenshot" in self.query or "screenshot" in self.query:
                speak("master,please tell me the name for this screenshot file")
                name = self.takecommand().lower()
                speak("please master hold the screen for few seconds, i am taking screenshot")
                time.sleep(3)
                img = pyautogui.screenshot()
                img.save(f"{name}.png")
                speak(
                    "i am done mastre, the screenshot is saved in our main folder.  now i am ready for next command master ")
                speak("master, do you have any other work")
                        # ---------------To perform operation------------------
            elif "shut down the system" in self.query:
                os.system("shutdown /s /t 5")
            elif "restart the system" in self.query:
                os.system("shutdown /r /t 5")
            elif "sleep the system" in self.query:
                os.system("rundll32.exe powrprof.dll,SetSuspendState 0,1,0")
            # ---------------To chech Instagram Profile------------------
            elif "instagram profile" in self.query or "profile on instragram" in self.query:
                speak("master please enter the user name correctly.")
                name = input("enter username here:")
                webbrowser.open(f"www.instagram.com/{name}")
                speak(f"sir here is the profile of the user {name}")
                time.sleep(5)
                speak("master would you like to download profile picture of this account.")
                condition = self.takecommand().lower()
                if "yes" or "download" in condition:
                    mod = instaloader.Instaloader()
                    mod.download_profile(name, profilr_picture_only=True)
                    speak("i am done master,profile picture is saved in our main folder.now i am ready")
                else:
                    pass
                speak("master, do you have any other work")
            # --------------To set alaram------------------
            elif "set alarm" in self.query:
                nn = int(datetime.datetime.now().hour)
                if nn == 22:
                    music_dir = 'E:\\music'
                    songs = os.listdir(music_dir)
                    os.startfile(os.path.join(music_dir, songs[0]))
                speak("master, do you have any other work")
            # --------------To set timer------------------
            elif 'timer' in self.query or 'stopwatch' in self.query:
                speak("For how many minutes?")
                timing = self.takeCommand()
                timing = timing.replace('minutes', '')
                timing = timing.replace('minute', '')
                timing = timing.replace('for', '')
                timing = float(timing)
                timing = timing * 60
                speak(f'I will remind you in {timing} seconds')

                time.sleep(timing)
                speak('Your time has been finished sir')
                speak("master, do you have any other work")
            # --------------To find my location using IP address------------------
            elif "where i am" in self.query or "where we are" in self.query:
                speak("wait sir,let me check")
                try:

                    location = self.query
                    speak(location)
                    webbrowser.open("https://www.google.com/maps/d/u/0/embed?mid=1EKrvpydeECY7QwBRk_IUBcax79Y&msa=0&hl=en&ie=UTF8&ll=37.24165301698757%2C-90.96897751171784&spn=0.077758%2C0.181103&output=embed&z=16" + location + "")
                except Exception as e:
                    speak("Sorry master due to network issue i am not able to find where we are.")
                    pass
                    speak("master, do you have any other work")
                # --------------To send email with file attachment and message------------------
            elif "open my email" in self.query:
                speak("opening email..")
                webbrowser.open("https://mail.google.com/mail/u/0/#inbox")
                speak("master, do you have any other work")
            elif "send a email" in self.query:
                setDiscussionValue("Eve: what should i send")
                setDisplayValue("Speaking...")
                speak("master what should i send")
                self.query = self.takecommand().lower()
                if "send a file" in self.query:
                    email = 'sksathish592001@gmail.com'  # Your email
                    password = 'sksathish@12'  # Your email account password
                    setDiscussionValue("Eve: what should i send")
                    setDisplayValue("Speaking...")
                    speak("master please say the user email-id correctly.")
                    send_to_email = fmail
                    #send_to_email = 'santhoshpoornachandrankvp@gmail.com'  # Whom you are sending the message to
                    setDiscussionValue("Eve: okay master, what is the subject for this email")
                    setDisplayValue("Speaking...")
                    speak("okay master, what is the subject for this email")
                    self.query = self.takecommand().lower()
                    subject = self.query  # The Subject in the email
                    setDiscussionValue("Eve: and master, what is the message for this email")
                    setDisplayValue("Speaking...")
                    speak("and master, what is the message for this email")
                    self.query2 = self.takecommand().lower()
                    message = self.query2  # The message in the email
                    setDiscussionValue("Eve: master please enter the correct path of the file into the shell")
                    setDisplayValue("Speaking...")
                    speak("master please enter the correct path of the file into the shell")
                    file_location = input("please enter the path here")  # The File attachment in the email
                    setDiscussionValue("Eve: please wait,i am sending email now")
                    setDisplayValue("Speaking...")
                    speak("please wait,i am sending email now")

                    msg = MIMEMultipart()
                    msg['From'] = email
                    msg['To'] = send_to_email
                    msg['Subject'] = subject

                    msg.attach(MIMEText(message, 'plain'))

                    # Setup the attachment
                    filename = os.path.basename(file_location)
                    attachment = open(file_location, "rb")
                    part = MIMEBase('application', 'octet-stream')
                    part.set_payload(attachment.read())
                    encoders.encode_base64(part)
                    part.add_header('Content-Disposition', "attachment; filename= %s" % filename)

                    # Attach the attachment to the MIMEMultipart object
                    msg.attach(part)
                    server = smtplib.SMTP('smtp.gmail.com', 587)
                    server.starttls()
                    server.login(email, password)
                    text = msg.as_string()
                    server.sendmail(email, send_to_email, text)
                    server.quit()
                    setDiscussionValue("Eve: email has been sent")
                    setDisplayValue("Speaking...")
                    speak("email has been sent")

                elif"send a message" in self.query:
                    email = 'sksathish592001@gmail.com' # Your email
                    password = 'sksathish@12'  # Your email account password
                    setDiscussionValue("Eve: please say the user email-id correctly.")
                    setDisplayValue("Speaking...")
                    speak("master please say the user email-id correctly.")
                    send_to_email = input(fmail)
                    #send_to_email = 'santhoshpoornachandrankvp@gmail.com'  # Whom you are sending the message to
                    message = self.query  # The message in the email

                    server = smtplib.SMTP('smtp.gmail.com', 587)  # Connect to the server
                    server.starttls()  # Use TLS
                    server.login(email, password)  # Login to the email server
                    server.sendmail(email, send_to_email, message)  # Send the email
                    server.quit()  # Logout of the email server
                    setDiscussionValue("Eve: email has been sent")
                    setDisplayValue("Speaking...")
                    speak("email has been sent")
                else:
                    speak("sry master i am unable to send this email")
                speak("master, do you have any other work")
            elif"read pdf" in self.query:
                pdf_reader()
                speak("master, do you have any other work")
            elif"covid" in self.query:
                speak("master please say  your country.")
                country = self.takecommand().lower()
                coronaVirus(country)
                speak("master, do you have any other work")
            elif 'quit' in self.query:
                speak("OK Sir, I am terminating myself in  three seconds")
                time.sleep(0.5)
                speak("three")
                time.sleep(1)
                speak("two")
                time.sleep(1)
                speak("one")
                quit()
            elif "weather" in self.query:
                owm = pyowm.OWM('api-key')  # open weather map API key
                # current weather forecast
                loc = owm.weather_at_place(city)
                weather = loc.get_weather()
                # status
                status = weather.get_detailed_status()
                var.set(f'{status} in {city}')
                window.update()
                speak(f'{status} in {city}')
                # temperature
                temp = weather.get_temperature(unit='celsius')
                for key, val in temp.items():
                    if key == 'temp':
                        var.set(f'{val} degree celcius')
                        window.update()
                        speak(f"current temperature is {val} degree celcius")
                # humidity, wind, rain, snow
                humidity = weather.get_humidity()
                wind = weather.get_wind()
                var.set(f'{humidity} grams per cubic meter')
                window.update()
                speak(f'humidity is {humidity} grams per cubic meter')
                var.set(f'wind {wind}')
                window.update()
                speak(f'wind {wind}')
                # sun rise and sun set
                sr = weather.get_sunrise_time(timeformat='iso')
                ss = weather.get_sunset_time(timeformat='iso')
                var.set(sr)
                window.update()
                speak(f'SunRise time is {sr}')
                var.set(ss)
                window.update()
                speak(f'SunSet time is {ss}')
                # clouds and rain
                loc = owm.three_hours_forecast(city)
                clouds = str(loc.will_have_clouds())
                rain = str(loc.will_have_rain())
                if clouds == 'True':
                    var.set("It may have clouds in next 5 days")
                    window.update()
                    speak("It may have clouds in next 5 days")
                else:
                    var.set("It may not have clouds in next 5 days")
                    window.update()
                    speak("It may not have clouds in next 5 days")
                if rain == 'True':
                    var.set("It may rain in next 5 days")
                    window.update()
                    speak("It may rain in next 5 days")
                else:
                    var.set("It may not rain in next 5 days")
                    window.update()
                    speak("It may not rain in next 5 days")
                speak("master, do you have any other work")
            else:
             speak("master, do you have any other work")

startExecution  = MainThread()
# class Main(QMainWindow):
#     def _init_(self):
#         super()._init_()
        # self.ui = Ui_MainWindow()
        # self.ui.setupUi(startExecution)
#         self.ui.pushButton.clicked.connect(self.startTask)
#
#         self.ui.pushButton_2.clicked.connect(self.close)
#     def startTask(self):
#         self.ui.movie = QtGui.QMovie("D:/gif/free-video-3045163.jpg")
#         self.ui.label.setMovie(self.ui.movie)
#         self.ui.movie.start()
#         self.ui.movie = QtGui.QMovie("D:/gif/201687.gif")
#         self.ui.label_2.setMovie(self.ui.movie)
#         self.ui.movie.start()
#         self.ui.movie = QtGui.QMovie("D:/gif/giphy.gif")
#         self.ui.label_3.setMovie(self.ui.movie)
#         self.ui.movie.start()
#         self.ui.movie = QtGui.QMovie("D:/gif/tumblr_nmzc9biHny1rhfekio1_500.gif")
#         self.ui.label_5.setMovie(self.ui.movie)
#         self.ui.movie.start()
#         self.ui.movie = QtGui.QMovie("D:/gif/SeriousFatherlyDalmatian-max-1mb.gif")
#         self.ui.label_6.setMovie(self.ui.movie)
#         self.ui.movie.start()
#         self.ui.movie = QtGui.QMovie("D:/gif/Inkedd7de2e0da1ebdb9b9a16142bda815951.jpg")
#         self.ui.label_7.setMovie(self.ui.movie)
#         self.ui.movie.start()
#         self.ui.movie = QtGui.QMovie("D:/gif/hud-1.gif")
#         self.ui.label_8.setMovie(self.ui.movie)
#         self.ui.movie.start()
#         self.ui.movie = QtGui.QMovie("D:/gif/Tech-buttons5-collection.png")
#         self.ui.label_9.setMovie(self.ui.movie)
#         self.ui.movie.start()
#         self.ui.movie = QtGui.QMovie("D:/gif/Inkedd7de2e0da1ebdb9b9a16142bda815951.jpg")
#         self.ui.label_10.setMovie(self.ui.movie)
#         self.ui.movie.start()
#         self.ui.movie = QtGui.QMovie("D:/gif/tumblr_o7vs1zNO341runoqyo1_540.gif")
#         self.ui.label_11.setMovie(self.ui.movie)
#         self.ui.movie.start()
#         self.ui.movie = QtGui.QMovie("D:/gif/00545cb7179c504433d4c8f5e845f286.gif")
#         self.ui.label_12.setMovie(self.ui.movie)
#         self.ui.movie.start()
#         self.ui.movie = QtGui.QMovie("D:/gif/81e94629734355.56016a05a166b.gif")
#         self.ui.label_13.setMovie(self.ui.movie)
#         self.ui.movie.start()
#         self.ui.movie = QtGui.QMovie("D:/gif/503cff29734355.56016a06899c4.gif")
#         self.ui.label_14.setMovie(self.ui.movie)
#         self.ui.movie.start()
#         self.ui.movie = QtGui.QMovie("D:/gif/1634624012763.gif")
#         self.ui.label_15.setMovie(self.ui.movie)
#         self.ui.movie.start()
#         timer = QTimer(self)
#         timer.timeout.connect(self.showTime)
#         timer.start(1000)
#         startExecution.start()
#     def user(self,s):
#         self.ui.textEdit.setText(s)
#     def showTime(self):
#         current_time = QTime.currentTime()
#         current_date = QDate.currentDate()
#         label_time = current_time.toString('hh:mm:ss')
#         label_date = current_date.toString(Qt.ISODate)
#         self.ui.textBrowser.setText(label_time)
#         self.ui.textBrowser_2.setText(label_date)
#
# app = QApplication(sys.argv)
# eve = Main()
# eve.show()
# exit(app.exec_())

class Main(QMainWindow):
    def _init_(self):
        super()._init_()
        # self.ui = Ui_MainWindow()
        UI.setupUi(self)
        UI.Btn_text_mode.clicked.connect(self.e_mail)


        # Remove window title bar
        self.setWindowFlags(QtCore.Qt.FramelessWindowHint)

        # Set main window to transparent
        self.setAttribute(QtCore.Qt.WA_TranslucentBackground)

        # Shadow effect style
        self.shadow = QGraphicsDropShadowEffect(self)
        self.shadow.setBlurRadius(50)
        self.shadow.setXOffset(0)
        self.shadow.setYOffset(0)
        self.shadow.setColor(QColor(0, 92, 157, 550))

        ##########################################################
        # Apply shadow to cental widget
        UI.centralwidget.setGraphicsEffect(self.shadow)

        ######################################################################
        # --------------------- Set window Icon
        # -- This icon and title will not appear on our app main window
        # because we removed the title bar
        # self.setWindowIcon(QtGui.QIcon(":/icons/icons/github.svg"))
        # self.setWindowTitle("MODERN UI")

        ############################################################
        # -------- Window Size grip to resize window
        # QSizeGrip(self.ui.size_grip)

        ###############################################
        # ----------------- Minimize window
        UI.Btn_MINIMISE.clicked.connect(lambda: self.showMinimized())

        # ----------------- Restore/Maximize window
        UI.Btn_MAXIMISE.clicked.connect(lambda: self.restore_or_maximize_window())

        # ----------------- Close window
        UI.Btn_CLOSE.clicked.connect(lambda: self.close())
        UI.Btn_EXIT.clicked.connect(lambda: self.close())

        # start button functionality
        UI.Btn_start.clicked.connect(self.startTask)
        # self.ui.pushButton_2.clicked.connect(self.close)

        # TOGGLE/BURGER MENU
        ######################################################
        UI.Btn_toggle.clicked.connect(lambda: self.ToggleAnimation(150, True))

        # PAGES
        ######################################################
        # PAGE HOME
        UI.Btn_HOME.clicked.connect(lambda: UI.stackedWidget.setCurrentWidget(UI.page_home))

        # PAGE ADVANCE
        UI.Btn_ADVANCE.clicked.connect(
            lambda: UI.stackedWidget.setCurrentWidget(UI.page_advance))

        # PAGE ABOUT
        UI.Btn_ABOUT.clicked.connect(
            lambda: UI.stackedWidget.setCurrentWidget(UI.page_about))

    def e_mail(self):
        fmail = self.Btn_audio_mode.text()
    ##################################################
    # Add mouse events  to the window
    ###############################################
    def mousePressEvent(self, event):
        # Get the current position of the mouse
        self.clickPosition = event.globalPos()
        # We will use this value to move the mouse window

    def ToggleAnimation(self, maxWidth, enable):
        if enable:
            # GET WIDTH
            width = UI.frame_left_menu.width()
            maxExtend = maxWidth
            standard = 40

            # SET MAX WIDTH
            if width == 40:
                widthExtended = maxExtend
                UI.Btn_HOME.setText("   HOME")
            else:
                widthExtended = standard
                UI.Btn_HOME.setText("")

            # ANIMATION
            self.animation = QPropertyAnimation(UI.frame_left_menu, b"minimumWidth")
            self.animation.setDuration(400)
            self.animation.setStartValue(width)
            self.animation.setEndValue(widthExtended)
            self.animation.setEasingCurve(QtCore.QEasingCurve.InOutQuart)
            self.animation.start()

            if width == 40:
                UI.Btn_HOME.setText("   HOME")
                UI.Btn_ADVANCE.setText("   ADVANCE")
                UI.Btn_ABOUT.setText("   ABOUT")
                UI.Btn_EXIT.setText("   EXIT")
            else:
                UI.Btn_HOME.setText("")
                UI.Btn_ADVANCE.setText("")
                UI.Btn_ABOUT.setText("")
                UI.Btn_EXIT.setText("")

    def restore_or_maximize_window(self):
        # if window is maximized
        if self.isMaximized():
            self.showNormal()
        else:
            self.showMaximized()

    def startTask(self):

        # UI.movie = QtGui.QMovie("gif\\45.gif")
        # UI.label_4.setMovie(UI.movie)
        # UI.movie.start()

        # UI.movie = QtGui.QMovie("gif\\43.gif")
        # UI.label_6.setMovie(UI.movie)
        # UI.movie.start()
        UI.movie = QtGui.QMovie("gif\\44.gif")
        UI.label_44.setMovie(UI.movie)
        UI.movie.start()

        UI.movie = QtGui.QMovie("gif\\17.gif")
        UI.globe.setMovie(UI.movie)
        UI.movie.start()

        UI.movie = QtGui.QMovie("gif\\36.gif")
        UI.label_31.setMovie(UI.movie)
        UI.movie.start()

        UI.movie = QtGui.QMovie("gif\\33.gif")
        UI.label_33.setMovie(UI.movie)
        UI.movie.start()

        UI.movie = QtGui.QMovie("gif\\200.gif")
        UI.label_23.setMovie(UI.movie)
        UI.movie.start()

        UI.movie = QtGui.QMovie("gif\\nice.gif")
        UI.label_nice.setMovie(UI.movie)
        UI.movie.start()

        UI.movie = QtGui.QMovie("gif\\22.gif")
        UI.label_22.setMovie(UI.movie)
        UI.movie.start()

        UI.movie = QtGui.QMovie("gif\\51.gif")
        UI.label_51.setMovie(UI.movie)
        UI.movie.start()

        UI.movie = QtGui.QMovie("gif\\48.gif")
        UI.label_48.setMovie(UI.movie)
        UI.movie.start()

        UI.movie = QtGui.QMovie("gif\\55.gif")
        UI.label_36.setMovie(UI.movie)
        UI.movie.start()

        # Update Time every 1000 mili.
        timer = QTimer(self)
        timer.timeout.connect(self.showTime)
        timer.start(1000)
        startExecution.start()

    def showTime(self):
        current_time = QTime.currentTime()
        current_date = QDate.currentDate()
        label_time = current_time.toString('hh:mm:ss')
        label_date = current_date.toString(Qt.ISODate)

        UI.time.setText(label_time)
        UI.date.setText(label_date)


app = QApplication(sys.argv)
eve = Main()
eve.show()
exit(app.exec_())