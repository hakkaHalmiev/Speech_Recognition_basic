from playsound import playsound
from gtts import gTTS, tts
import speech_recognition as sr
import os
import time
from datetime import datetime
import random
from random import choice

r=sr.Recognizer()

def record(ask=False):
    with sr.Microphone() as source:
        if ask:
            print(ask)
        audio=r.listen(source)     
        voice= ""
        try:
            voice=r.recognize_google(audio,language="tr-TR")
        except sr.UnknownValueError :
            print("asistan: anlamadım")
        except sr.RequestError:
            print("asistan: çalışmıyor")
        return voice

def response (voice):
    if "merhaba" in voice:
        speak("sana da merhaba canım benim ")
    if "motor" in voice:
        speak("motoru başlattım patron ")
    if "testere" in voice or "destere" in voice:
        speak("testere başladı merak etme ")
    if "saat" in voice or "saat kaç" in voice:
        selection=["Saat şu an : ","hemen bakıyorum: "]
        clock=datetime.now().strftime("%H:%M")
        selection=random.choice(selection)
        speak(selection+clock)
        ##speak(datetime.now().strftime("%H:%M"))
    if "tarih" in voice or "hangi gündeyiz" in voice:
        speak(datetime.now().strftime("%H:%M"))
    elif "programı kapat" in voice or "görüşürüz" in voice:
        speak("kapatıyorum, görüşürüz, iyi günler")
        os.remove("answer.mp3")
        exit()
    else:
        speak("tekrar söyleyiniz lütfen")
   
   
def speak (string):
    tts=gTTS(text=string,lang="tr",slow=False)
    file ="answer.mp3"
    tts.save(file)
    playsound(file)
    os.remove(file)

speak("selam")
print("selam")

while True:
       voice=record()
       if voice!='':
            voice=voice.lower()
            print(voice)
            response(voice)

