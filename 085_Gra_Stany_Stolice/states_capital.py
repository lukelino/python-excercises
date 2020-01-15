#! python3
# Tworzy quiz wraz z pytaniami i odpowiedziami ułożonymi w losowej kolejności wraz z odpowiedziami.
"""
    Utworzenie quizu,
    Dla każdego quizu 50 pytań losowo ułożonych,
    Dla każdego pytania losowo ułożone odpowiedzi,
    Zapis quizu w pliku,
    Utworzenie odpowiedzi do wygenerowanych 35 plików txt,
    ----
    Słownik do przechowywania pary klucz: wartość --> Stan: Stolica
    metody open(), write(), close()
    random.shuffle() --> losowość pytań i odpowiedzi
"""

import capitals_module
import random


def prepare_a_correct_answer(capitals_states_dct):
    """ Przygotowanie właściwych odpowiedzi """
    capitals = list(capitals_states_dct.values())
    states = list(capitals_states_dct.keys())
    for quizNum in range(50):
        correct_answer = capitals_states_dct[states[quizNum]]
        wrong_answers = capitals
        del wrong_answers[wrong_answers.index(correct_answer)]
        wrong_answers = random.sample(wrong_answers, 3)
        answer_options = wrong_answers + [correct_answer]
        random.shuffle(answer_options)


capitals_states = capitals_module.capitals

prepare_a_correct_answer(capitals_states)
