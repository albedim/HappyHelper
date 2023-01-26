from audio.recognizer import listen, toText
from main.actions import getAction


def execute() -> None:
    print("Listening...")
    audio = listen()
    text = toText(audio)
    print(text)
    getAction(text)


if __name__ == '__main__':
    while True:
        execute()
