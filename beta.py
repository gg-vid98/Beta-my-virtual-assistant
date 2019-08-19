import pyttsx3
import datetime
import speech_recognition as sr
import wikipedia
import webbrowser
import os
import smtplib
import random
import requests
import json
from joke.jokes import *
from joke.quotes import *
engine = pyttsx3.init('sapi5')
voices=engine.getProperty('voices')
engine.setProperty('voice',voices[1].id)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()
def wishMe():
    hour=int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speak("Good Morning")
    elif hour>=12 and hour<18:
        speak(' good afternoon')
    else:
        speak('good evening')
   
    speak('Hello, how can I help, I am beta..')
def takeCommand():
    #microphone input from user and string output
    r=sr.Recognizer()
    with sr.Microphone() as source:
        print('Listening')
        r.pause_threshold=0.5 #non speaking time b4 phase ends
        #r.energy_threshold=200
        #r.phrase_threshold=0.1
        audio=r.listen(source)
    try:
        print("recognizing")
        query=r.recognize_google(audio,language='en-in')
        print("user said",query)
    except Exception as e:
       #print(e)
       print("say again")
       return "None"
    return query 
def sendEmail(to,content):
    server=smtplib.SMTP('smtp.gmail.com',587)
    server.ehlo()
    server.starttls()
    server.login('your-mail','passwd')
    server.sendmail('your-mail',to,content)

if __name__=='__main__':
    wishMe()
    while(True):
    #if 1:  
        query=takeCommand().lower()
        if 'wikipedia' in query:
            speak("searching wikipedia")
            query=query.replace("wikipedia","")
            results=wikipedia.summary(query,sentences=2)
            speak("According to wikipedia")
            speak(results)
        elif 'open youtube' in query:
            webbrowser.open("youtube.com")
        elif 'open google' in query:
            webbrowser.open("google.com")
        elif 'open hackerrank' in query:
            webbrowser.open("hackerrank.com")
        elif 'play music' in query:
            music_dir="C:\\Users\\Vidya\\Desktop\\music"
            songs=os.listdir(music_dir)
            s=random.randint(0,len(songs)-1)
            os.startfile(os.path.join(music_dir,songs[s]))
        elif 'the time' in query:
            strTime=datetime.datetime.now().strftime("%H:%M:%S")
            speak(f"time is{strTime}")
        elif 'open chrome' in query: 
            codePath="C:\\Program Files (x86)\\Google\\Chrome\\Application\\chrome.exe"
            os.startfile(codePath)
        elif 'send mail' in query:
            try:
                speak("what should I say")
                content=takeCommand()
                to="receiver mail"
                sendEmail(to,content)
            except Exception as e:
                print(e)
                speak("Sorry unable to send")
        elif 'give an intro' in query:
            speak('I am beta as awesome as you . A virtual assistant. Ask me anything and I am here to help. I can sing, speak and send mails')
        elif 'thank you' in query:
            speak(" Welcome")
        
       
       
        elif 'read news' in query:
            url = ('https://newsapi.org/v2/top-headlines?country=in&apiKey=560bb7f7ccdd44f78893006ea612ce75')
            response = requests.get(url)
            text = response.text
            my_json = json.loads(text)
            for i in range(0, 5):
                speak(my_json['articles'][i]['title'])   
        elif 'joke' in query:
            speak(geek())   
        elif 'are you there' in query or 'are you able to hear me' in query:
            speak('yeah I am  just feeling  a bit slow today')
        elif 'quote' in query:
            speak(quotesondesign())
        elif 'bye' in query:
            speak('Have a good day')
            break
            
        
        

