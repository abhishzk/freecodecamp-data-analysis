import unittest
import sea_level_predictor

class SeaLevelPredictorTestCase(unittest.TestCase):
    def test_plot_sea_level(self):
        # Test if the function runs without errors
        sea_level_predictor.plot_sea_level('epa-sea-level.csv')

    def test_plot_sea_level_since_2000(self):
        # Test if the function runs without errors
        sea_level_predictor.plot_sea_level_since_2000('epa-sea-level.csv')

if __name__ == '__main__':
    unittest.main()
