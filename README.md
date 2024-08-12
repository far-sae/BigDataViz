
# BigDataViz

## Overview

**BigDataViz** is a Python library designed for visualizing large datasets efficiently. It leverages `Dask` for data processing and `Matplotlib` for creating scatter plots, including features for annotating data points. The library also provides tools for working with CJK characters using fonts like SimHei.

## Features

- **Efficient Data Handling**: Process large datasets using `Dask`.
- **Customizable Scatter Plots**: Create scatter plots with full annotations, supporting CJK characters.
- **Interactive Plots**: Explore data interactively with `Plotly`.
- **Aggregation**: Reduce data density by aggregating data points.

## Installation

1. **Clone the repository**:
    ```bash
    git clone https://github.com/far-sae/BigDataViz.git
    cd BigDataViz
    ```

2. **Set up a virtual environment**:
    ```bash
    python3 -m venv .venv
    source .venv/bin/activate  # On Windows use `.venv\Scripts\activate`
    ```

3. **Install the required packages**:
    ```bash
    pip install -r requirements.txt
    ```

4. **Ensure you have the necessary fonts**:
    - If you plan to use CJK characters, make sure the SimHei font is installed on your system.
    - On macOS:
        - `/Library/Fonts/` or `~/Library/Fonts/`
    - On Windows:
        - `C:\Windows\Fonts\`
    - On Linux:
        - `/usr/share/fonts/` or `~/.fonts/`

## Usage

### Example Usage

```python
from BigDataViz import BigDataViz

# Load the dataset
viz = BigDataViz("path/to/your/large_dataset.csv")

# Drop rows with NaN values in 'height' and 'weight'
viz.data = viz.data.dropna(subset=['height', 'weight'])

# Plotting height vs. weight with full annotations for all columns
viz.plot_with_annotations(plot_type="scatter", color="blue", s=10)
```

### Interactive Plotting

For large datasets, consider using interactive plots:

```python
import plotly.express as px

def plot_interactive(data):
    fig = px.scatter(data, x='height', y='weight', text='name')
    fig.update_traces(marker=dict(size=5),
                      selector=dict(mode='markers'))
    fig.show()
```

### Reducing Data Density

If the data is too dense for clear visualization, consider aggregating it:

```python
data_grouped = viz.data.groupby('height').agg({'weight': 'mean'}).reset_index()
viz.plot_with_annotations(data_grouped, plot_type="scatter", color="blue", s=10)
```

## Configuration

### Font Setup

If your plots require CJK characters, you'll need to specify the correct path to the `SimHei.ttf` font in your script:

```python
import matplotlib.font_manager as fm

# Specify the path to the SimHei.ttf file
font_path = '/path/to/SimHei.ttf'  # Update this with the actual path

# Set up the font
font_prop = fm.FontProperties(fname=font_path)
plt.rcParams['font.sans-serif'] = [font_prop.get_name()]
```

### Annotating Large Datasets

To avoid overcrowded annotations, you can limit the number of annotated points:

```python
def plot_data_with_annotations(data, plot_type="scatter", **kwargs):
    # Annotate only the first 100 points
    for i in range(min(100, len(data))):
        # Annotation code here...
```

## Contributing

Contributions are welcome! Please open an issue or submit a pull request.

## Acknowledgements

- This project uses [Dask](https://dask.org/), [Matplotlib](https://matplotlib.org/), and [Plotly](https://plotly.com/python/).
- Thanks to all contributors and the open-source community.
