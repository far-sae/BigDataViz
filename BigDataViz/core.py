from .utils import load_data
from .plot_with_simhei import plot_data, plot_data_with_annotations, plot_pairplot
from .preprocess import preprocess_data


class BigDataViz:
    def __init__(self, file_path: str):
        self.data = load_data(file_path)

    def preprocess(self, operations: dict):
        self.data = preprocess_data(self.data, operations)

    def plot(self, plot_type="scatter", **kwargs):
        plot_data(self.data, plot_type, **kwargs)

    def plot_with_annotations(self, plot_type="scatter", **kwargs):
        plot_data_with_annotations(self.data, plot_type, **kwargs)

    def plot_pair(self):
        plot_pairplot(self.data)
