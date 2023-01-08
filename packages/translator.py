import translators as ts

from main.system_iterator import getAppConfig
from packages.languages import LANGUAGES


def translate(text, language) -> str | None:
    try:
        newLanguage = ts.translate_text(language, from_language=getAppConfig()['language'], to_language='en').lower()
        newText = ts.translate_text(text, from_language=getAppConfig()['language'], to_language=LANGUAGES[newLanguage])
        return newText.lower()
    except Exception:
        return None
