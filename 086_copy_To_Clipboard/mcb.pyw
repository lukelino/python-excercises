#! python3
""" mcb.pyw -- zapisuje i wczytuje do schowka fragmenty tekstu """
# Użycie:   py.exe mcb.pyw save <słowo-kluczowe> -- zapis schowka wraz ze słowem kluczowym
#           py.exe mcb.pyw <słowo-kluczowe> -- wczytanie słowa kluczowego do schowka
#           py.exe mcb.pyw list -- wczytanie wszystkich słów kluczowych do schowka

import shelve
import pyperclip
import sys

mcbShelf = shelve.open('mcb')

# zapis zawartości schowka
if len(sys.argv) == 3 and sys.argv[1].lower() == 'save':
    mcbShelf[sys.argv[2]] = pyperclip.paste()
elif len(sys.argv) == 3 and sys.argv[1].lower() == 'delete':
    del mcbShelf[sys.argv[2]]
elif len(sys.argv) == 2 and sys.argv[1].lower() == 'delete':
    mcbShelf.clear()
    pyperclip.copy(str(list(mcbShelf.keys())))
elif len(sys.argv) == 2:
    # wyświetlenie listy słów kluczowych i wczytanie treści
    if sys.argv[1].lower() == 'list':
        pyperclip.copy(str(list(mcbShelf.keys())))
    elif sys.argv[1] in mcbShelf:
        pyperclip.copy(mcbShelf[sys.argv[1]])
mcbShelf.close()
