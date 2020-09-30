import csv
from pygal.maps.world import World
from pygal.style import RotateStyle
from country_codes import get_country_code

filename = 'file_one.csv'
with open(filename) as f:
    reader = csv.reader(f)
    for i in range(5):
        header_row = next(reader)

    cc_populations = {}

    for row in reader:
        country_name = row[0]
        data = row[58]
        code = get_country_code(country_name)
        if code:
            try:
                cc_populations[code] = float(data)
            except ValueError:
                continue

wm_style = RotateStyle('#336699')
wm = World(style=wm_style)
wm.force_uri_protocol = 'http'
wm.add('Forests', cc_populations)
wm.render_to_file('world_16.svg')
