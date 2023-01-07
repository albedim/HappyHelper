import json
import os
import translators.server as ts
import pywhatkit as kit


def destroyTasks():
    os.system("taskkill /im chrome.exe /f")


def play(title):
    kit.playonyt(title)


def replaceChars(text: str):
    return text.replace("e", "è")


def getVocalCommands():
    return json.load(open('utils.json'))['vocal_input'][0]

"""
def translate(text):
    try:
        return ts.translate_text(text, from_language='en', to_language=getAppConfig()['language'])
    except Exception:
        return text
"""


def getVocalOutput():
    return json.load(open('utils.json'))['vocal_output'][0]


def getAppConfig():
    return json.load(open('utils.json'))['app_config'][0]
