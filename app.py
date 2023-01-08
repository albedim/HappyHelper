from audio.extractor import say
from audio.recognizer import listen, toText
from main.actions import getAction, getCalling, getStopRequest
from main.system_iterator import destroyTasks, getVocalOutput


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
    print(text)
    getAction(text)


if __name__ == '__main__':
    while True:
        execute()
