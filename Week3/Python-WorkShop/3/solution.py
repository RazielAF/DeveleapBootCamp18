import re


def main(sentence):
  if not sentence:
    return ""
  
  words=re.findall(r'\b\w+\b',sentence)

  long_word=max(words,key=len)

  return long_word

print(main(""))