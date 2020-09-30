from die import Die
import pygal

# Utworzenie dwóch kości do gry typu D6.
die_1 = Die()
die_2 = Die()

# Wykonanie pewnej liczby rzutów i umieszczenie wyników na liście.
results = [die_1.roll() + die_2.roll() for roll_num in range(1000)]

# Analiza wyników.
max_result = die_1.num_sides + die_2.num_sides
frequencies = [results.count(value) for value in range(2, max_result+1)]

# Wizualizacja wyników.
hist = pygal.Bar()
hist.force_uri_protocol = 'http'

hist.title = "Wynik rzucania dwiema kośćmi D6 tysiąc razy."
hist.x_labels = list(range(2, max_result+1))
hist.x_title = "Wynik"
hist.y_title = "Częstotliwość występowania wartości"
hist.add('D6 + D6', frequencies)
hist.render_to_file('dice_visual.svg')
