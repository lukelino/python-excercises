#! python3
"""
    Tworzy katalogi i podkatalogi w pętli
"""

import os


def create_dirs():
    current_dir = os.getcwd()
    print(current_dir)
    for dirs in range(20):
        os.makedirs(f'{current_dir}'.join(f'\\{dirs}\\{dirs+1}'))


create_dirs()
