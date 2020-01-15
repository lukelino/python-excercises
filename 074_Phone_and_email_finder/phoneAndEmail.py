#! python3
# phone and email -- wyszukuje numery telefonów i adresy e-mail z listy
"""
    1. Pobranie tekstu ze schowka
    2. Wyszukanie w tekście numerów telefonów i adresów e-mail
    3. Umieszczenie znalezionych danych w schowku

    moduły: pyperclip, re
    dwa wyrażenia regularne do dopasowania numeru i adresu
    znaleźć wszystkie dopasowania
    sformatować i umieścić w schowku
    jakiś komunikat, jeśli brak numerów
"""

import pyperclip
import re

phoneRegex = re.compile(
    r'''(
    (\d{3}|\(\d{3}\))?              # numer kierunkowy. Opcjonalny -- dlatego pojawia sią '?'
    (\s|-|\.)?                      # separator
    (\d{3})                         # pierwsze trzy cyfry
    (\s|-|\.)                       # separator
    (\d{4})                         # ostatnie cztery cyfry
    (\s*(ext|x|ext.)\s*(\d{2,5}))?  # numer wewnętrzny 
    )''', re.VERBOSE)

# Utworzenie wyrażenia regularnego dopasowującego adres e-mail
emailRegex = re.compile(
    r'''(
    [a-zA-Z0-9._%+-]+               # nazwa użytkownika
    @                               # znak '@'
    [a-zA-Z0-9.-]+                  # nazwa domeny
    (\.[a-zA-Z]{2,4})               # kropka i później cokolwiek
    )''', re.VERBOSE)

with open('some_data.txt', 'r') as f:
    text = str(pyperclip.copy(f.read()))
text = str(pyperclip.paste())

# Wyszukanie wyrażeń w schowku
# text = str(pyperclip.copy())
matches = []

for groups in phoneRegex.findall(text):
    phoneNum = '-'.join([groups[1], groups[3], groups[5]])
    if groups[8] != '':
        phoneNum += ' ext ' + groups[8]
    matches.append(phoneNum)
for groups in emailRegex.findall(text):
    matches.append(groups[0])

# Skopiowanie wyników do schowka
if len(matches) > 0:
    pyperclip.copy('\n'.join(matches))
    print('Skopiowano do schowka:')
    print('\n'.join(matches))
else:
    print('Nie znaleziono żadnego numeru telefonu lub adresu email.')
