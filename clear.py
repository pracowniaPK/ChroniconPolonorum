import re

f = open('tekst.txt', 'r', encoding='utf-8')
txt = f.read()
txt = re.sub('(\[\d+\])', '', txt)
print(txt)
