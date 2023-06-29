# pip install pyttsx3 
# pip install speechrecognition
# pip install datetime
# pip install pyjokes
# pip install pipwin
# pipwin install pyaudio

import pyttsx3                     # for text to speech conversion
import speech_recognition as sr # for speech recognition and speech to text conversion ,will get speech as input from user
import datetime
import pyjokes
import webbrowser
import os
import time
def sptotext():
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening.....")
        recognizer.adjust_for_ambient_noise(source)
        audio = recognizer.listen(source)
        try:
            print("Recognizing......")
            data = recognizer.recognize_google(audio)
            print(data)
            return data
        except sr.UnknownValueError:
            data = "Not Understand"
            print(data)
            return data 
# sptotext()

def texttosp(x):
    engine = pyttsx3.init()
    voices = engine.getProperty('voices')
    engine.setProperty('voice',voices[0].id)
    rate = engine.getProperty('rate')
    engine.setProperty('rate',150)
    engine.say(x)
    engine.runAndWait()
# texttosp("Hello guys !")

if __name__ == '__main__':
    if "hello captain" in sptotext().lower():
        texttosp("hey Akshita") 
        while True:
            data1= sptotext().lower()
            if "your name" in data1:
                name="my name is captain"
                texttosp(name)
            elif "my name" in data1:
                name2="your name is Akshita Agrawal"
                texttosp(name2)
            elif "old are you" in data1:
                age="i am one month old"
                texttosp(age)
            elif "about yourself" in data1:
                about="myself captain, your voice administrator. i am one month old. you can ask me anything, i will try my best to satisfie you with the appropriate output. thanku !"
                texttosp(about)
            elif "time" in data1:
                time=datetime.datetime.now().strftime("%I%M%p")
                texttosp(time)
            elif "youtube" in data1:
                webbrowser.open("https://www.youtube.com/")
            elif "song" in data1:
                webbrowser.open("https://www.youtube.com/watch?v=nojhZlC326g")
            elif "bhajan" in data1:
                webbrowser.open("https://www.youtube.com/watch?v=AqyWfisjCFQ&list=PLB_UT8N8x8i5Drbe4msTs89lcv7gwpoKm&index=1")
            elif "linkedin" in data1:
                webbrowser.open("https://www.linkedin.com/in/akshita-agrawal-847411232/")
            elif "joke" in data1:
                joke1 = pyjokes.get_joke(language="en",category="neutral")
                print(joke1)
                texttosp(joke1)
            elif "picture" in data1:
                add= "C:/Users/lenovo/Desktop/AKSHITA/Photos"
                listpics = os.listdir(add)
                print(listpics)
                # os.startfile(os.path.join(add,listpics[0]))
                os.startfile(os.path.join(add,listpics[int(sptotext())]))
            elif "exit" in data1:
                texttosp("thanku very much Akshita! nice to talk you.")
                texttosp("exit")
                break
            else:
                texttosp("sorry! I am unable to get data.")
                texttosp("thanks")
                texttosp("exit")
                break
            time.sleep(2)
    else:
        texttosp("sorry! I am unable to proceed")
        texttosp("thanks")
        texttosp("exit")

# email,whatsapp,insta,facebook,tmkoc,..................