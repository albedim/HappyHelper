import pyttsx3

from system_iterator import getAppConfig


def say(command):
    engine = pyttsx3.init()
    engine.say(command)
    engine.runAndWait()
