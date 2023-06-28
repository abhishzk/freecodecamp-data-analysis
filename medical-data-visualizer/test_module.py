import unittest
from medical_data_visualizer import draw_cat_plot, draw_heat_map

class MedicalDataVisualizerTestCase(unittest.TestCase):
    def test_draw_cat_plot(self):
        # Test if the function runs without errors
        draw_cat_plot()

    def test_draw_heat_map(self):
        # Test if the function runs without errors
        draw_heat_map()

if __name__ == '__main__':
    unittest.main()
