import json
from country_codes import get_country_code
from pygal.maps.world import World
from pygal.style import RotateStyle


# Wczytanie danych i umieszczenie ich na liście.
filename = 'gdp_json.json'
with open(filename) as f:
    pop_data = json.load(f)

# Utworzenie słownika danych dotyczących populacji.
cc_populations = {}
for pop_dict in pop_data:
    if str(pop_dict['Year']) == '2010':
        country_name = pop_dict['Country Name']
        population = pop_dict['Value']
        code = get_country_code(country_name)
        if code:
            cc_populations[code] = float(population)

print(cc_populations)
wm_style = RotateStyle('#336699')
wm = World(style=wm_style)
wm.force_uri_protocol = 'http'
wm.value_formatter = lambda x: "%.2f" % x
wm.add('GDP', cc_populations)
wm.render_to_file('world_gdp.svg')

