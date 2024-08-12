# tests/test_core.py
import unittest
from BigDataViz.core import BigDataViz

class TestBigDataViz(unittest.TestCase):
    def test_load_data(self):
        viz = BigDataViz("/Users/farazsaeed/BigDataViz/examples/Olympic_Athlete_Bio.csv")
        self.assertTrue(viz.data is not None)

    def test_plot(self):
        viz = BigDataViz("/Users/farazsaeed/BigDataViz/examples/Olympic_Athlete_Bio.csv")
        viz.plot(plot_type="scatter", color="blue")

if __name__ == "__main__":
    unittest.main()
