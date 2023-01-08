import json

from datetime import datetime
from audio.extractor import say
from main.system_iterator import getVocalOutput


def readTasks():
    tasks = json.load(open('user_tasks.json'))
    for task in tasks:
        say(task['name'] + getVocalOutput()['added_in'] + task['date'])


def hasTasks():
    tasks = json.load(open('user_tasks.json'))
    return len(tasks) > 0


def deleteTasks():
    with open("user_tasks.json", "w") as outfile:
        json.dump([], outfile)


def addTask(task):
    tasks = json.load(open('user_tasks.json'))
    tasks.append({
        "name": task,
        "date": datetime.now().strftime("%A, %d %B")
    })
    with open("user_tasks.json", "w") as outfile:
        json.dump(tasks, outfile)