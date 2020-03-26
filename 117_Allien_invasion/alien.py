import pygame
from pygame.sprite import Sprite


class Alien(Sprite):
    """ Klasa przedstawiająca pojedynczego obcego"""
    def __init__(self, ai_settings, screen):
        """ Inicjalizacja obcego o zdefiniowanie jego położenia początkowego """
        super().__init__()
        self.screen = screen
        self.ai_settings = ai_settings

        # Wczytanie obrazu obcego i zdefiniowanie jego atrybutu rect
        self.image = pygame.image.load('images/alien.bmp')
        self.rect = self.image.get_rect()

        # Umieszczenie nowego obcego w pobliżu lewego górnego rogu ekranu
        self.rect.x = self.rect.width
        self.rect.y = self.rect.height

        # Przechowywanie dokładnego położenia obcego
        self.x = float(self.rect.x)

    def blitme(self):
        """ Wyświetlenie obcego w jego aktualnym położeniu """
        self.screen.blit(self.image, self.rect)
