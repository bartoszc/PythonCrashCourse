from random_walk import RandomWalk
import pygal

# Tworzenie nowego błądzenia losowego, dopóki program pozostaje aktywny.

rw = RandomWalk(500)
rw.fill_walk()

# Wizualizacja wyników.
hist = pygal.Bar()
hist.force_uri_protocol = 'http'

hist.title = "Błądzenie losowe."
hist.x_labels = [str(x) for x in rw.x_values]
hist.x_title = "Wynik"
hist.y_title = "Częstotliwość występowania wartości"
hist.add('RW', rw.y_values)
hist.render_to_file('rw_v.svg')