"""" Przechowywanie ustawień gry """


class Settings:
    """ Klasa przeznaczona do przechowywania wszystkich ustawień gry. """

    def __init__(self):
        """ Inicjalizacja ustawień gry. """
        # Ustawienia ekranu
        self.screen_width = 1200
        self.screen_height = 800
        self.bg_color = (72, 61, 139)

        # Ustawienia dotyczące statku
        self.ship_speed_factor = 1.5

        # Ustawienia dotyczące pocisku
        self.bullet_speed_factor = 1
        self.bullet_width = 3
        self.bullet_height = 15
        self.bullet_color = 255, 255, 0
        self.bullets_allowed = 3
