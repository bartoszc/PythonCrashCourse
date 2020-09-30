import csv
from matplotlib import pyplot as plt
from datetime import datetime

filename = 'bangkok_2015.csv'
with open(filename) as f:
    reader = csv.reader(f)
    header_row = next(reader)

    dates, hums = [], []

    for row in reader:
        try:
            current_date = datetime.strptime(row[0], "%Y-%m-%d")
            hum = int(row[8])
        except ValueError:
            print(current_date, 'Brak danych.')
        else:
            dates.append(current_date)
            hums.append(hum)

# Dane wykresu.
fig = plt.figure(dpi=128, figsize=(10, 6))
plt.plot(dates, hums, c='red', alpha=0.5)

# Formatowanie wykresu.
title = "Najwyższa i najniższa temperatura dnia - 2015\nBangkok"
plt.title(title, fontsize=20)
plt.xlabel('', fontsize=16)
plt.ylabel("Temperatura (F)", fontsize=16)
fig.autofmt_xdate()
plt.tick_params(axis='both', which='major', labelsize=16)

plt.show()