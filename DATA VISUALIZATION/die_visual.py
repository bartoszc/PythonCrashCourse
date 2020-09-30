from die import Die
import pygal

# Utworzenie kości typu D6.
die = Die()  # 1.

# Wykonanie pewnej liczby rzutów i umieszczenie wyników na liście.
results = []
for roll_num in range(1000):  # 2.
    result = die.roll()
    results.append(result)
#%%
# Analiza wyników.
frequencies = []
for value in range(1, die.num_sides+1):
    frequency = results.count(value)
    frequencies.append(frequency)

# Wizualizacja wyników.
hist = pygal.Bar()
hist.force_uri_protocol = 'http'

hist.title = "Wynik rzucania pojedynczą kością D6 tysiąc razy."
hist.x_labels = ['1', '2', '3', '4', '5', '6']
hist.x_title = "Wynik"
hist.y_title = "Częstotliwość występowania wartości"
hist.add('D6', frequencies)
hist.render_to_file('die_visual.svg')


# %%
