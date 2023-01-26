from googletrans import Translator

from main.system_iterator import getVocalOutput
from packages.languages import LANGUAGES


def translate(text, language) -> str | None:
    try:
        translator = Translator()
        newLanguage = translator.translate(language, dest='en').text.lower()
        newText = translator.translate(text, dest=LANGUAGES[newLanguage]).text
        return newText.lower()
    except KeyError:
        return getVocalOutput()['translation_error']
