import unittest
from city_functions import full_name


class CitiesTestCase(unittest.TestCase):
    """Testy dla programu 'name_function.py'."""

    def test_city_country(self):
        """"Czy dane w postaci 'Janis Joplin' są obsługiwane prawidłowo?"""
        formatted_name = full_name('santiago', 'chile')
        self.assertEqual(formatted_name, 'Santiago, Chile')

    def test_city_country_population(self):
        """"Czy dane w postaci 'Janis Joplin' są obsługiwane prawidłowo?"""
        formatted_name = full_name('santiago', 'chile', '5000000')
        self.assertEqual(formatted_name, 'Santiago, Chile - population 5000000')


unittest.main(argv=['first-arg-is-ignored'], exit=False)