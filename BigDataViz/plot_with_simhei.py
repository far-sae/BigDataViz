import matplotlib.pyplot as plt
import matplotlib.font_manager as fm
import pandas as pd
import seaborn as sns
import datashader as ds
from datashader import transfer_functions as tf
import warnings

# Path to SimHei or another comprehensive font like Noto Sans CJK SC
font_path = '/System/Library/Fonts/Supplemental/Arial Unicode.ttf'  # Replace with the correct path to SimHei.ttf or Noto Sans CJK SC
try:
    font_prop = fm.FontProperties(fname=font_path)
    plt.rcParams['font.sans-serif'] = [font_prop.get_name()]
except Exception as e:
    # Fallback to a more comprehensive built-in font if SimHei is not available
    print(f"Failed to load SimHei font. Error: {e}")
    plt.rcParams['font.sans-serif'] = ['Noto Sans CJK SC']

plt.rcParams['axes.unicode_minus'] = False

# Handle missing glyph warnings gracefully
warnings.filterwarnings("ignore", message="Glyph .* missing from current font")

def plot_data(data, plot_type="scatter", **kwargs):
    if not isinstance(data, pd.DataFrame):
        data = data.compute()

    if len(data) > 1e6:
        canvas = ds.Canvas(plot_width=800, plot_height=600)
        agg = canvas.points(data, x='height', y='weight')
        img = tf.shade(agg)
        img.to_pil().show()
    else:
        plt.figure(figsize=(10, 6))
        if plot_type == "scatter":
            plt.scatter(data['height'], data['weight'], **kwargs)
        plt.xlabel('Height', fontproperties=font_prop)
        plt.ylabel('Weight', fontproperties=font_prop)
        plt.title('Height vs. Weight Scatter Plot', fontproperties=font_prop)
        plt.show()

def plot_data_with_annotations(data, plot_type="scatter", **kwargs):
    if not isinstance(data, pd.DataFrame):
        data = data.compute()

    plt.figure(figsize=(12, 8))

    if plot_type == "scatter":
        plt.scatter(data['height'], data['weight'], **kwargs)

        # Annotate each point with all column details
        for i in range(len(data)):
            annotation_text = (
                f"ID: {data['athlete_id'].iloc[i]}\n"
                f"Name: {data['name'].iloc[i]}\n"
                f"Sex: {data['sex'].iloc[i]}\n"
                f"Born: {data['born'].iloc[i]}\n"
                f"Height: {data['height'].iloc[i]}\n"
                f"Weight: {data['weight'].iloc[i]}\n"
                f"Country: {data['country'].iloc[i]}\n"
                f"Country NOC: {data['country_noc'].iloc[i]}\n"
                f"Description: {data['description'].iloc[i]}\n"
                f"Special Notes: {data['special_notes'].iloc[i]}"
            )
            plt.annotate(
                annotation_text,
                (data['height'].iloc[i], data['weight'].iloc[i]),
                textcoords="offset points",
                xytext=(5, 5),
                ha='left',
                fontsize=8,
                alpha=0.7,
                fontproperties=font_prop  # Use the manually specified font
            )

    plt.xlabel('Height', fontproperties=font_prop)
    plt.ylabel('Weight', fontproperties=font_prop)
    plt.title('Height vs. Weight Scatter Plot with Full Annotations', fontproperties=font_prop)
    plt.show()

def plot_pairplot(data):
    if not isinstance(data, pd.DataFrame):
        data = data.compute()

    numeric_data = data[['height', 'weight']].dropna()

    sns.pairplot(numeric_data)
    plt.show()

# Example Usage

def main():
    # Load a sample dataset
    data = pd.DataFrame({
        'athlete_id': [1, 2, 3],
        'name': ['张三', '李四', '王五'],
        'sex': ['M', 'F', 'M'],
        'born': ['1990-01-01', '1985-02-02', '1992-03-03'],
        'height': [180, 165, 170],
        'weight': [75, 55, 65],
        'country': ['China', 'China', 'China'],
        'country_noc': ['CHN', 'CHN', 'CHN'],
        'description': ['优秀运动员', '国际比赛冠军', '省级比赛冠军'],
        'special_notes': ['无', '注意事项', '无']
    })

    # Drop rows with NaN values in 'height' and 'weight'
    data = data.dropna(subset=['height', 'weight'])

    # Plotting height vs. weight with full annotations for all columns
    plot_data_with_annotations(data, plot_type="scatter", color="blue", s=100)

    # Optionally, create a pair plot of the data
    # plot_pairplot(data)

if __name__ == "__main__":
    main()
