import unittest
from city_functions import get_city_country


class CityTestCase(unittest.TestCase):
    """Tests for 'city_functions.py'."""

    def test_city_country(self):
        """Do cities like 'Santiago, Chile' work?"""
        formatted_city = get_city_country('santiago', 'chile')
        self.assertEqual(formatted_city, 'Santiago, Chile')

    def test_city_county_population(self):
        """Do cities like 'Santiago, Chile - population 5 000 000' work?"""
        formatted_city = get_city_country('santiago', 'chile', '5 000 000')
        self.assertEqual(formatted_city, 'Santiago, Chile - population 5 000 000')

    if __name__ == '__main__':
        unittest.main()
