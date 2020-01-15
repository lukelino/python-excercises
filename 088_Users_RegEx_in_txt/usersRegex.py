#! python3
"""otwiera wszystkie pliki 'txt' i szuka wierszy dopasowanych do podanego przez użytkownika wyrażenia"""
import os
import re
import pprint

current_dir = os.getcwd()

all_files = os.listdir(current_dir)
files = list()
for elem in all_files:
    if elem.endswith('txt'):
        files.append(elem)

txt = ''
for file in files:
    with open(file, encoding='utf-8') as f:
        txt += f.read()

usersReg = input('Podaj wyrażenie regularne do dopasowania: ')
regExp = re.compile(usersReg)
reg = re.findall(regExp, txt)

regExpAll = re.compile(f'\\n.*\\s{usersReg}\\s.*\\.')
result = re.findall(regExpAll, txt)


# pp.pprint(result)
with open('new.txt', 'w', encoding='utf-8') as new_f:
    pp = pprint.PrettyPrinter(indent=2, width=70, stream=new_f)
    pp.pprint(result)
