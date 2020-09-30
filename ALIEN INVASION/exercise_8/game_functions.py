import sys
import pygame
from bullet import Bullet
from alien import Alien
from time import sleep


def check_play_button(ai_settings, screen, stats, play_button, ship, aliens, bullets, mouse_x, mouse_y):
    """Rozpoczęcie nowej gry po kliknięciu przycisku Gra przez użytkownika."""
    button_clicked = play_button.rect.collidepoint(mouse_x, mouse_y)
    if button_clicked and not stats.game_active:
        # Wyzerowanie danych statystycznych gry.
        ai_settings.initialize_dynamic_settings()
        stats.reset_stats()
        stats.game_active = True

        # Ukrycie kursora myszy.
        pygame.mouse.set_visible(False)

        # Usunięcie zawartości list aliens i bullets.
        aliens.empty()
        bullets.empty()

        # Utworzenie nowej floty i wyśrodkowanie statku.
        create_alien(ai_settings, screen, aliens)


def check_keydown_events(event, ai_settings, screen, ship, bullets):
    """Reakcja na naciśnięcie klawisza."""
    if event.key == pygame.K_UP:
        ship.moving_up = True
    elif event.key == pygame.K_DOWN:
        ship.moving_down = True
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
    if event.key == pygame.K_UP:
        ship.moving_up = False
    elif event.key == pygame.K_DOWN:
        ship.moving_down = False


def check_events(ai_settings, screen, stats, play_button, ship, aliens, bullets):
    """Reakcja na zdarzenia generowane przez klawiaturę i mysz."""
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        elif event.type == pygame.MOUSEBUTTONDOWN:
            mouse_x, mouse_y = pygame.mouse.get_pos()
            check_play_button(ai_settings, screen, stats, play_button, ship, aliens, bullets, mouse_x, mouse_y)
        elif event.type == pygame.KEYDOWN:
            check_keydown_events(event, ai_settings, screen, ship, bullets)
        elif event.type == pygame.KEYUP:
            check_keyup_events(event, ship)


def update_screen(ai_settings, screen, stats, ship, aliens, bullets, play_button):
    """Uaktualnienie obrazów na ekranie i przejście do nowego ekranu."""
    # Odświeżenie ekranu w trakcie każdej iteracji pętli.
    screen.fill(ai_settings.bg_color)

    # Ponowne wyświetlenie wszystkich pocisków pod warstwami statku kosmicznego i obcych
    for bullet in bullets.sprites():
        bullet.draw_bullet()

    ship.blitme()
    aliens.draw(screen)

    # Wyświetlenie przycisku tylko wtedy, gdy gra jest nieaktywna.
    if not stats.game_active:
        play_button.draw_button()

    # Wyświetlenie ostatnio zmodyfikowanego ekranu.
    pygame.display.flip()


def update_bullets(ai_settings, screen, ship, aliens, bullets, stats):
    """Uaktualnienie położenia pocisków i usunięcie tych niewidocznych na ekranie."""
    # Uaktualnienie położenia pocisków.
    bullets.update()

    # Usunięcie pocisków, które znajdują się poza ekranem.
    for bullet in bullets.copy():
        if bullet.rect.right > 1280:
            if stats.bullets_left > 0:
                # Decrement ships_left.
                stats.bullets_left -= 1
            else:
                stats.game_active = False
                pygame.mouse.set_visible(True)
            bullets.remove(bullet)

    check_bullet_alien_collisions(ai_settings, screen, ship, aliens, bullets)


def check_bullet_alien_collisions(ai_settings, screen, ship, aliens, bullets):
    """Reakcja na kolizję między pociskiem i obcym."""
    # Usunięcie wszystkich pocisków i obcych, między którymi doszło do kolizji.
    collisions = pygame.sprite.groupcollide(bullets, aliens, True, True)

    if len(aliens) == 0:
        # Pozbycie się istniejących pocisków i utworzenie nowej floty.
        bullets.empty()
        ai_settings.increase_speed()
        create_alien(ai_settings, screen, aliens)


def create_alien(ai_settings, screen, aliens):
    """Utworzenie obcego i umieszczenie go w rzędzie."""
    alien = Alien(ai_settings, screen)
    aliens.add(alien)


def update_aliens(ai_settings, stats, screen, ship, aliens, bullets):
    """Sprawdzenie, czy flota znajduje się przy krawędzi ekranu, a następnie uaktualnienie położenia wszystkich obcych
    we flocie."""
    check_fleet_edges(ai_settings, aliens, screen)
    aliens.update()


def check_fleet_edges(ai_settings, aliens, screen):
    """Odpowiednia reakcja, gdy obcy dotrze do krawędzi ekranu."""
    screen_rect = screen.get_rect()
    for alien in aliens.sprites():
        alien.rect.y += ai_settings.fleet_drop_speed
        if alien.check_edges():
            change_fleet_direction(ai_settings, aliens)
            break


def change_fleet_direction(ai_settings, aliens):
    """Przesunięcie całej floty w dół i zmiana kierunku, w którym się ona porusza."""
    for alien in aliens.sprites():
        alien.rect.y += ai_settings.fleet_drop_speed
    ai_settings.fleet_direction *= -1





