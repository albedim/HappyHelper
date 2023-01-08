import pyttsx3


def say(command) -> None:
    engine = pyttsx3.init()
    engine.say(command)
    engine.runAndWait()
