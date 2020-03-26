import sys
import pygame
from bullet import Bullet
from alien import Alien


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


def update_screen(ai_settings, screen, ship, aliens, bullets):
    """ Uaktualnienie obrazów na ekranie i przejście do nowego ekranu. """
    # Odświeżenie ekranu w trakcie każdej iteracji pętli
    screen.fill(ai_settings.bg_color)
    # Ponowne wyświetlenie wszystkich pocisków pod warstwami statku kosmicznego
    # i obcych
    for bullet in bullets.sprites():
        bullet.draw_bullet()

    ship.blitme()  # Wyświetlenie statku
    # Metoda draw() wywoływana jest dla grupy
    aliens.draw(screen)  # Wyświetlenie na ekranie każdego obcego, znajdującego się w grupie

    # Wyświetlenie ostatnio zmodyfikowanego ekranu
    pygame.display.flip()


def update_bullets(ai_settings, screen, ship, aliens, bullets):
    """ Uaktualnienie położenia pocisków i usunięcie niewidocznych """
    # Uaktualnienie położenia
    bullets.update()
    # Usunięcie pocisków, które znajdują się poza ekranem
    for bullet in bullets.copy():
        if bullet.rect.bottom <= 0:
            bullets.remove(bullet)
        print(len(bullets))
    # Sprawdzenie, czy którykolwiek pocisk trafił obcego
    # Jeżeli tak, usuwamy zarówno pocisk jak i obcego
    collisions = pygame.sprite.groupcollide(bullets, aliens, True, True)

    if len(aliens) == 0:
        # Pozbycie się aktualnych pocisków i utworzenie nowej floty
        bullets.empty()
        create_fleet(ai_settings, screen, ship, aliens)


def fire_bullet(ai_settings, screen, ship, bullets):
    """ Wystrzelenie pocisku, jeśli nie przekroczono ustalonego limitu. """
    # Utworzenie nowego pocisku i dodanie go do grupy pocisków
    # jeśli na ekranie jest mniej niż 3 pociski
    if len(bullets) < ai_settings.bullets_allowed:
        new_bullet = Bullet(ai_settings, screen, ship)
        bullets.add(new_bullet)


def create_fleet(ai_settings, screen, ship, aliens):
    """ Utworzenie pełnej floty obcych """
    # Utworzenie obcego i ustalenie liczby obcych, którzy zmieszczą się w rzędzie
    # Odległość między poszczególnymi obcymi jest równa szerokości obcego
    alien = Alien(ai_settings, screen)
    number_aliens_x = get_number_aliens(ai_settings, alien.rect.width)
    number_rows = get_number_rows(ai_settings, ship.rect.height, alien.rect.height)
    # Utworzenie floty obcych
    for row_number in range(number_rows):
        for alien_number in range(number_aliens_x):
            create_alien(ai_settings, screen, aliens, alien_number, row_number)


def get_number_aliens(ai_settings, alien_width):
    # Ustalenie liczby obcych, którzy zmieszczą się w rzędzie
    available_space_x = ai_settings.screen_width - 2 * alien_width
    number_aliens_x = int(available_space_x / (2 * alien_width))
    return number_aliens_x


def create_alien(ai_settings, screen, aliens, alien_number, row_number):
    """ Utworzenie obcego i umieszczenie go w rzędzie """
    alien = Alien(ai_settings, screen)
    alien_width = alien.rect.width
    alien.x = alien_width + 2 * alien_width * alien_number
    alien.rect.x = alien.x
    alien.rect.y = alien.rect.height + 2 * alien.rect.height * row_number
    aliens.add(alien)


def get_number_rows(ai_settings, ship_height, alien_height):
    """ Ustalenie ile rzędów obcych zmieści się na ekranie """
    available_space_y = (ai_settings.screen_height - (3 * alien_height) - ship_height)
    number_rows = int(available_space_y / (2 * alien_height))
    return number_rows


def update_aliens(ai_settings, aliens):
    """ Sprawdzenie, czy flota znajduje się przy krawędzi ekranu.
        Uaktualnienie położenia wszystkich obcych we flocie """
    check_fleet_edges(ai_settings, aliens)
    aliens.update()


def check_fleet_edges(ai_settings, aliens):
    """ Odpowiednia reakcja, gdy obcy dotrze do krawędzi ekranu """
    for alien in aliens.sprites():
        if alien.check_edges():
            change_fleet_direction(ai_settings, aliens)
            break


def change_fleet_direction(ai_settings, aliens):
    """ Przesunięcie całej floty w dół i zmiana kierunku poruszania"""
    for alien in aliens.sprites():
        alien.rect.y += ai_settings.fleet_drop_speed
    ai_settings.fleet_direction *= -1
