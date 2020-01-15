#! python3
"""Kopiowanie plików i katalogów"""

import shutil
import os
import send2trash

path = os.getcwd()

# skopiowanie pliku
shutil.copy(r'F:\Py\088_Users_RegEx_in_txt\Miles_3.txt', path)
size = os.path.getsize(os.path.join(path, 'Miles_3.txt'))
print(round(size/1000))

# usunięcie katalogu
# os.unlink(r'F:\Py\tmp_a\Nowy obraz mapy bitowej.bmp')

# skopiowanie katalogu. argument DST: tworzy katalog
# shutil.copytree(r'F:\Py\tmp', r'F:\Py\tmp_a')

dir_list = os.listdir(path)
print(dir_list)

send2trash.send2trash(r'F:\Py\tmp_a\Nowy_dokument_tekstowy_(2).txt')

