import asyncio
import sys

from datetime import datetime
from playsound import playsound


async def timer(lastTime) -> None:
    while lastTime != datetime.now().strftime("%H:%M:%S"):
        await asyncio.sleep(1)
    playsound('assets/audio/alarm.mp3')


asyncio.run(timer(sys.argv[1]))
