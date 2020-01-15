#! python3
"""Przejście przez drzewo katalogu"""

import os

for folderName, subFolders, filenames in os.walk(r'D:\Kama'):
    print('Katalog bieżący to: ' + folderName)

    for subfolder in subFolders:
        print(f'Podkatalog katalogu {folderName}: {subfolder}')

    for filename in filenames:
        print(f'Plik katalogu {folderName}: {filename}')
