import unittest
from country_codes import get_country_code


class TestCodes(unittest.TestCase):

    def test_give_default_raise_1(self):
        self.assertEqual(get_country_code('Andorra'), 'ad')

    def test_give_default_raise_2(self):
        self.assertEqual(get_country_code('United Arab Emirates'), 'ae')

    def test_give_default_raise_3(self):
        self.assertEqual(get_country_code('Afghanistan'), 'af')

    def test_give_default_raise_4(self):
        self.assertNotEqual(get_country_code('Poland'), 'pu')


unittest.main(argv=['first-arg-is-ignored'], exit=False)
