import requests
import pygal
from pygal.style import LightColorizedStyle as LCS, LightenStyle as LS

# Wykonanie wywołania API i zachowanie otrzymanej odpowiedzi.

URL = 'https://api.github.com/search/repositories?q=language:javascript&sort=star'
r = requests.get(URL)
print("Kod stanu:", r.status_code)

# Umieszczenie odpowiedzi API w zmiennej.
response_dict = r.json()
print("Całkowita liczba repozytoriów:", response_dict['total_count'])

# Przetworzenie informacji o repozytoriach.
repo_dicts = response_dict['items']

names, plot_dicts = [], []
for repo_dict in repo_dicts:
    names.append(repo_dict['name'])

    plot_dict = {'value': repo_dict['stargazers_count'],
                 'label': str(repo_dict['description']),
                 'xlink': repo_dict['html_url']}

    plot_dicts.append(plot_dict)

# Utworzenie wizualizacji.
my_style = LS('#333366', base_style=LCS)

my_config = pygal.Config()
my_config.x_label_rotation = 45
my_config.show_legend = False
my_config.title_font_size = 24
my_config.label_font_size = 14
my_config.major_label_font_size = 18
my_config.truncate_label = 15
my_config.show_y_guides = False
my_config.width = 1000

chart = pygal.Bar(my_config, style=my_style)
chart.force_uri_protocol = 'http'
chart.title = 'Oznaczone największą liczbą gwiazdek projekty JS w serwisie GitHub'
chart.x_labels = names
chart.add('', plot_dicts)
chart.render_to_file('js_repos.svg')
