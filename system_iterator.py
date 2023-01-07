import json
import os
import pywhatkit as kit


def destroyTasks():
    os.system("taskkill /im chrome.exe /f")


def play(title):
    kit.playonyt(title)


def replaceChars(text: str):
    return text.replace("è", "e")


def getVocalCommands():
    return json.load(open('utils.json'))['vocal_input'][0]


def getVocalOutput():
    return json.load(open('utils.json'))['vocal_output'][0]


def getAppConfig():
    return json.load(open('utils.json'))['app_config'][0]
