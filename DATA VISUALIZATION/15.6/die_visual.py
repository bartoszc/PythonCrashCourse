from die import Die
import pygal

# Utworzenie kości typu D6.
die = Die()  # 1.

# Wykonanie pewnej liczby rzutów i umieszczenie wyników na liście.
results = [die.roll() for roll_num in range(1000)]

# Analiza wyników.
frequencies = [results.count(value) for value in range(1, die.num_sides+1)]

# Wizualizacja wyników.
hist = pygal.Bar()
hist.force_uri_protocol = 'http'

hist.title = "Wynik rzucania pojedynczą kością D6 tysiąc razy."
hist.x_labels = list(range(1, die.num_sides+1))
hist.x_title = "Wynik"
hist.y_title = "Częstotliwość występowania wartości"
hist.add('D6', frequencies)
hist.render_to_file('die_visual.svg')
