#! python3
""" Allows to assign a value to a variable and store it in a dictionary """


def check_if_var(user_string):
    """ Check if expression is a variable declaration and assignment """
    tst = user_string.split('=')
    if '=' in user_string and user_string.count('=') == 1 and tst[0].isalpha():
        return True
    elif '=' in user_string and user_string.count('=') != 1:
        print('Invalid syntax')
        return False


def store_var_in_dct(values, user_dct):
    key_val = values.split('=')
    if key_val[0] not in user_dct and key_val[1].isdigit():                         # key not in dct
        user_dct.setdefault(key_val[0], int(key_val[1]))
    elif key_val[0] in user_dct and key_val[1].isdigit():                           # key in dct
        user_dct.update({key_val[0]: int(key_val[1])})
    elif key_val[0] not in user_dct.keys() and key_val[1] in user_dct.keys():       # key not in dct and key = key
        user_dct.setdefault(key_val[0], user_dct[f'{key_val[1]}'])
    elif key_val[0] in user_dct.keys() and key_val[1] in user_dct.keys():           # key in dct and key = key
        user_dct.update({key_val[0]: user_dct[f'{key_val[1]}']})
    elif key_val[0] not in user_dct.keys() and key_val[1].isalpha() and key_val[1] not in user_dct.keys():
        print('Invalid assignment')
    elif key_val[0] in user_dct.keys() and key_val[1].isalpha() and key_val[1] not in user_dct.keys():
        print('Invalid assignment')
    return user_dct


var_dct = {}

while True:

    numbers = input('>').split()
    s = ''.join(numbers)
    if check_if_var(s):
        var_dct = store_var_in_dct(s, var_dct)
        print(var_dct)
    else:
        continue
