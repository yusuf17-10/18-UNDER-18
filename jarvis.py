import pyttsx3
from datetime import datetime
import speech_recognition as sr
import wikipedia
import webbrowser

engine = pyttsx3.init('sapi5')

voices = engine.getProperty('voices')

engine.setProperty('voice',voices[0].id)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def wishMe():
    hour = int(datetime.now().hour)
    if hour>=0 and hour<12:
        speak("Good Morning")

    elif hour>=12 and hour<18:
        speak("Good AfterNoon")

    else:
        speak("Good Evening")

    speak("I am Jarvis , Please tell me how can i help you")

def takeCommand():
    
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        
        r.pause_threshold = 1
        audio = r.listen(source,timeout=5,phrase_time_limit=3)

    try:
        print("Recognizing...")
        query = r.recognize_google(audio, language='en-in')
        print(f"User said: {query}\n")

    except Exception as e:
       
        print("Say that again please...")
        speak("Say that again please... so that i can help you")
        return "None"
    return query

if __name__ == "__main__":
    wishMe()
    x =datetime.now()
    speak("Type Y for Voice command and N to type command")

    speak("If You Want The information....Then Please Include wiki pidea in your voice for example : Sharuk Khan Wikipidea")
    print("If You Want The information....Then Please Include wiki pidea in your voice for example : Sharuk Khan Wikipidea")
    while True:
        choice=input("Type Y for Voice command and N to type command: ")
        if(choice=="y" or choice=="n" or choice=="N" or choice=="Y"):
            break
        else:
            print("Choose again. It should either y or n")

    while True:
        if(choice=="y" or choice=="Y"):
            query = takeCommand().lower()
        elif(choice=="n" or choice=="N"):
            query=input("")
            
        if 'wikipedia' in query:
            speak("Searching Wikipedia...")
            query=query.replace("wikipedia","")
            results = wikipedia.summary(query,sentences=2)
            speak("According to Wikipedia")
            print(results)
            speak(results)

        elif 'open youtube' in query:
            webbrowser.open("youtube.com")
        
        elif 'hi' in query:
            speak("hi how can i help you")

        elif "hello" in query:
            speak("Hello how can i help you")

        elif 'open google' in query:
            webbrowser.open("google.com")

        elif "quit" in query:
            speak("Thanks for using me!!")
            break

        elif "time" in query:
            current_time = x.strftime("%H:%M:%S") 
            print("Current Time =", current_time)
            hr = int(x.strftime("%H"))%12
            min = int(x.strftime("%M"))
            speak(f"The time is {hr} {min}")
        
        elif "create" in query:
            speak("Proud to say. I was developed by the student of white hat junior named V.Mohammad Yusuf")
        
        elif "who are you" in query:
            speak("I am Jarvis your virtual assistant how can i help you")
        


