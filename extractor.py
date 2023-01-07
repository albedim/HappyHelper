import pyttsx3


def say(command):
    engine = pyttsx3.init()
    engine.say(command)
    engine.runAndWait()