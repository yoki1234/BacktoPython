import pyttsx3
engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('rate',150)
engine.runAndWait()

def speak(str):
    engine.say(str)
    engine.runAndWait()

speak("hello,how are you")