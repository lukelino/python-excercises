#! python3
"""
    Utworzenie 35 quizów,
    Dla każdego quizu 50 pytań losowo ułożonych,
    Dla każdego pytania losowo ułożone odpowiedzi,
    Zapis quizów w 35 plikach,
    Utworzenie odpowiedzi do wygenerowanych 35 plików txt,
    ----
    Słownik do przechowywania pary klucz: wartość --> Stan: Stolica
    metody open(), write(), close()
    random.shuffle() --> losowość pytań i odpowiedzi
"""

import random
import re
import pprint
import os


def create_a_dict_of_states_capitals(whole_data):
    states_reg = re.compile(r'''
    (.*)                            # stan
    (\s\W\w\w\W)                    # kod stanu
    (\s-\s)                         # separator
    (\w.*)                          # stolica
    ''', re.VERBOSE)

    # Umieszczenie danych quizu w słowniku
    capitals_dct = {}
    for groups in states_reg.findall(whole_data):
        capitals_dct.setdefault(groups[0], groups[3])
    print(capitals_dct)
    return capitals_dct


def create_a_py_module_of_states_capitals(capital_state):
    # Zapisanie słownika jako plik/moduł
    with open(file, 'w') as f:
        f.write('capitals = ' + pprint.pformat(capital_state) + '\n\t')


current_dir = os.getcwd()

path_1 = os.path.join(current_dir, 'states_capitals.txt')
file = r'capitals_module.py'
path_2 = os.path.join(current_dir, file)

if not os.path.exists(path_2):
    with open(path_1, 'r') as f:
        whole_data = f.read()
    # print(whole_data)
    capitals = create_a_dict_of_states_capitals(whole_data)
    create_a_py_module_of_states_capitals(capitals)
