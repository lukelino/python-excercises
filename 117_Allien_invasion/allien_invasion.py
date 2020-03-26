#! python3
""" Gra 'inwazja obcych'. Gracz kontroluje statek kosmiczny u dołu ekranu. """

import pygame
from pygame.sprite import Group
import settings
from ship import Ship
import game_functions as gf


def run_game():
    # Inicjalizacja gry i utworzenie ekranu.
    pygame.init()
    ai_settings = settings.Settings()
    screen = pygame.display.set_mode((ai_settings.screen_width, ai_settings.screen_height))     # KROTKA
    pygame.display.set_caption('Inwazja obcych')

    # Utworzenie statku kosmicznego
    ship = Ship(ai_settings, screen)
    # Utworzenie grupy przeznaczonej do przechowywania pocisków.
    bullets = Group()
    # Utworzenie grupy do przechowywania obcych
    aliens = Group()

    # Utworzenie floty obcych
    gf.create_fleet(ai_settings, screen, ship, aliens)

    # Rozpoczęcie pętli głównej gry.
    while True:
        # Oczekiwanie na naciśnięcie klawisza lub przycisku myszy
        gf.check_events(ai_settings, screen, ship, bullets)
        ship.update()
        gf.update_bullets(ai_settings, screen, ship, aliens, bullets)
        gf.update_aliens(ai_settings, aliens)
        gf.update_screen(ai_settings, screen, ship, aliens, bullets)


run_game()
