"""
    Formatowanie tekstu.
    Sprawdza w słoniku najdłuższy klucz - wartość i dopasowuje formatowanie
"""
dct = {'imię': 'Robert', 'nazwisko': 'Johnson', 'profesja': 'blues', 'wiek': 42, 'instrument': 'gitara akustyczna'}


def check_length(dictionary):           # Sprawdza długość klucza, zapiuje w liście i zwraca max
    lst = []
    for k, v in dictionary.items():
        lst.append(len(k))
    return max(lst)


m = check_length(dct)

for k, v in dct.items():
    print(k.ljust(m + 10, '.') + str(v).rjust(1))       # '42' wymaga str, żeby użyć rjust()
