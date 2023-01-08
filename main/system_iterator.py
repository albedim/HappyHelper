import json
import os
import pywhatkit as kit


def destroyTasks() -> None:
    os.system("taskkill /im chrome.exe /f")


def play(title) -> None:
    kit.playonyt(title)


def getVocalCommands() -> list:
    return json.load(open('utils.json'))['vocal_input'][0]


def getVocalOutput() -> list:
    return json.load(open('utils.json'))['vocal_output'][0]


def getUserTasks() -> list:
    return json.load(open('user_tasks.json'))


def getAppConfig() -> list:
    return json.load(open('utils.json'))['app_config'][0]
