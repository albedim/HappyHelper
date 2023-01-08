from audio.recognizer import listen, toText
from main.actions import getAction


def execute():
    print("Listening...")
    audio = listen()
    text = toText(audio)
    getAction(text)
    print(text)


if __name__ == '__main__':
    while True:
        execute()
