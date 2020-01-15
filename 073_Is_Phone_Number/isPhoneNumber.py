"""
sprawdza, czy ciąg tekstu jest numerem telefonicznym.
"""
import re


def is_phone_number(txt):
    if len(txt) != 11:
        return False
    for i in range(0, 3):
        if not txt[i].isdecimal():
            return False
    if txt[3] != '-':
        return False
    for i in range(4, 7):
        if not txt[i].isdecimal():
            return False
    if txt[7] != '-':
        return False
    for i in range(8, 11):
        if not txt[i].isdecimal():
            return False
    return True


def if_phone_number_re(lst):
    ph_n = re.compile(r'\d\d\d-\d\d\d-\d\d\d')      # zwróci cały ciąg. zastosowanie () utworzy krotki.
    mo = ph_n.findall(lst)
    return mo


def find_space_and_w(txt):      # wyszuka wszystkie ' Palmer'
    sp_w = re.compile(r'\sPalmer')
    return sp_w.findall(txt)


def not_a_reg(txt):     # pomija 'a' i zwraca string
    no_a = re.compile(r'[^a]')      # ^negatywna klasa znaków. Wyklucza znaki.
    s = ''
    for val in no_a.findall(txt):
        s += val
    return s


def replace(txt):
    to_rep = re.compile(r'Niekochany')
    return to_rep.sub('*****', txt)


def replace_v2(txt):
    to_be_rep = re.compile(r'Niekochany (\w)\w*')
    return to_be_rep.sub(r'\1*****', txt)


def count_letters(txt):
    dct = {}
    for char in txt:
        dct.setdefault(char, 0)
        dct[char] = dct[char] + 1
    return dct


def find_f_name_l_name(txt):
    fname_lname = re.compile(r'imię: (\w*) nazwisko: (\w*)')
    return fname_lname.findall(txt)


message = 'Niekochany nie zdradza, niekochany chodzi dzwoniąc w kieszeni niepotrzebnym kluczem. Z bramy wychyla się ' \
          'staruszek niepokojąco podobny do Bogarta. Celuję prosto w twoje serce synu. Przecież wiesz, ' \
          'że to najmniej czuły we mnie punkt. W sąsiedniej bramie znaleziono siedemdziesięcioletnią Marilyn Monroe. ' \
          'Potrafiła wykrztusić jedynie PU PU PI DU. Niekochany nie zdradza, niekochany chodzi dzwoniąc w kieszeni ' \
          'niepotrzebnym kluczem. Jaka jest pańska narodowość? jestem pijakiem. Jestem nieślubnym dzieckiem Bogarta ' \
          'i Marilyn Monroe. 519-508-623. To ja zabiłem imię: Laurę nazwisko: Palmer.' \
          'To wszystko na ten temat. 886-438-155. Niekochany ' \
          'nie zdradza, niekochany chodzi dzwoniąc w kieszeni niepotrzebnym kluczem. Z bramy wychyla się ' \
          'staruszek niepokojąco podobny do Bogarta. Celuję prosto w twoje serce synu. Przecież wiesz, ' \
          'że to najmniej czuły we mnie punkt. W sąsiedniej bramie znaleziono siedemdziesięcioletnią Marilyn Monroe. ' \
          'Potrafiła wykrztusić jedynie PU PU PI DU. Niekochany nie zdradza, niekochany chodzi dzwoniąc w kieszeni ' \
          'niepotrzebnym kluczem. Jaka jest pańska narodowość? jestem pijakiem. Jestem nieślubnym dzieckiem Bogarta ' \
          'i Marilyn Monroe. 519-508-621. To ja zabiłem imię: Laurę nazwisko: Palmer.' \
          'To wszystko na ten temat. 886-438-152.' \
          'Niekochany nie zdradza, niekochany chodzi dzwoniąc w kieszeni niepotrzebnym kluczem. Z bramy wychyla się ' \
          'staruszek niepokojąco podobny do Bogarta. Celuję prosto w twoje serce synu. Przecież wiesz, ' \
          'że to najmniej czuły we mnie punkt. W sąsiedniej bramie znaleziono siedemdziesięcioletnią Marilyn Monroe. ' \
          'Potrafiła wykrztusić jedynie PU PU PI DU. Niekochany nie zdradza, niekochany chodzi dzwoniąc w kieszeni ' \
          'niepotrzebnym kluczem. Jaka jest pańska narodowość? jestem pijakiem. Jestem nieślubnym dzieckiem Bogarta ' \
          'i Marilyn Monroe. 519-508-627. To ja zabiłem Laurę Palmer.To wszystko na ten temat. 886-438-154.' \
          'Niekochany nie zdradza, niekochany chodzi dzwoniąc w kieszeni niepotrzebnym kluczem. Z bramy wychyla się ' \
          'staruszek niepokojąco podobny do Bogarta. Celuję prosto w twoje serce synu. Przecież wiesz, ' \
          'że to najmniej czuły we mnie punkt. W sąsiedniej bramie znaleziono siedemdziesięcioletnią Marilyn Monroe. ' \
          'Potrafiła wykrztusić jedynie PU PU PI DU. Niekochany nie zdradza, niekochany chodzi dzwoniąc w kieszeni ' \
          'niepotrzebnym kluczem. Jaka jest pańska narodowość? jestem pijakiem. Jestem nieślubnym dzieckiem Bogarta ' \
          'i Marilyn Monroe. 519-538-623. To ja zabiłem Laurę Palmer.To wszystko na ten temat. 886-438-115 ' \
          'Niekochany nie zdradza, niekochany chodzi dzwoniąc w kieszeni niepotrzebnym kluczem. Z bramy wychyla się'

phone_numbers = list()
for i in range(len(message)):
    var = message[i:i + 11]
    if is_phone_number(var):
        phone_numbers.append(var)
print(phone_numbers)

l_of_phones = if_phone_number_re(message)       # .findall -- szybsze w użyciu
print(l_of_phones)

space_word = find_space_and_w(message)
print(space_word)

no_a_v = not_a_reg(message)
print(no_a_v)

d = count_letters(message)
print(d)

replaced_wit_stars = replace(message)
print(replaced_wit_stars)

replaced_from_sec_letter = replace_v2(message)
print(replaced_from_sec_letter)

fname_lname = find_f_name_l_name(message)
print(fname_lname)
