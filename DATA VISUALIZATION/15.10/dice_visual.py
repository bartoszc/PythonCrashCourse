from die import Die
import matplotlib.pyplot as plt

# Utworzenie dwóch kości do gry typu D6.
die_1 = Die()
die_2 = Die()

# Wykonanie pewnej liczby rzutów i umieszczenie wyników na liście.
results = []
for roll_num in range(1, 12):  # 2.
    result = die_1.roll() + die_2.roll()
    results.append(result)

# Analiza wyników.
frequencies = []
max_result = die_1.num_sides + die_2.num_sides
for value in range(2, max_result+1):
    frequency = results.count(value)
    frequencies.append(frequency)

# Zdefiniowanie zakresu dla każdej osi.
plt.axis([2, 12, 0, 11])

plt.scatter(results, frequencies, s=50)
plt.show()
