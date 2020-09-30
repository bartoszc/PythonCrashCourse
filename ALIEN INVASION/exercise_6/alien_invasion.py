import pygame
from settings import Settings
from ship import Ship
import game_functions as gf
from pygame.sprite import Group
from alien import Alien
from game_stats import GameStats


def run_game():
    # Inicjalizacja gry i utworzenie obiektu ekranu.
    pygame.init()
    ai_settings = Settings()
    screen = pygame.display.set_mode((ai_settings.screen_width, ai_settings.screen_height))
    pygame.display.set_caption("Inwazja obcych")

    # Utworzenie egzemplarza przeznaczonego do przechowywania danych
    # statystycznych dotyczących gry.
    stats = GameStats(ai_settings)

    # Utworzenie obcego.
    alien = Alien(ai_settings, screen)

    # Utworzenie statku obcych
    ship = Ship(ai_settings, screen)

    # Utworzenie grupy przeznaczonej do przechowywania pocisków
    aliens = Group()

    # Rozpoczęcie pętli głównej gry.
    while True:
        gf.check_events(ai_settings, screen, ship)

        if stats.game_active:
            ship.update()
            gf.update_aliens(ai_settings, stats, screen, aliens, ship)
        gf.update_screen(ai_settings, screen, ship, aliens)


run_game()
