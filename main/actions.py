import asyncio
import random

import translators as ts
from datetime import datetime
from wikipedia import wikipedia
from audio.extractor import say
from main.utils import subFirstWord, replaceChars, getWordsNumber, subLastWord
from main.system_iterator import play, getVocalCommands, getVocalOutput, getAppConfig
from packages.tasks import addTask, hasTasks, readTasks, deleteTasks
from packages.timer import getLastTime, timer
from packages.translator import translate


def getAction(text) -> None:
    if getCalling(text):
        # Bad words checker
        if "*" in text:
            return say(getVocalOutput()['no_bad_words'])
        # Hi
        elif getVocalCommands()['hi'] in text:
            return say(getVocalOutput()['hi'])
        # How are you
        elif getVocalCommands()['how_are_you'] in text or getVocalCommands()['how_are_you1'] in text:
            if random.randint(0, 100) > 50:
                return say(getVocalOutput()['im_fine'])
            else:
                return say(getVocalOutput()['im_fine1'])
        # Play music
        elif getVocalCommands()['play'] in text:
            song = subFirstWord(text, 2)
            play(title=song)
            return say(f'{song}, da youtube')
        # What is it or who are they
        elif replaceChars(getVocalCommands()['what_is']) in text or replaceChars(getVocalCommands()['who_is']) in text:
            content = subFirstWord(text, 3)
            wikipedia.set_lang(getAppConfig()['language'])
            return say(wikipedia.summary(content.replace(" ", "_"), 3))
        # Current time
        elif getVocalCommands()['current_time'] in text:
            return say(getVocalOutput()['time'] + datetime.now().strftime("%H:%M"))
        # Current date
        elif replaceChars(getVocalCommands()['current_date']) in text:
            return say(getVocalOutput()['date'] + datetime.now().strftime("%A, %d %B"))
        # Thank you
        elif getVocalCommands()['thank_you'] in text:
            return say(getVocalOutput()['you_are_welcome'])
        # Timer
        elif getVocalCommands()['request_timer'] in text:
            time = subFirstWord(text, getWordsNumber(text) - 2)
            lastTime = getLastTime(time)
            say(time + getVocalOutput()['from_now'])
            asyncio.run(timer(lastTime))
        # Add a task
        elif (getVocalCommands()['add'] in text or getVocalCommands()['add1'] in text) and \
                getVocalCommands()['tasks'] in text:
            task = subFirstWord(text, 4)
            addTask(task)
            return say(getVocalOutput()['task_added'])
        # Get tasks
        elif getVocalCommands()['tasks'] in text and (
                getVocalCommands()['tell_me'] in text or getVocalCommands()['say'] in text):
            if hasTasks():
                readTasks()
            else:
                return say(getVocalOutput()['no_tasks_found'])
        # Delete Tasks
        elif (getVocalCommands()['delete'] in text or getVocalCommands()['delete1'] in text) and  \
                getVocalCommands()['tasks']:
            deleteTasks()
            say(getVocalOutput()['tasks_removed'])
        else:
            return say(getVocalOutput()['not_understood'])


# checks if there is the assistant name in the provided string
def getCalling(text):
    return getAppConfig()['name'] in text


# checks if there is the stop command in the provided string
def getStopRequest(text):
    return getAppConfig()['stop'] in text
