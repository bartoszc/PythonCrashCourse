def full_name(city, country, population=''):
    if population:
        full_name = city + ', ' + country
        return full_name.title() + ' - population ' + population
    else:
        full_name = city + ', ' + country
        return full_name.title()

