import unittest
from demographic_data_analyzer import calculate_demographic_data

class DemographicDataAnalyzerTestCase(unittest.TestCase):
    def setUp(self):
        self.data = calculate_demographic_data()

    def test_race_counts(self):
        self.assertEqual(self.data['race_counts']['White'], 27816)
        self.assertEqual(self.data['race_counts']['Black'], 3124)
        self.assertEqual(self.data['race_counts']['Asian-Pac-Islander'], 1039)
        self.assertEqual(self.data['race_counts']['Amer-Indian-Eskimo'], 311)
        self.assertEqual(self.data['race_counts']['Other'], 271)

    def test_average_age_men(self):
        self.assertAlmostEqual(self.data['average_age_men'], 39.4, places=1)

    def test_percentage_bachelors(self):
        self.assertAlmostEqual(self.data['percentage_bachelors'], 16.4, places=1)

    def test_higher_education_rich(self):
        self.assertAlmostEqual(self.data['higher_education_rich'], 46.5, places=1)

    def test_lower_education_rich(self):
        self.assertAlmostEqual(self.data['lower_education_rich'], 17.4, places=1)

    def test_min_work_hours(self):
        self.assertEqual(self.data['min_work_hours'], 1)

    def test_rich_percentage(self):
        self.assertAlmostEqual(self.data['rich_percentage'], 10.0, places=1)

    def test_highest_earning_country(self):
        self.assertEqual(self.data['highest_earning_country'], 'United-States')

    def test_highest_earning_percentage(self):
        self.assertAlmostEqual(self.data['highest_earning_percentage'], 25.0, places=1)

if __name__ == '__main__':
    unittest.main()
