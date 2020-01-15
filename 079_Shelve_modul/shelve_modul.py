#! python3
"""
    Działanie modułu 'shelve -- umożliwia zapisz/otwórz.
    Pozwala przechowywać w pliku zmienne, dane.
"""
import shelve

data_file = shelve.open('data_file')
cats = ['Morpheus', 'Heroin', 'Too Tight']
data_file['cats'] = cats
data_file.close()

