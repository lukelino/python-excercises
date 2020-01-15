import random
import capitals_module
import shelve

capitals = capitals_module.capitals


def create_answers():
    """Przygotowanie prawidłowych i nieprawidłowych odpowiedzi"""
    states = list(capitals.keys())
    random.shuffle(states)
    correct_answer, answer_options = None, None
    for questionNum in range(50):                                   # Czy tutaj potrzebna jest pętla????
        correct_answer = capitals[states[questionNum]]
        wrong_answers = list(capitals.values())
        del wrong_answers[wrong_answers.index(correct_answer)]     # usuń z listy niewłaściwych odpowiedzi tę właściwą
        wrong_answers = random.sample(wrong_answers, 3)       # zamerdaj i wybierz 3 z listy
        answer_options = wrong_answers + [correct_answer]      # do tej pory correct_answer nie był listą
        random.shuffle(answer_options)
    return correct_answer, answer_options


def number_of_players():
    """Ustala liczbe graczy"""
    while True:
        try:
            how_many_players = int(input('Ilu graczy:'))
            return how_many_players
        except ValueError:
            print('To nie liczba')


def names_of_players(players_num):
    """Imiona poszczególnych graczy"""
    names = {}      # Słownik gracz:punkty
    for num in range(players_num):
        names.setdefault(input(f'Podaj imię gracza {num + 1}: ').title(), 0)     # Początkowa wartość punktów = 0
    return names


def save_results(dct_with_results, time_stamp):
    """Zapis stanu gry: Gracz:wynik"""
    data_file = shelve.open('game_results')
    data_file[str(time_stamp)] = dct_with_results
    data_file.close()


def read_saved_results():
    data_file_path = r'D:\Py\085_a_Game_States_Capitals\game_results'
    data = shelve.open(data_file_path)
    return data


def del_saved_results():
    """Kasuje zapisane punkty"""
    pass


def new_or_old_game():
    """Można wczytać grę, lub rozpocząć nową"""
    pass
