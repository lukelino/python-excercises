#! python3
"""Przenosi pliki z pulpitu do folderu"""

import shutil
import os
import sys
import datetime
import re

data = datetime.datetime.now().replace(microsecond=0)

# Zamiana spacji na podkreślnik, zamiana : na podkreślenie
patterns = [('-', ''), (' ', '_'), (':', '_')]
for old, new in patterns:
    data = re.sub(old, new, str(data))

# Utworzenie podkatalogu
target_dir = sys.argv[1]
target_dir = target_dir + ':'
target_sub_dir = os.path.join(target_dir, str(data))
os.mkdir(target_sub_dir)
print(f'w katalogu {target_dir} utworzono katalog {data}.')

desktop_path = r'C:\Users\Lukasz\Desktop'
all_files_on_desktop = os.listdir(desktop_path)

endings = ['doc', 'pdf', 'ppt', 'pptx', 'docx', 'xls', 'xlsx', 'odp', 'jpg', 'odt', 'txt', 'DOCX']
files_to_be_moved = []
for file in all_files_on_desktop:
    for ending in endings:
        if file.endswith(ending):
            files_to_be_moved.append(file)

print(f'Przeniesione pliki do katalogu {target_sub_dir}:')
for elem in files_to_be_moved:
    print(elem)
    shutil.move(os.path.join(desktop_path, elem), target_sub_dir)
