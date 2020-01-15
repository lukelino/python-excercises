#! python3
# Tworzy quiz wraz z pytaniami i odpowiedziami ułożonymi w losowej kolejności wraz z odpowiedziami.
"""
    Utworzenie 35 quizów,
    Dla każdego quizu 50 pytań losowo ułożonych,
    Dla każdego pytania losowo ułożone odpowiedzi,
    Zapis quizów w 35 plikach,
    Utworzenie odpowiedzi do wygenerowanych 35 plików txt,
    ----
    Słownik do przechowywania pary klucz: wartość --> Stan: Stolica
    metody open(), write(), close()
    random.shuffle() --> losowość pytań i odpowiedzi
"""

import capitals_module
import random

capitals = capitals_module.capitals
encoding = 'utf-8'
# Wygenerowanie 35 plików
for quizNum in range(35):
    # Utworzenie plików quizu i odpowiedzi na pytania.
    quizFile = open(f'capitals_quiz{quizNum + 1}.txt', 'w', encoding=encoding)
    answerKeyFile = open(f'capitals_quiz_answers{quizNum + 1}.txt', 'w', encoding=encoding)

    # Zapis nagłówka quizu.
    quizFile.write('Imię i nazwisko:\n\nData:\n\n')
    quizFile.write(f'Quiz stolic stanów (Quiz {quizNum + 1})'.center(20))
    quizFile.write('\n\n')


# Losowe ustalenie kolejności stanów.
states = list(capitals.keys())
random.shuffle(states)

# Iteracja przez 50 stanów i utworzenie pytania dotyczącego każdego z nich.
for questionNum in range(50):
    # Przygotowanie prawidłowych i nieprawidłowych odpowiedzi
    correctAnswer = capitals[states[questionNum]]
    wrongAnswers = list(capitals.values())
    del wrongAnswers[wrongAnswers.index(correctAnswer)]
    wrongAnswers = random.sample(wrongAnswers, 3)
    answerOptions = wrongAnswers + [correctAnswer]
    random.shuffle(answerOptions)

    # Zapis pytania i odpowiedzi w pliku quizu
    quizFile.write(f'{questionNum + 1}: Co jest stolicą stanu {states[questionNum]}?\n')
    for i in range(4):
        quizFile.write('    %s. %s\n' % ('ABCD'[i], answerOptions[i]))
        quizFile.write('\n')

        # Zapis odpowiedzi w pliku
        answerKeyFile.write('%s. %s\n' % (questionNum + 1, 'ABCD'[answerOptions.index(correctAnswer)]))

quizFile.close()
answerKeyFile.close()
