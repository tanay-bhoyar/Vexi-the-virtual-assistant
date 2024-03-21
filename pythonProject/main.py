import speech_recognition as sr
import pyttsx3 as p
from dadjokes import Dadjoke
import pywhatkit as pwk
from datetime import datetime
from datetime import date
import wikipedia

listener = sr.Recognizer()
engine = p.init()
dadjoke = Dadjoke()
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)
mic = sr.Microphone(device_index=1)



def talk(text):
    engine.say(text)
    engine.runAndWait()

def takeCommand():
    with mic as source:
        print("Listening....")

        audio=listener.listen(source)

        try:
            text=listener.recognize_google(audio)
            text=text.lower()
            if 'vexi' in text:
                text=text.replace("vexi","")
                print(text)
        except sr.UnknownValueError:
            print("Sorry")
        except sr.RequestError as e:
            pass

        return text

def sayJokes():
    x=dadjoke.joke
    talk(x)

def run():
    talk("what can i do for you")
    command = takeCommand()
    print(command)
    if 'joke' in command:
        sayJokes()
    elif 'play' in command:
        song=command.replace('play',"")
        talk('playing'+song)
        pwk.playonyt(song)
    elif 'time' in command:
        talk(datetime.now().strftime("%H:%M"))
    elif 'date' in command:
        talk(date.today())
    elif "who the heck is" in command:
        person = command.replace('who the heck is','')
        info = wikipedia.summary(person,5)
        talk(info)
    elif 'are you single' in command:
       talk("sorry i am in a relationship with wifi")
    elif 'who are you' in command:
        talk("my name is vexi i am a virtual assistant made by K1NG")
    else:
        talk("say the command again")
    while True:
        run()

run()