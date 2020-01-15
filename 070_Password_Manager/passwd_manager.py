#! python3
# Niebezpieczny program menedżera haseł
PASSWORDS = {'email': 'JKLjky7ghjg65gft57fgh67bBGT', 'blog': 'poiPOINBNHG6*&^%$YGYUTFguyt6rfghf3#@',
             'luggage': '12345'}
# Argumenty wiersza poleceń będą przechowywane w zmiennej o nazwie sys.argv.
# Pierwszym elementem na liscie sys.argv zawsze powienien być ciąg tekstowy zawierający nazwę programu.
# Drugim elementem powinien być pierwszy argument wiersza poleceń -- tutaj nazwa konta, dla którego chcemy pobrać hasło.

import sys
import pyperclip

if len(sys.argv) < 2:
    print('Użycie: python passwd.py [konto] - skopiowanie wskazanego konta')
    sys.exit()

account = sys.argv[1]   # Pierwszym argumentem wiersza poleceń jest nazwa konta

if account in PASSWORDS:
    pyperclip.copy(PASSWORDS[account])
    print('Hasło do konta {account} zostało skopiowane do schowka.')
else:
    print(f'{account} nie istnieje.')
