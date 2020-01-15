#! python3
"""
    czytanie i zapisywanie plików.
"""
import os
file = r'F:\Py\078_Reading_Writing_Files\inwokacja.txt'
encoding = 'utf-8'


def reading_file(file):
    with open(file, encoding=encoding) as f:
        txt = f.read()
        print(txt)


def read_line(file):
    with open(file, encoding=encoding) as f:
        line = f.readline()
        while line:
            print(line, end='')
            line = f.readline()


def reading_lines(file):
    with open(file, encoding=encoding) as f:
        txt = f.readlines()
        print(txt)


def writing_txt(file, txt):
    with open(file, 'a', encoding=encoding) as f:
        f.write(txt)


reading_file(file)
print('\n')
read_line(file)
print('\n')
reading_lines(file)

txt = '\nLitwa to nie moja ojczyzna.\n'
writing_txt(file, txt)
print('\n', 'a\n')
reading_file(file)