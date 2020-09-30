import sys
import pygame
from bullet import Bullet
from alien import Alien


def check_keydown_events(event, ai_settings, screen, ship, bullets):
    """Reakcja na naciśnięcie klawisza."""
    if event.key == pygame.K_RIGHT:
        ship.moving_right = True
    elif event.key == pygame.K_LEFT:
        ship.moving_left = True
    elif event.key == pygame.K_SPACE:
        fire_bullet(ai_settings, screen, ship, bullets)
    elif event.key == pygame.K_q:
        sys.exit()


def fire_bullet(ai_settings, screen, ship, bullets):
    """Wystrzelenie pocisku, jeśli nie przekroczono ustalonego limitu."""
    # Utworzenie nowego pocisku i dodanie go do grupy pocisków.
    if len(bullets) < ai_settings.bullets_allowed:
        new_bullet = Bullet(ai_settings, screen, ship)
        bullets.add(new_bullet)


def check_keyup_events(event, ship):
    """Reakcja na zwolnienie klawisza."""
    if event.key == pygame.K_RIGHT:
        ship.moving_right = False
    elif event.key == pygame.K_LEFT:
        ship.moving_left = False


def check_events(ai_settings, screen, ship, bullets):
    """Reakcja na zdarzenia generowane przez klawiaturę i mysz."""
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            check_keydown_events(event, ai_settings, screen, ship, bullets)
        elif event.type == pygame.KEYUP:
            check_keyup_events(event, ship)


def update_screen(ai_settings, screen, ship, aliens, bullets):
    """Uaktualnienie obrazów na ekranie i przejście do nowego ekranu."""
    # Odświeżenie ekranu w trakcie każdej iteracji pętli.
    screen.fill(ai_settings.bg_color)

    # Ponowne wyświetlenie wszystkich pocisków pod warstwami statku kosmicznego i obcych
    for bullet in bullets.sprites():
        bullet.draw_bullet()

    ship.blitme()
    aliens.draw(screen)

    # Wyświetlenie ostatnio zmodyfikowanego ekranu.
    pygame.display.flip()


def update_bullets(ai_settings, screen, aliens, bullets):
    """Uaktualnienie położenia pocisków i usunięcie tych niewidocznych na ekranie."""
    # Uaktualnienie położenia pocisków.
    bullets.update()

    # Usunięcie pocisków, które znajdują się poza ekranem.
    for bullet in bullets.copy():
        if bullet.rect.bottom <= 0:
            bullets.remove(bullet)

    collisions = pygame.sprite.groupcollide(bullets, aliens, True, True)

    if len(aliens) == 0:
        # Pozbycie się istniejących pocisków i utworzenie nowej floty.
        bullets.empty()
        create_alien(ai_settings, screen, aliens)


def create_alien(ai_settings, screen, aliens):
    """Utworzenie obcego i umieszczenie go w rzędzie."""
    alien = Alien(ai_settings, screen)
    aliens.add(alien)


def update_aliens(ai_settings, aliens):
    """Sprawdzenie, czy flota znajduje się przy krawędzi ekranu, a następnie uaktualnienie położenia wszystkich obcych
    we flocie."""
    check_fleet_edges(ai_settings, aliens)
    aliens.update()


def check_fleet_edges(ai_settings, aliens):
    """Odpowiednia reakcja, gdy obcy dotrze do krawędzi ekranu."""
    for alien in aliens.sprites():
        alien.rect.y += ai_settings.fleet_drop_speed

    for alien in aliens.copy():
        if alien.rect.bottom > 800:
            aliens.remove(alien)





