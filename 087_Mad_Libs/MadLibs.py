#! python3
"""odczytuje zawartość pliku tekstowego i pozwala użytkownikowi dodać własny tekst"""
# Pozwala zastąpić w tym tekście słowa PRZYMIOTNIK, RZECZOWNIK, PRZYSŁÓWEK, CZASOWNIK

import re

key_words = ['PRZYMIOTNIK', 'RZECZOWNIK', 'PRZYSŁÓWEK', 'CZASOWNIK', 'RZECZOWNIK']
pairs_of_words = []

for i in range(len(key_words)):
    user_word = input(f'Podaj {key_words[i]}: ')
    pair = (key_words[i], user_word)
    pairs_of_words.append(pair)

with open(r'F:\Py\087_Mad_Libs\mad_libs.txt', encoding='utf-8') as f:
    txt = f.read()

for old, new in pairs_of_words:
    txt = re.sub(old, new, txt, 1)

print(txt)

with open(r'F:\Py\087_Mad_Libs\mad_libs_2.txt', 'a', encoding='utf-8') as f:
    f.write(txt + '\n')
