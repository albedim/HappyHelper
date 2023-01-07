from extractor import say
from recognizer import listen, toText
from actions import getAction, getCalling, getStopRequest
from system_iterator import destroyTasks, getVocalOutput


def execute():
    print("Listening...")
    audio = listen()
    text = toText(audio)
    if getCalling(text):
        say(getVocalOutput()['ready_for_listening'])
        do()
    if getStopRequest(text):
        destroyTasks()


def do():
    print("Waiting for commands...")
    audio = listen()
    text = toText(audio)
    getAction(text)


if __name__ == '__main__':
    while True:
        execute()
