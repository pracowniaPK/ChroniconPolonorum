import re

def replace(words, text):
    for s in words:
        text = re.sub(' {} '.format(s), '~{} '.format(s), text)
    return text

f = open('tekst.txt', 'r', encoding='utf-8')
txt = f.read()
# txt = re.sub(' i', '~i', txt)
txt = replace(['a', 'i', 'o', 'u', 'w', 'z'], txt)

print(txt)

