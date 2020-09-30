from pygal.maps.world import COUNTRIES


def get_country_code(country_name):
    """Zwraca stosowany przez Pygal dwuznakowy kod państwa przypisany danemu państwu."""
    for code, name in COUNTRIES.items():
        if name == country_name:
            return code
        else:
            nc = country_name.replace(',', '').split()[0]
            if name == nc:
                return code

    # Jeżeli państwo nie zostało znalezione, wartością zwrotną będzie None.
    return None
