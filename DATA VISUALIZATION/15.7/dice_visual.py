from die import Die
import pygal

# Utworzenie dwóch kości do gry typu D6.
die_1 = Die(8)
die_2 = Die(8)

# Wykonanie pewnej liczby rzutów i umieszczenie wyników na liście.
results = []
for roll_num in range(1000000):  # 2.
    result = die_1.roll() + die_2.roll()
    results.append(result)

# Analiza wyników.
frequencies = []
max_result = die_1.num_sides + die_2.num_sides
for value in range(2, max_result+1):
    frequency = results.count(value)
    frequencies.append(frequency)

# Wizualizacja wyników.
hist = pygal.Bar()
hist.force_uri_protocol = 'http'

hist.title = "Wynik rzucania dwiema kośćmi D6 tysiąc razy."
hist.x_labels = list(range(2, max_result+1))
hist.x_title = "Wynik"
hist.y_title = "Częstotliwość występowania wartości"
hist.add('D8 + D8', frequencies)
hist.render_to_file('dice_visual.svg')
