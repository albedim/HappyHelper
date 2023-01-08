import json
import os
import asyncio
import pywhatkit as kit

from datetime import datetime, timedelta
from audio.extractor import say
from main.utils import getFirstWord


def destroyTasks():
    os.system("taskkill /im chrome.exe /f")


def play(title):
    kit.playonyt(title)


# Gets the last timer time
def getLastTime(givenTime):
    currentTime = datetime.strptime(datetime.now().strftime("%H:%M:%S"), "%H:%M:%S")
    param = int(getFirstWord(givenTime))
    timerTime = None
    if "ora" in givenTime or "ore" in givenTime:
        timerTime = currentTime + timedelta(hours=param)
    elif "minuto" in givenTime or "minuti" in givenTime:
        timerTime = currentTime + timedelta(minutes=param)
    elif "secondo" in givenTime or "secondi" in givenTime:
        timerTime = currentTime + timedelta(seconds=param)
    return timerTime.time().strftime("%H:%M:%S")


async def timer(lastTime):
    while lastTime != datetime.now().strftime("%H:%M:%S"):
        await asyncio.sleep(1)
    for i in range(5):
        say(getVocalOutput()['timer_finished'])


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
