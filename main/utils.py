
def getFirstWord(text):
    return text.split(" ")[0]


# Gets the content from a sentence
def subFirstWord(text, firstIndex) -> str:
    words = text.split(" ")
    content = ''
    counter = 0
    while counter < len(words):
        content += words[counter] + " " if counter >= firstIndex else ''
        counter += 1
    return content


def subLastWord(text, firstIndex, lastIndex) -> str:
    words = text.split(" ")
    content = ''
    counter = 0
    while counter < len(words):
        content += words[counter] + " " if firstIndex <= counter < lastIndex else ''
        counter += 1
    return content


def getWordsNumber(text) -> int:
    return len(text.split(" "))


def replaceChars(text: str) -> str:
    return text.replace("Ã¨", "è")