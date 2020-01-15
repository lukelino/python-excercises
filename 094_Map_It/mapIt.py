#! python3
""" Pobiera adres z wiersza poleceń lub ze schwka i uruchamia mapę google """

import sys
import pyperclip
import webbrowser

if len(sys.argv) > 1:
    # Pobierz dane z wiersza poleceń
    address = ' '.join(sys.argv[1:])
else:
    # Wklej adres ze schowka
    address = pyperclip.paste()

# Otwórz mapy google
webbrowser.open_new_tab(f'https://www.google.pl/maps/place/{address}')
