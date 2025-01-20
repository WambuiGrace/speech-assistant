import speech_recognition as sr
import time
from time import ctime
import webbrowser
import os
import playsound
import random
from gtts import gTTS

def get_audio(ask = False):
    r = sr.Recognizer()
    with sr.Microphone() as source:
        if ask:
            speak(ask)
        audio = r.listen(source)# listen for audio 
        voice = ""
        try:
            voice = r.recognize_google(audio) # recognize the audio using Google Speech Recognition       
        except sr.UnknownValueError:
            speak("Could not understand audio")
            speak("Could not understand audio")
        except sr.RequestError as e:
            speak("Could not request results; {0}".format(e))
        return voice
    
def response(voice):
    if "hello" in voice:
        speak("Hello! How are you?")
    elif "what time is it" in voice:
        speak(ctime())
    elif "search" in voice:
        search = get_audio("What do you want to search for today?")
        url = "https://www.google.com/search?q=" + search
        webbrowser.get().open(url)
        speak("Here is what I found for " + search)
    elif "find location" in voice:
        location = get_audio("What is the location?")
        url = "https://www.google.nl/maps/place/" + location + "/&amp;"
        webbrowser.get().open(url)
        speak("Here is the location of " + location+ " on Google Maps")
    elif "exit" in voice:
        speak("Goodbye!")
        exit()
    else:
        speak("I am sorry, I did not get that. Please try again.")

def speak(audio_string):
    tts = gTTS(text=audio_string, lang='en')
    r = random.randint(1, 10000000)
    audio_file = 'audio-' + str(r) + '.mp3'
    tts.save(audio_file)
    playsound.playsound(audio_file)
    speak(audio_string)
    os.remove(audio_file)
        
time.sleep(2)
speak("How can I assist you today?")
while 2:
    voice = get_audio()
    response(voice)