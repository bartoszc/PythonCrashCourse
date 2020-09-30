from pygal.maps.world import COUNTRIES
import pprint
import json

pprint.pprint(COUNTRIES)

# Wczytanie danych i umieszczenie ich na liście.
filename = 'population_data.json'
with open(filename) as f:
    pop_data = json.load(f)


for pop_dict in pop_data:
    if pop_dict['Year'] == '2010':
        print(pop_dict['Country Name'])