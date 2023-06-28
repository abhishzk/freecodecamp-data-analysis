import unittest
import time_series_visualizer

class DataVisualizerTestCase(unittest.TestCase):
    def test_draw_line_plot(self):
        # Test if the function runs without errors
        time_series_visualizer.draw_line_plot('fcc-forum-pageviews.csv')

    def test_draw_bar_plot(self):
        # Test if the function runs without errors
        time_series_visualizer.draw_bar_plot('fcc-forum-pageviews.csv')

    def test_draw_box_plot(self):
        # Test if the function runs without errors
        time_series_visualizer.draw_box_plot('fcc-forum-pageviews.csv')

if __name__ == '__main__':
    unittest.main()
