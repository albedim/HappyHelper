import speech_recognition as sr

from system_iterator import getAppConfig

recognizer = sr.Recognizer()


def toText(audio):
    try:
        text = recognizer.recognize_google(audio, language=getAppConfig()['language'])
        return text.lower()
    except sr.RequestError as e:
        return 'Could not request results;' + e
    except sr.UnknownValueError:
        return 'Warning: Empty voice'
    except Exception:
        return 'Could not request results;'


def listen() -> sr.AudioData:
    with sr.Microphone() as source:
        recognizer.adjust_for_ambient_noise(source, duration=0.2)
        audio = recognizer.listen(source, phrase_time_limit=3)
        return audio
