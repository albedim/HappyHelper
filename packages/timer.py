import asyncio
import os
from datetime import datetime, timedelta

from playsound import playsound

from main.utils import getFirstWord


# Gets the last timer.py time
def getLastTime(givenTime) -> str:
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


async def timer(lastTime) -> None:
    await asyncio.run(os.system(f'cmd /k python ./packages/start_timer.py {lastTime}'))
    playsound('assets/audio/alarm.mp3')
