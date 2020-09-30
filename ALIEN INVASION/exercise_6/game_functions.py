import sys
import pygame
from alien import Alien


def ship_hit(ai_settings, stats, screen, ship, aliens):
    """Respond to ship being hit by alien."""
    if stats.ships_left > 0:
        # Decrement ships_left.
        stats.ships_left -= 1
    else:
        stats.game_active = False
        sys.exit()

    # Empty the list of aliens and bullets.
    aliens.empty()

    # Create a new fleet, and center the ship.
    create_alien(ai_settings, screen, aliens)


def check_keydown_events(event, ship):
    """Reakcja na naciśnięcie klawisza."""
    if event.key == pygame.K_RIGHT:
        ship.moving_right = True
    elif event.key == pygame.K_LEFT:
        ship.moving_left = True
    elif event.key == pygame.K_q:
        sys.exit()


def check_keyup_events(event, ship):
    """Reakcja na zwolnienie klawisza."""
    if event.key == pygame.K_RIGHT:
        ship.moving_right = False
    elif event.key == pygame.K_LEFT:
        ship.moving_left = False


def check_events(ai_settings, screen, ship):
    """Reakcja na zdarzenia generowane przez klawiaturę i mysz."""
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            check_keydown_events(event, ship)
        elif event.type == pygame.KEYUP:
            check_keyup_events(event, ship)


def update_screen(ai_settings, screen, ship, aliens):
    """Uaktualnienie obrazów na ekranie i przejście do nowego ekranu."""
    # Odświeżenie ekranu w trakcie każdej iteracji pętli.
    screen.fill(ai_settings.bg_color)

    ship.blitme()
    aliens.draw(screen)

    # Wyświetlenie ostatnio zmodyfikowanego ekranu.
    pygame.display.flip()


def create_alien(ai_settings, screen, aliens):
    """Utworzenie obcego i umieszczenie go w rzędzie."""
    alien = Alien(ai_settings, screen)
    aliens.add(alien)


def update_aliens(ai_settings, stats, screen, aliens, ship):
    """Sprawdzenie, czy flota znajduje się przy krawędzi ekranu, a następnie uaktualnienie położenia wszystkich obcych
    we flocie."""
    check_fleet_edges(ai_settings, stats, screen, ship, aliens)
    aliens.update()

    collisions = pygame.sprite.spritecollideany(ship, aliens)

    if collisions:
        for alien in aliens.copy():
            aliens.remove(alien)

    if len(aliens) == 0:
        # Pozbycie się istniejących pocisków i utworzenie nowej floty.
        create_alien(ai_settings, screen, aliens)


def check_fleet_edges(ai_settings, stats, screen, ship, aliens):
    """Odpowiednia reakcja, gdy obcy dotrze do krawędzi ekranu."""
    screen_rect = screen.get_rect()

    for alien in aliens.sprites():
        alien.rect.y += ai_settings.fleet_drop_speed

    for alien in aliens.copy():
        if alien.rect.bottom >= screen_rect.bottom:
            ship_hit(ai_settings, stats, screen, ship, aliens)
            break


