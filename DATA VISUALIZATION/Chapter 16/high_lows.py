import csv
from matplotlib import pyplot as plt
from datetime import datetime

filename = 'death_valley_2014.csv'
with open(filename) as f:
    reader = csv.reader(f)
    header_row = next(reader)

    dates, highs, lows = [], [], []

    for row in reader:
        try:
            current_date = datetime.strptime(row[0], "%Y-%m-%d")
            high = int(row[1])
            low = int(row[3])
        except ValueError:
            print(current_date, 'Brak danych.')
        else:
            dates.append(current_date)
            highs.append(high)
            lows.append(low)

# Dane wykresu.
fig = plt.figure(dpi=128, figsize=(10, 6))
plt.ylim(-100, 100)
plt.plot(dates, highs, c='red', alpha=0.5)
plt.plot(dates, lows, c='blue', alpha=0.5)
plt.fill_between(dates, highs, lows, facecolor='blue', alpha=0.1)

# Formatowanie wykresu.
title = "Najwyższa i najniższa temperatura dnia - 2014\nDolina Śmierci, Kalifornia"
plt.title(title, fontsize=20)
plt.title("Najwyższa i najniższa temperatura dnia - 2014", fontsize=24)
plt.xlabel('', fontsize=16)
plt.ylabel("Temperatura (F)", fontsize=16)
fig.autofmt_xdate()
plt.tick_params(axis='both', which='major', labelsize=16)

plt.show()