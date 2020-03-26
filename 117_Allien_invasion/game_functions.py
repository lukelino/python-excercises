import sys
import pygame
from bullet import Bullet


def check_keydown_events(event, ai_settings, screen, ship, bullets):
    """ Reakcja na naciśnięcie klawisza. """
    if event.key == pygame.K_RIGHT:
        # przesunięcie statku w prawo
        ship.moving_right = True
    elif event.key == pygame.K_LEFT:
        # przesunięcie statku w lewo
        ship.moving_left = True
        # strzał
    elif event.key == pygame.K_SPACE:
        fire_bullet(ai_settings, screen, ship, bullets)
        # wyjście z gry po naciśnięciu 'Q'
    elif event.key == pygame.K_q:
        sys.exit()


def check_keyup_events(event, ship):
    """ Reakcja na zwolnienie klawisza. """
    if event.key == pygame.K_RIGHT:
        ship.moving_right = False
    elif event.key == pygame.K_LEFT:
        ship.moving_left = False


def check_events(ai_settings, screen, ship, bullets):
    """ Reakcja na zdarzenia generowane przez klawiaturę i mysz. """
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            check_keydown_events(event, ai_settings, screen, ship, bullets)
        elif event.type == pygame.KEYUP:
            check_keyup_events(event, ship)


def update_screen(ai_settings, screen, ship, alien, bullets):
    """ Uaktualnienie obrazów na ekranie i przejście do nowego ekranu. """
    # Odświeżenie ekranu w trakcie każdej iteracji pętli
    screen.fill(ai_settings.bg_color)
    # Ponowne wyświetlenie wszystkich pocisków pod warstwami statku kosmicznego
    # i obcych
    for bullet in bullets.sprites():
        bullet.draw_bullet()

    ship.blitme()   # Wyświetlenie statku
    alien.blitme()      # Wyświetlenie obcego
    
    # Wyświetlenie ostatnio zmodyfikowanego ekranu
    pygame.display.flip()


def update_bullets(bullets):
    """ Uaktualnienie położenia pocisków i usunięcie niewidocznych """
    # Uaktualnienie położenia
    bullets.update()
    # Usunięcie pocisków, które znajdują się poza ekranem
    for bullet in bullets.copy():
        if bullet.rect.bottom <= 0:
            bullets.remove(bullet)
        print(len(bullets))


def fire_bullet(ai_settings, screen, ship, bullets):
    """ Wystrzelenie pocisku, jeśli nie przekroczono ustalonego limitu. """
    # Utworzenie nowego pocisku i dodanie go do grupy pocisków
    # jeśli na ekranie jest mniej niż 3 pociski
    if len(bullets) < ai_settings.bullets_allowed:
        new_bullet = Bullet(ai_settings, screen, ship)
        bullets.add(new_bullet)
