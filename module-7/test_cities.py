#test_cities.py

import unittest
from city_functions import city_country

class TestCityCountry(unittest.TestCase):
    """Tests for the city_country function."""

    def test_city_country(self):
        result = city_country("santiago", "chile")
        self.assertEqual(result, "Santiago, Chile")

    def test_city_country_population(self):
        result = city_country("kathmandu", "nepal", population=1000000)
        self.assertEqual(result, "Kathmandu, Nepal - population 1000000")

    def test_city_country_population_language(self):
        result = city_country("tokyo", "japan", population=14000000, language="japanese")
        self.assertEqual(result, "Tokyo, Japan - population 14000000, Japanese")

if __name__ == '__main__':
    unittest.main()
