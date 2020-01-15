#! python3
"""Kompresja plików za pomocą modułu zipfile"""

import zipfile
import os
import re

path = os.getcwd()
all_files = os.listdir(path)

file_to_zip = ''        # By uniknąć błędu, że może nie być przypisana wartość
for file in all_files:
    if file.endswith('txt'):
        file_to_zip = file

fileRegex = re.compile(r'''((\w.*)(\.)(\w{3}))''', re.VERBOSE)
pattern = fileRegex.findall(file_to_zip)

newFile = pattern[0][1] + '_0' + '.zip'

answer = input('z - zip  e - extract: ')
if answer == 'z':
    if not os.path.exists(newFile):
        fileZip = zipfile.ZipFile(os.path.join(path, newFile), 'w')
        fileZip.write(pattern[0][0], compress_type=zipfile.ZIP_DEFLATED)
        fileZip.close()
        print(f'{file_to_zip}: {os.path.getsize(os.path.join(path, file_to_zip))}')
        print(f'{newFile}: {os.path.getsize(os.path.join(path, newFile))}')
    else:
        num = 0
        while True:
            to_zip_file = os.path.basename(pattern[0][1]) + '_' + str(num) + '.zip'
            if not os.path.exists(to_zip_file):
                break
            num += 1
        fileZip = zipfile.ZipFile(os.path.join(path, to_zip_file), 'w')
        fileZip.write(to_zip_file, compress_type=zipfile.ZIP_DEFLATED)
        fileZip.close()
elif answer == 'e':
    readZip = zipfile.ZipFile(os.path.join(path, newFile))
    readZip.extractall(os.path.join(path, 'Extracted'))
    readZip.close()
else:
    print('!')
