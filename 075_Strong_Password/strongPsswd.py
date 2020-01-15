#! python3
"""
    Funkcja używa wyrażeń regularnych by sprawdzić siłę hasła
"""

import re


def check_if_strong(psswd):
    length = re.compile(r'.{8,}')
    lower_case = re.compile(r'[a-z]')
    upper_case = re.compile(r'[A-Z]')
    pattern_length = length.search(psswd)
    pattern_lower_case = lower_case.search(psswd)
    pattern_upper_case = upper_case.search(psswd)

    if pattern_length is not None and pattern_lower_case is not None and pattern_upper_case is not None:
        return True
    else:
        return False


def string_check(psswd):
    lst = []
    if len(psswd) >= 8:
        for char in psswd:
            if char.isdigit():
                lst.append(True)
                break
        for char in psswd:
            if char.islower():
                lst.append(True)
                break
        for char in psswd:
            if char.isupper():
                lst.append(True)
                break
    print(lst)
    if len(lst) == 3:
        return True
    else:
        return False


my_password = '10a2QABC!'
if check_if_strong(my_password):
    print(True)
else:
    print(False)

if string_check(my_password):
    print(f'str -> {True}')
else:
    print(f'str -> {False}')
