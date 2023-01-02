import speech_recognition as sr
import pyttsx3
import pywhatkit
import datetime
import wikipedia
import pyjokes
import time
import sys
import os
import random

listener = sr.Recognizer()
engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)
commands_dict = {}


def talk(text):
    print(text)
    engine.say(text)
    engine.runAndWait()


def take_command():
    try:
        with sr.Microphone() as source:
            print('listening...')
            voice = listener.listen(source)
            command = listener.recognize_google(voice)
            command = command.lower()
            if 'alexa' in command:
                command = command.replace('alexa', '')
                print(command)
    except:
        command = ''
    return command

def person(name):
    name = name.replace('who the heck is', '')
    info = wikipedia.summary(name, 1)
    talk(info)
commands_dict['who the heck is'] = person

def greeting(name):
    name = name.replace('hi my name is', '')
    talk('Hi, nice to meet you' + name)
commands_dict['hi my name is'] = greeting

def run_alexa():
    command = take_command()
    found = False
    for keyword in commands_dict:
        if keyword in command: 
            try:
                commands_dict[keyword]()
            except TypeError: #take function with 0 or 1 parameters
                commands_dict[keyword](command)
            found = True
            talk('Anthing else you wanna say?')
    if not found:
        commands_dict['repeat_cmd']()
    time.sleep(1) #brief pause between commands

def profile():
    talk("I'm Alexa, GDSC virtual assistant.")
commands_dict['what is your name'] = profile

def play(command):
    song=command.replace('play','')
    talk('playing' +song)
    pywhatkit.playonyt(song)
commands_dict['play'] = play

def current_time():
    time = datetime.datetime.now().strftime('%I:%M %p')
    talk('Current time is ' + time)
commands_dict['time'] = current_time

def repeat_cmd():
    talk('Please say the command again.')
commands_dict['repeat_cmd'] = repeat_cmd

def bye():
    talk('Goodbye.')
    sys.exit()
commands_dict['bye'] = bye

def date():
    talk("Sorry, I have a headache today")
commands_dict['date'] = date

def whatToEat():
    food = ['Proton', "TNB", "Vmall", "Mas", "Petronas", "Grant", "SD", "TM", "YAB"]
    talk("I'd recommend " + random.choice(food))
commands_dict['eat'] = commands_dict['food'] = whatToEat

def joke():
    talk(pyjokes.get_joke())
commands_dict['joke'] = joke

def write_a_note():
    talk("What should i write?")
    note = take_command()
    file = open('jarvis.txt', 'w')
    talk("Should i include date and time?")
    snfm = take_command()
    if 'yes' in snfm or 'sure' in snfm:
        strTime = datetime.datetime.now().strftime("%d/%m/%Y(%a) %H:%M:%S")
        file.write(strTime + " :- ")
    file.write(note)
    file.close()
    talk("Note written.")
commands_dict['write a note'] = write_a_note

def single():
    talk("I'm in a relationship with Google.")
commands_dict['single'] = single

def assignment():
    talk("Go ask google, he know more than me.")
commands_dict['assignment'] = commands_dict['homework'] = assignment

def open_slide():
    os.startfile(r'C:\Users\AH CHUN\Downloads\GDSC\HOPE\Game\Create-a-Virtual-Assistant-with-Python\Promotion Slide.pdf')
    sys.exit()
commands_dict['gdsc'] = open_slide

def age():
    talk("I'm always 18")
commands_dict['old'] = commands_dict['age'] = age


talk('Welcome to GDSC. How can I help you?')
while True:
    run_alexa()