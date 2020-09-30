class Settings:
    """Klasa przeznaczona do przechowywania wszystkich ustawień gry."""
    def __init__(self):
        """Inicjalizacja ustawień gry."""
        # Ustawienia ekranu.
        self.screen_width = 1200
        self.screen_height = 800
        self.bg_color = (230, 230, 230)

        # Ustawienia dotyczące statku
        self.ship_speed_factor = 1.5
        self.ship_limit = 3

        # Ustawienia dotyczące obcego.
        self.alien_speed_factor = 2
        self.fleet_drop_speed = 1
        # Wartość fleet_direction wynosząca 1 oznacza prawo, natomiast -1 oznacza lewo.
        self.fleet_direction = 0


