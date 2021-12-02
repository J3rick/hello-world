# Module Importing
import speech_recognition as sr
import pyttsx3
import pywhatkit
import datetime
import wikipedia

listener = sr.Recognizer()
engine = pyttsx3.init() #initializing engine
voices = engine.getProperty('voices') #Allows you to get all the voices that the python package provides
engine.setProperty('voice', voices[1].id) # Setting voice of alexa to female

def talk(text):
    engine.say(text) #
    engine.runAndWait()

def take_command():
    try:
        with sr.Microphone() as source: #source of command
            print ('listening...')
            voice = listener.listen(source) #listening for source from microphone
            command = listener.recognize_google(voice) #passes voice to google api to get text
            command = command.lower() #Makes command to lower case
            if 'kinara' in command: #If Kinara is mentioned in the command
                command = command.replace('kinara', '') #this way, the name of the AI helper will not be entered into the search query
                print(command)
    except:
        pass
    return command

def run_kinara():
    command = take_command()
    print (command)
    if 'play' in command:
        song = command.replace('play', '') #Removes the word "play" from command
        talk('playing ' + song ) #Kinara says playing 
        pywhatkit.playonyt(song) #Proceeds to play
    elif 'time' in command:
        time = datetime.datetime.now().strftime('%H:%M %p')
        talk('Current time is ' + time)
    elif 'who the heck is' in command:
        person = command.replace('who the heck is', '')
        info = wikipedia.summary(person, 1)
        print(info)
        talk(info)
    else:
        talk('Please say the command again.')

while True:
    run_kinara()