#! python3
"""
    1. Funkcja pobiera ciąg tekstowy
    2. Jeśli nie ma argumentów -- usuwa białe znaki
    3. Jeśli ma argumenty -- usuwa znaki przekazane jako argument
"""
import re


def do_something_with_string(txt, param=None):
    if param is None:
        when_no_param = re.compile(r'(^\s*)|(\s*$)')        # zaczyna się od spacji i kończy się spacją
        new_string = when_no_param.sub(r'', txt)
        print(len(new_string))
    else:
        when_param = re.compile(f'{param}')
        new_string = when_param.sub(r'', txt)
    return new_string


my_string = '             Ala ma małego kota. Nic specjalnego,  a  to nie jest. ale jaja.     '
print(do_something_with_string(my_string))
s = do_something_with_string(my_string, 'a')
print(s)
