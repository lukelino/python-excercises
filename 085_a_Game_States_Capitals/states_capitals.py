#! python3

import game_functions
import os
import datetime


results = game_functions.read_saved_results()
for k, v in results.items():
    print(f'{k} --> {v}')


# Ilu graczy
playersNum = game_functions.number_of_players()
list_of_players = game_functions.names_of_players(playersNum)

# Gra
status = True
while status:
    state = None
    abcd = 'ABCD'
    print(list_of_players)
    for player in list_of_players:
        correctAnswer, answerOptions = game_functions.create_answers()  # Przygotowanie zestawu pytań

        for k, v in game_functions.capitals.items():  # Przypisanie odpowiedzi pytania
            if correctAnswer == v:
                state = k

        print(f'\n{player}, co jest stolicą stanu {state}:')
        dct = {}        # Słownik do przechowywania wszystkich klucz:wartość odpowiedź:stolica
        for i in range(4):      # wyświetlenie wszystkich opcji odpowiedzi
            print(f"{abcd[i]}: {answerOptions[i]}")
            dct.setdefault(abcd[i], answerOptions[i])
        answer = input('?:')

        if answer.lower() in abcd.lower():
            if dct[answer.upper()] == correctAnswer:
                print(f'\nTak, stolicą {state.upper()} jest {correctAnswer.upper()}.')
                list_of_players[player] += 1        # Dodaje punkt przy dobrej odpowiedzi
            else:
                print(f'\nNie, {dct[answer.upper()]} nie jest stolicą {state}.\nStolicą {state.upper()} '
                      f'jest {correctAnswer.upper()}.')
                list_of_players[player] -= 1        # Odejmuje punkt przy błędnej odpowiedzi
        elif answer == 'q':
            status = False
            break
        else:
            print('Żartujesz?\nDo wyboru masz [Q] - wyjście lub A, B, C, D.')
time = datetime.datetime.now().replace(microsecond=0)
game_functions.save_results(list_of_players, time)

print(list_of_players)
print('Koniec')

# TODO: Zapis/Odczyt stanu gry dla każdego gracza. Moduł 'shelve'
