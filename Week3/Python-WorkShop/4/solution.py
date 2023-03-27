
import re

def main(str):
    words = re.findall(r"[^\s,;. ]+|[,.; ]", str)
    capitalized_words = []
    for word in words:
        if word[0].isalpha() or word[0].isascii():
            capitalized_words.append(word[0].upper() + word[1:].lower())
        else:
            capitalized_words.append(word)
    capital = ''.join(capitalized_words)
    return capital 