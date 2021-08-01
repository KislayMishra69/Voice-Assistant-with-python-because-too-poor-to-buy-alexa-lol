#I'll be naming it Jarvis...because it sounds cool. You can name it anything you want :D

# All the modules we'll be needing for this are as follows:-
import speech_recognition as sr
import pyttsx3
import pywhatkit
import datetime
import wikipedia
import webbrowser
import pyaudio
import os

# we create a variable 'listener' which will be our sr.Recognizer
listener = sr.Recognizer()
engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)

# Defining a talk function
def talk(text):
    engine.say(text)
    engine.runAndWait()

# Defining a take command function through which the AI will take commands
def take_command():
    try:
        with sr.Microphone() as source:
            print('listening...')
            voice = listener.listen(source)
            command = listener.recognize_google(voice)
            command = command.lower()
        
    except:
        pass
    return command

# Defining the commands and their output
def run_jarvis():
    command = take_command()
    print("Recognizing...")
    print(command)
# A command to play music on YouTube
    if 'play' in command:
        song = command.replace('play', '')
        talk('playing ' + song)
        pywhatkit.playonyt(song)

# A command to tell time
    elif 'time' in command:
        time = datetime.datetime.now().strftime('%I:%M %p')
        talk('Current time is ' + time)
        
# A command which will open youtube on google chrome
    elif 'youtube' in command:
        webbrowser.open("https://www.youtube.com/")
        talk("YouTube has been opened...") 
      
# A command which uses the Wikipedia module to get information about people from wikipedia
    elif 'who is' in command:
        person = command.replace('who is', '')
        info = wikipedia.summary(person, 1)
        print(info)
        talk(info)
        
# A command which will play...well..the best song (be surprised lol)
    elif 'best song' in command:
        webbrowser.open("https://www.youtube.com/watch?v=dQw4w9WgXcQ")
        talk("There you go")
        
# A command to open reddit
    elif 'reddit' in command:
        webbrowser.open("https://www.reddit.com/")
        talk("Opening Reddit...")


while True:
    run_jarvis()
