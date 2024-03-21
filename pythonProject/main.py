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
    text = takeCommand()
    print(text)
    if 'joke' in text:
        sayJokes()
    elif 'play' in text:
        song=text.replace('play',"")
        talk('playing'+song)
        pwk.playonyt(song)
    elif 'time' in text:
        talk(datetime.now().strftime("%H:%M"))
    elif 'date' in text:
        talk(date.today())
    elif "who the heck is" in text:
        person = text.replace('who the heck is','')
        info = wikipedia.summary(person,5)
        talk(info)
    elif 'are you single' in text:
       talk("sorry i am in a relationship with wifi")
    elif 'who are you' in text:
        talk("my name is vexi i am a virtual assistant made by K1NG")
    else:
        talk("say the command again")
    while True:
        run()

run()
