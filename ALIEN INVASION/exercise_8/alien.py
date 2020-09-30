import pygame
from pygame.sprite import Sprite


class Alien(Sprite):
    """Klasa przedstawiająca pojedynczego obcego we flocie."""
    def __init__(self, ai_settings, screen):
        """Inicjalizacja obcego i zdefiniowanie jego położenia początkowego."""
        super(Alien, self).__init__()
        self.screen = screen
        self.ai_settings = ai_settings

        # Wczytanie obrazu obcego i zdefiniowanie jego atrybutu rect.
        self.image = pygame.image.load('images/rectangle.bmp')
        self.rect = self.image.get_rect()

        # Umieszczenie nowego obcego w pobliżu lewego górnego rogu ekranu.
        screen_rect = self.screen.get_rect()
        self.rect.x = screen_rect.width - self.rect.width

        # Przechowywanie dokładnego położenia obcego.
        self.y = float(self.rect.y)

    def blitme(self):
        """Wyświetlenie obcego w jego aktualnym położeniu."""
        self.screen.blit(self.image, self.rect)

    def update(self):
        """Przesunięcie obcego w prawo lub w lewo."""
        self.y += (self.ai_settings.alien_speed_factor * self.ai_settings.fleet_direction)
        self.rect.y = self.y

    def check_edges(self):
        """Zwraca wartość True, jeśli obcy znajduje się przy krawędzi ekranu."""
        screen_rect = self.screen.get_rect()
        if self.rect.bottom >= screen_rect.bottom:
            return True
        elif self.rect.top <= 0:
            return True
