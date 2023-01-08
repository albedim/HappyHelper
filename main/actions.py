import asyncio

from datetime import datetime
from wikipedia import wikipedia
from audio.extractor import say
from main.utils import getContent, replaceChars, getWordsNumber
from main.system_iterator import play, getVocalCommands, getVocalOutput, getAppConfig, getLastTime, timer


def getAction(text):
    # Play music
    if getVocalCommands()['play'] in text:
        song = getContent(text, 1)
        play(title=song)
        return say(f'{song}, da youtube')
    # TODO
    elif getVocalCommands()['say'] in text or getVocalCommands()['tell_me'] in text:
        return say(f'Cosa devo dirti?')
    # What is it or who are they
    elif replaceChars(getVocalCommands()['what_is']) in text or replaceChars(getVocalCommands()['who_is']) in text:
        content = getContent(text, 2)
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
        lastTime = getLastTime(getContent(text, getWordsNumber(text) - 2))
        asyncio.run(timer(lastTime))
    else:
        return say(getVocalOutput()['not_understood'])


# checks if there is the assistant name in the provided string
def getCalling(text):
    return getAppConfig()['name'] in text


# checks if there is the stop command in the provided string
def getStopRequest(text):
    return getAppConfig()['stop'] in text


