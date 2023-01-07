import time

from wikipedia import wikipedia
from extractor import say
from system_iterator import play, getVocalCommands, getVocalOutput, getAppConfig


def getFirstWord(text):
    return text.split(" ")[0]


# Gets the content from a sentence
def getContent(text, firstIndex):
    words = text.split(" ")
    content = ''
    counter = 0
    while counter < len(words):
        content += words[counter] + " " if counter >= firstIndex else ''
        counter += 1
    return content


def getAction(text):
    if getVocalCommands()['play'] in text:
        song = getContent(text, 1)
        play(title=song)
        return say(f'{song}, da youtube')
    elif getVocalCommands()['say'] in text or getVocalCommands()['tell_me'] in text:
        return say(f'Cosa devo dirti?')
    elif getVocalCommands()['what_is'] in text or getVocalCommands()['who_is'] in text:
        content = getContent(text, 2)
        wikipedia.set_lang(getAppConfig()['language'])
        return say(wikipedia.summary(content.replace(" ", "_"), 3))
    elif getVocalCommands()['current_time'] in text:
        return say("Sono le " + time.localtime().strftime("%H:%M"))
    else:
        return say(getVocalOutput()['not_understood'])


# checks if there is the assistant name in the provided string
def getCalling(text):
    return getAppConfig()['name'] in text


# checks if there is the stop command in the provided string
def getStopRequest(text):
    return getAppConfig()['stop'] in text


