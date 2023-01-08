
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


def getWordsNumber(text):
    return len(text.split(" "))


def replaceChars(text: str):
    return text.replace("e", "è")