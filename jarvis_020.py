'''
Author : Harsh Vishwakarma
Project : Virtual Assistant (Jarvis)
Version : 0.2.0
Desciption : This is version 0.1.0 and it can Perform some basic tasks like
             doesn't run not connected to internet,
             says command before every task,
             search in wikipedia,
             open youtube, google, stackoverflow, hackerrank, facebook, instagram
             plays music,
             tell about time,
             open sublime, visual code studio, 
             close itself on command
'''


import pyttsx3                          #pip install pyttsx3
import datetime                         #built-in module
import speech_recognition as sr         #pip install speechRecognition
import wikipedia                        #pip install wikipedia
import webbrowser                       #built-in module
import os                               # built-in module
import random                           # built-in module
import socket                           # built-in module

# Initializing Engine and Microsoft Speech API
engine = pyttsx3.init("sapi5")
voices = engine.getProperty("voices")
engine.setProperty("voice",voices[0].id)

# speak function
def speak(audio):
    engine.say(audio)
    engine.runAndWait()

# tell to both speak & print
def tell(audio):
    print(audio)
    speak(audio)

# To close the File
def isclose(x):
    if 'close' in x or 'stop' in x or 'exit' in x:
        tell("Bye Harsh")
        tell("Its time to go now")
        exit()
        
# Take command to Execute Something
def takecommand():  

    r = sr.Recognizer()
    with sr.Microphone() as source:
        tell("Listening....")
        r.pause_threshold = 1
        audio= r.listen(source)

    try:
        print("Recognizing....")
        query = r.recognize_google(audio,language = "en-in")
        tell(f"You Said : {query}\n")
            
    except Exception as e:
        
        tell("Can't Recognize..")
        tell("Please say that again")
        takecommand()
        return "None"
    return query

# Checks if Device is connected to Internet or Not
def is_connected():
    try:
        # connect to the host -- tells us if the host is actually
        # reachable
        socket.create_connection(("1.1.1.1", 53))
        return True
    except OSError:
        pass
    return False

# Listen only to get voice data
def listen():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print(".")
        r.pause_threshold = 1
        audio= r.listen(source)
    try:
        query = r.recognize_google(audio,language = "en-in")
        print(f"You said: {query}")            
    except Exception as e:
        return "None"
    return query


# Tasks to be Performed by Jarvis
def dotask(query):

     if 'wikipedia' in query:
         query = query.replace('wikipedia', '')
         result = wikipedia.summary(query, sentences=2)
         tell("According to Wikipedia....")
         tell(result)
     elif 'open youtube' in query :
         webbrowser.open("youtube.com")
     elif 'open google' in query:
         webbrowser.open("google.com")
     elif 'open facebook' in query:
         webbrowser.open("facebook.com")
     elif 'open instagram' in query:
         webbrowser.open("instagram.com")
     elif 'open stackoverflow' in query:
         webbrowser.open("stackoverflow.com")
     elif 'open hacker rank' in query:
         webbrowser.open("hackerrank.com")
     elif 'open code' in query:
         os.startfile(r'C:\Users\Lenovo\AppData\Local\Programs\Microsoft VS Code\Code.exe')
     elif 'open sublime' in query:
         os.startfile(r"C:\Program Files\Sublime Text 3\sublime_text.exe")
     elif 'open hacker rank' in query:
         webbrowser.open("hackerrank.com")
     elif 'open hacker rank' in query:
         webbrowser.open("hackerrank.com")
     elif 'who are you' in query:
         tell("I am Jarvis")
         tell("Virtual Assistant of Harsh Vishwakarma")
         tell("I am on Version 0.2.0")
         
     elif 'play music' in query:
         music_dir = r"F:\song listen"
         songs = os.listdir(music_dir)
         os.startfile(os.path.join(music_dir, songs[random.randint(0,len(songs))]))
     elif 'time' in query:
         time = datetime.datetime.now().strftime("%H:%M:%S")
         tell(f"Time is {time}")
     else:
         isclose(query)

    

        
        
# To wish me Everytime when the Application start
def wishme():
    hour = int(datetime.datetime.now().hour)
    if hour>=4 and hour<12:
        speak("Good Morning Harsh")
    elif hour>=12 and hour<17:
        speak("Good Afternoon Harsh")
    elif hour >= 17 and hour < 20:
        speak("Good Evening Harsh")
    else:
        speak("Heyyy Harsh")
    tell("I am Jarvis")
    tell("Your Assistant")
    tell("How may I help you")


if __name__ == '__main__':
    wishme()
    if(is_connected()):                   
        dotask(takecommand().lower())
        while 1:
            sound = listen().lower()
            if 'jarvis' in sound:
                query = takecommand().lower()
                dotask(query)
            else:
                isclose(sound)
    else:
        tell("Your System is Not Connected to Internet")
        tell("Hence I am  Unable to Recognize your Voice")
        tell("Please Connect to Internet")
        isclose("exit")
                
            
            
    
