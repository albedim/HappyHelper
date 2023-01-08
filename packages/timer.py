import asyncio

from datetime import datetime, timedelta
from audio.extractor import say
from main.system_iterator import getVocalOutput
from main.utils import getFirstWord


# Gets the last timer.py time
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