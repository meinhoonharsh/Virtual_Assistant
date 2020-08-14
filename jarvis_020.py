'''
Author : Harsh Vishwakarma
Project : Virtual Assistant (Jarvis)
Version : 0.2.0
Desciption : This is version 0.1.0 and it can Perform some basic tasks like
             doesn't run not connected to internet,
             says command before every task,
             search in wikipedia,
             open youtube, google, stackoverflow, hackerrank, facebook, instagram
             plays song which was asked,
             plays random music,
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
    elif 'search' in query:
        query = query.replace('search for',"")
        query = query.replace('search', "")
        if 'youtube' in query:
            query = query.replace('in youtube', "")
            query = query.replace('on youtube', "")
            query = query.replace('youtube', "")
            tell("Searching on YouTube...")
            webbrowser.open(f"https://www.youtube.com/search?q={query}")
        else:
                query = query.replace('in google',"")
                query = query.replace('on google',"")
                query = query.replace('google',"")
                tell("Searching on Google...")
                webbrowser.open(f"https://www.google.com/search?q={query}")
    elif 'open' in query:
        query = query.replace('open','')
        if 'youtube' in query:
            tell("Opening Youtube...")
            webbrowser.open('youtube.com')
        elif 'google' in query:
            tell("Opening Google")
            webbrowser.open("google.com")
        elif 'facebook' in query:
            tell("Opening Facebook")
            webbrowser.open("facebook.com")
        elif 'instagram' in query:
            tell("Opening Instagram")
            webbrowser.open("instagram.com")
        elif 'stackoverflow' in query or 'stack overflow' in query:
            tell("Opening Stack Overflow")
            webbrowser.open("stackoverflow.com")
        elif 'hacker rank' in query or 'hackerrank' in query:
            tell("Opening Hacker Rank")
            webbrowser.open("hackerrank.com")
        elif 'code' in query:
            tell("Opening Visual Code Studio")
            os.startfile(r'C:\Users\Lenovo\AppData\Local\Programs\Microsoft VS Code\Code.exe')
        elif 'sublime' in query:
            tell("Opening Sublime Text 3")
            os.startfile(r"C:\Program Files\Sublime Text 3\sublime_text.exe")
        elif 'blog' in query:
            tell("Opening Your Blog Website")
            webbrowser.open("blog.harshvishwakarma.xyz")
        elif 'website' in query:
            tell("Opening Your Website")
            webbrowser.open("harshvishwakarma.xyz")
        else:
            tell(f"Can't Open {query}")
    elif 'play music' in query or 'play song' in query:
        query = query.replace('play music', '')
        query = query.replace('play song', '')
        query = query.strip()
        music_dir = r"F:\song listen"
        songs = os.listdir(music_dir)
        # print(f"Query :{query}")
        x=0
        if query=="":
            randmusic = songs[random.randint(0, len(songs))]
            tell(f"PLaying {randmusic}")
            os.startfile(os.path.join(music_dir, randmusic))
            x=1
        else:
            for i in songs:
                # print(f"Song : {i}")                
                if query in i.lower():
                    tell(f"Playing Song {query}")
                    os.startfile(os.path.join(music_dir, i))
                    x=1
                    break
        
        if x==0:
            tell(f"No Song name {query} in your Directory")
    elif 'who are you' in query:
         tell("I am Jarvis")
         tell("Virtual Assistant of Harsh Vishwakarma")
         tell("I am on Version 0.2.0")


    # For telling the time
    elif 'time' in query:
         time = datetime.datetime.now().strftime("%H:%M:%S")
         tell(f"Time is {time}")
    else:
         isclose(query)      



    #  if 'wikipedia' in query:
    #      query = query.replace('wikipedia', '')
    #      result = wikipedia.summary(query, sentences=2)
    #      tell("According to Wikipedia....")
    #      tell(result)
    #  elif 'open youtube' in query :
    #      webbrowser.open("youtube.com")
    #  elif 'open google' in query:
    #      webbrowser.open("google.com")
    #  elif 'open facebook' in query:
    #      webbrowser.open("facebook.com")
    #  elif 'open instagram' in query:
    #      webbrowser.open("instagram.com")
    #  elif 'open stackoverflow' in query:
    #      webbrowser.open("stackoverflow.com")
    #  elif 'open hacker rank' in query:
    #      webbrowser.open("hackerrank.com")
    #  elif 'open code' in query:
    #      os.startfile(r'C:\Users\Lenovo\AppData\Local\Programs\Microsoft VS Code\Code.exe')
    #  elif 'open sublime' in query:
    #      os.startfile(r"C:\Program Files\Sublime Text 3\sublime_text.exe")
    #  elif 'open hacker rank' in query:
    #      webbrowser.open("hackerrank.com")
    #  elif 'open hacker rank' in query:
    #      webbrowser.open("hackerrank.com")
    #  elif 'who are you' in query:
    #      tell("I am Jarvis")
    #      tell("Virtual Assistant of Harsh Vishwakarma")
    #      tell("I am on Version 0.2.0")
         
    #  elif 'play music' in query:
    #      music_dir = r"F:\song listen"
    #      songs = os.listdir(music_dir)
    #      os.startfile(os.path.join(music_dir, songs[random.randint(0,len(songs))]))
    #  elif 'time' in query:
    #      time = datetime.datetime.now().strftime("%H:%M:%S")
    #      tell(f"Time is {time}")
    #  else:
    #      isclose(query)

    

        
        
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
                
            
            
    
